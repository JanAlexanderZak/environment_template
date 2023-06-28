""" Mockup class
"""

class ActivationFuncs:
    def __init__(self):
        pass

    def step(z):
        return np.sign(z)

    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    def relu(z):
        return np.maximum(0, z)