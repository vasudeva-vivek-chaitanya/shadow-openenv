from app.env import ShadowEnv
from app.models import Action

env = ShadowEnv()

for t in ["easy","medium","hard"]:
    s = env.reset(t)
    done=False
    while not done:
        code = s.code
        if "Syntax Error" in str(s.errors):
            a = Action(action_type="FIX_SYNTAX")
        elif "/ 0" in code:
            a = Action(action_type="FIX_BUG")
        elif "range(len" in code:
            a = Action(action_type="REFACTOR")
        else:
            a = Action(action_type="AUTOCOMPLETE")
        s, r, done, _ = env.step(a)
    print(t, "completed:", s.tests_passed)
