from pyfmi import load_fmu
def test_pyfmi(mode="CS"):
    
    if(mode == "CS"):
        model = load_fmu("./resources/dymola/windows/ModelicaGym_CartPole_CS.fmu", kind=mode, log_level=7)
    elif(mode == "ME"):
        model = load_fmu("./resources/dymola/windows/ModelicaGym_CartPole_ME.fmu", kind=mode, log_level=7)
    else:
        model = load_fmu("./resources/dymola/windows/ModelicaGym_CartPole_CS.fmu", kind=mode, log_level=7)
    
    model.reset()
    model.setup_experiment(start_time=0)
    model.initialize()
    opts = model.simulate_options()
    opts['ncp'] = 50
    opts['initialize'] = False
    model.set("f", -1)
    model.simulate(start_time=0, final_time=2, options=opts)
    model.set("f", -1)
    model.simulate(start_time=2, final_time=3, options=opts)
    print("PyFMI is available and successfully simulating.")


def test_gym(visualize=True):
    import gym
    env = gym.make('CartPole-v0')
    env.reset()
    for _ in range(10):
        if visualize:
            env.render()
        env.step(env.action_space.sample())
    env.close()
    print("OpenAI Gym is available and successfully working.")


if __name__ == '__main__':
    test_pyfmi()
    test_gym()
