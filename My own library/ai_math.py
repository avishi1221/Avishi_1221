import math

def sigmoid(x):
    """Computes the sigmoid activation function."""
    return 1 / (1 + math.exp(-x))

def relu(x):
    """Computes the ReLU activation function."""
    return max(0, x)

def mse_loss(y_true, y_pred):
    """Computes Mean Squared Error loss."""
    return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)
