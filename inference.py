import requests
import time

BASE_URL = "https://anirudhiu5-ai-code-review-system.hf.space"

# 🔥 HuggingFace Phi-3 API


def generate_review(code):
    prompt = f"""
You are an expert Python code reviewer.
Find bugs and issues in this code:

{code}

List issues clearly:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    print("RAW:", result)

    return result.get("response", "")


def run_task(task):
    print(f"\n===== {task.upper()} =====")

    # 1. GET CODE
    res = requests.post(f"{BASE_URL}/reset", params={"task": task})
    data = res.json()
    code = data["code"]

    print("\nCode:\n", code)

    # 2. 🔥 AI GENERATES REVIEW
    review = generate_review(code)

    print("\nAI Review:\n", review)

    # 3. SEND TO SYSTEM
    res = requests.post(f"{BASE_URL}/step", json={"review": review})
    result = res.json()

    print("Reward:", result["reward"])
    print("Info:", result["info"])


def main():
    for task in ["easy", "medium", "hard"]:
        run_task(task)
        time.sleep(1)


if __name__ == "__main__":
    main()