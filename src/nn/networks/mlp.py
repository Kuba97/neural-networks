from src.nn.activations.hidden_activations import Sigmoid
from src.nn.layers.fully_connected import (FullyConnected)
from src.nn.module import Module


class MultiLayerPerceptron(Module):
    def __init__(self, input_dim, output_dim, initializer):
        super().__init__()
        self.hidden = FullyConnected(in_shape=input_dim,
                                     out_shape=64,
                                     activation=Sigmoid(),
                                     initializer=initializer)

        self.output = FullyConnected(in_shape=64,
                                     out_shape=output_dim,
                                     activation=Sigmoid(),
                                     initializer=initializer)

    def forward(self, x):
        x = self.hidden.forward(x)
        x = self.output.forward(x)
        return x

    def backward(self, upstream_gradients):
        out_grad = self.output.backward(upstream_gradients)
        out_grad = self.hidden.backward(out_grad)
        return out_grad

    def parameters(self):
        return [] + self.hidden.parameters() + self.output.parameters()
