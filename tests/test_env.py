from env.environment import CodeReviewEnv


def test_reset():
    env = CodeReviewEnv()
    observation = env.reset("easy")

    assert "code" in observation
    assert "instruction" in observation


def test_step():
    env = CodeReviewEnv()
    env.reset("easy")

    observation, reward, done, _ = env.step("missing colon")

    assert isinstance(reward, float) or isinstance(reward, int)
    assert done is True


def test_state():
    env = CodeReviewEnv()
    env.reset("easy")

    state = env.state()

    assert "code" in state
    assert "true_issues" in state