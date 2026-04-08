from pydantic import BaseModel


class Observation(BaseModel):
    code: str
    instruction: str