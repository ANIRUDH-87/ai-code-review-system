from env.environment import CodeReviewEnv

def main():
    env = CodeReviewEnv()

    tasks = ["easy", "medium", "hard"]

    for task in tasks:
        print(f"\nRunning task: {task}")

        observation = env.reset(task)
        print("Code:\n", observation["code"])

        # Dummy review (for testing)
        review = "This code has issues"

        observation, reward, done, _ = env.step(review)

        print("Reward:", reward)
        print("Done:", done)


if __name__ == "__main__":
    main()