from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Code Review System Running"}

@app.get("/reset")
def reset():
    return {"code": "def greet()\n    print('Hello')", "instruction": "Review code"}

@app.post("/step")
def step(review: dict):
    return {"reward": 1, "done": True}

@app.get("/state")
def state():
    return {"status": "running"}