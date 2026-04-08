from env.environment import CodeReviewEnv


def validate():
    env = CodeReviewEnv()

    try:
        # Test reset
        observation = env.reset("easy")
        assert "code" in observation
        assert "instruction" in observation

        # Test step
        observation, reward, done, _ = env.step("missing colon")
        assert isinstance(reward, float) or isinstance(reward, int)
        assert done is True

        # Test state
        state = env.state()
        assert "code" in state
        assert "true_issues" in state

        print("✅ Environment validation passed")

    except Exception as e:
        print("❌ Validation failed:", str(e))


if __name__ == "__main__":
    validate()