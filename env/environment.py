from tasks.task_manager import get_task
from graders.easy_grader import grade_easy
from graders.medium_grader import grade_medium
from graders.hard_grader import grade_hard

from env.state import State
from env.observation import Observation
from env.reward import Reward


class CodeReviewEnv:

    def __init__(self):
        self.current_state = None

    def reset(self, task="easy"):
        code, true_issues = get_task(task)

        self.current_state = State(
            code=code,
            true_issues=true_issues,
            task_type=task,
            done=False
        )

        observation = Observation(
            code=code,
            instruction="Review this Python code and identify issues"
        )

        return observation.dict()

    def step(self, review):
        if self.current_state is None:
            raise ValueError("Call reset() first")

        if self.current_state.task_type == "easy":
            score = grade_easy(review, self.current_state.true_issues)

        elif self.current_state.task_type == "medium":
            score = grade_medium(review, self.current_state.true_issues)

        elif self.current_state.task_type == "hard":
            score = grade_hard(review, self.current_state.true_issues)

        else:
            raise ValueError("Invalid task type")

        self.current_state.done = True

        observation = Observation(
            code=self.current_state.code,
            instruction="Review this Python code and identify issues"
        )

        return (
    observation.dict(),
    score,
    self.current_state.done,
    {
        "matched_issues": self.current_state.true_issues,
        "detected_issues": [issue for issue in self.current_state.true_issues if issue in review.lower()],

        "score_explanation": f"Matched {score*100}% of expected issues"
    }
)

    def state(self):
        return self.current_state.dict()