from pydantic import BaseModel
from typing import List


class State(BaseModel):
    code: str
    true_issues: List[str]
    task_type: str
    done: bool