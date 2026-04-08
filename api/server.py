from fastapi import FastAPI
from env.environment import CodeReviewEnv
from env.action import Action
import requests

app = FastAPI()

env = CodeReviewEnv()


# 🔹 RESET
@app.post("/reset")
def reset(task: str = "easy"):
    observation = env.reset(task)
    return observation


@app.post("/step")
def step():
    if env.current_state is None:
        return {"error": "Call /reset first"}

    code = env.current_state.code

    # 🔥 CALL PHI-3 (OLLAMA)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": f"""
You are an expert Python code reviewer.
Find bugs in this code:

{code}

List issues clearly:
""",
            "stream": False
        }
    )

    result = response.json()
    ai_review = result.get("response", "")

    # 👉 PASS AI REVIEW TO ENV
    observation, reward, done, info = env.step(ai_review)

    return {
        "ai_review": ai_review,
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": info
    }


# 🔹 STATE
@app.get("/state")
def state():
    if env.current_state is None:
        return {"error": "Environment not initialized. Call /reset first"}

    return env.state()