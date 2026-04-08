import ast
from app.models import Observation, Reward
from app.tasks import TASKS
from app.grader import grade

class ShadowEnv:

    def __init__(self):
        self.code = ""
        self.steps = 0
        self.prev_score = 0
        self.history = []

    def reset(self, task_id="easy"):
        self.task_id = task_id
        self.task = TASKS[task_id]
        self.code = self.task["initial_code"]
        self.steps = 0
        self.prev_score = 0
        self.history = []
        return self._obs()

    def state(self):
        return self._obs()

    def step(self, action):
        prev = self.code

        if action.action_type == "FIX_SYNTAX":
            self.code = self.code.replace("def add(a,b)", "def add(a,b):")

        elif action.action_type == "FIX_BUG":
            self.code = self.code.replace("/ 0", "/ 1")

        elif action.action_type == "REFACTOR":
            self.code = self.code.replace("range(len(lst))", "lst")

        elif action.action_type == "AUTOCOMPLETE":
            self.code += "\n# suggestion"

        self.steps += 1
        self.history.append(self.code)

        score = grade(self.task_id, self.code, self.task)
        reward = (score - self.prev_score) * 10

        if prev == self.code:
            reward -= 1
        if self.history.count(self.code) > 2:
            reward -= 2

        self.prev_score = score
        done = score == 1.0 or self.steps >= 15

        return self._obs(), Reward(value=reward), done, {}

    def _obs(self):
        errors = []
        try:
            ast.parse(self.code)
        except:
            errors.append("Syntax Error")

        return Observation(
            code=self.code,
            errors=errors,
            tests_passed=(len(errors)==0 and "return" in self.code),
            task_id=self.task_id
        )
