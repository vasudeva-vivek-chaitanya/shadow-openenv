from fastapi import FastAPI
from app.env import ShadowEnv
from app.models import Action

app = FastAPI()
env = ShadowEnv()


@app.post("/reset")
def reset(task_id: str = "easy"):
    return env.reset(task_id)


@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}


@app.get("/state")
def state():
    return env.state()


@app.post("/reset")
def reset(task_id: str = "easy"):
    return env.reset(task_id)
