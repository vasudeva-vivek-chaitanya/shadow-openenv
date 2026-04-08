import os
from openai import OpenAI
from app.env import ShadowEnv
from app.models import Action


API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN") or os.getenv("OPENAI_API_KEY")

TASKS = ["easy", "medium", "hard"]
BENCHMARK = "shadow-openenv"
MAX_STEPS = 10

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)
env = ShadowEnv()


def log_start(task):
    print(f"[START] task={task} env={BENCHMARK} model={MODEL_NAME}", flush=True)


def log_step(step, action, reward, done, error):
    error_val = error if error else "null"
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error_val}",
        flush=True,
    )


def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )


def get_action(code):
    try:
        res = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": f"""
Fix or improve this code:

{code}

Respond with ONLY one:
AUTOCOMPLETE or FIX_BUG or REFACTOR or FIX_SYNTAX
""",
                }
            ],
        )
        return res.choices[0].message.content.strip()

    except Exception:
        # fallback (mandatory)
        if "Syntax Error" in code:
            return "FIX_SYNTAX"
        if "/ 0" in code:
            return "FIX_BUG"
        if "range(len" in code:
            return "REFACTOR"
        return "AUTOCOMPLETE"


def run_task(task):
    state = env.reset(task)
    done = False

    rewards = []
    step = 0
    error = None

    log_start(task)

    while not done and step < MAX_STEPS:
        action_str = get_action(state.code)

        try:
            action = Action(action_type=action_str)
            state, reward_obj, done, _ = env.step(action)

            reward = reward_obj.value if reward_obj else 0.0
            rewards.append(reward)

            log_step(step + 1, action_str, reward, done, error)

        except Exception as e:
            error = str(e)
            log_step(step + 1, action_str, 0.0, True, error)
            done = True

        step += 1

    # score normalization [0,1]
    total_reward = sum(rewards)
    max_possible = MAX_STEPS * 10  # approximate upper bound
    score = min(max(total_reward / max_possible, 0.0), 1.0)

    success = state.tests_passed

    log_end(success, step, score, rewards)


if __name__ == "__main__":
    for task in TASKS:
        run_task(task)
