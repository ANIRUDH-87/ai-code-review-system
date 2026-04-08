from pydantic import BaseModel


class Action(BaseModel):
    review: str