from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    code: str
    errors: List[str]
    tests_passed: bool
    task_id: str

class Action(BaseModel):
    action_type: str  # AUTOCOMPLETE / FIX_BUG / REFACTOR / FIX_SYNTAX

class Reward(BaseModel):
    value: float
