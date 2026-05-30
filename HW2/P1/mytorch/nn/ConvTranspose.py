import numpy as np
from resampling import *
from Conv1d import *
from Conv2d import *


class ConvTranspose1d:
    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        upsampling_factor,
        weight_init_fn=None,
        bias_init_fn=None,
    ):
        # Do not modify this method
        self.upsampling_factor = upsampling_factor

        # Initialize Conv1d stride 1 and upsample1d isntance
        self.upsample1d = # TODO
        self.conv1d_stride1 = # TODO


    def forward(self, A):
        """
        Argument:
            A (np.array): (batch_size, in_channels, input_size)
        Return:
            Z (np.array): (batch_size, out_channels, output_size)
        """
        
        Z = # TODO (<= 2 lines of code)

        # 1. Upsampling1d forward

        # 2. Conv1d_stride1 forward
        

        return Z


    def backward(self, dLdZ):
        """
        Argument:
            dLdZ (np.array): (batch_size, out_channels, output_size)
        Return:
            dLdA (np.array): (batch_size, in_channels, input_size)
        """
        
        dLdA = # TODO (<= 2 lines of code)

        # 1. Conv1d_stride1 backward

        # 2. Upsampling1d backward
        

        return dLdA


class ConvTranspose2d:
    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        upsampling_factor,
        weight_init_fn=None,
        bias_init_fn=None,
    ):
        # Do not modify this method
        self.upsampling_factor = upsampling_factor

        # Initialize Conv2d() isntance
        self.conv2d_stride1 = # TODO
        self.upsample2d = # TODO

    def forward(self, A):
        """
        Argument:
            A (np.array): (batch_size, in_channels, input_size)
        Return:
            Z (np.array): (batch_size, out_channels, output_size)
        """
        
        Z = # TODO (<= 2 lines of code)

        # 1. Upsampling2d forward

        # 2. Conv2d_stride1 forward

        return Z

    def backward(self, dLdZ):
        """
        Argument:
            dLdZ (np.array): (batch_size, out_channels, output_size)
        Return:
            dLdA (np.array): (batch_size, in_channels, input_size)
        """
        

        dLdA = # TODO (<= 2 lines of code)

        # 1. Conv2d_stride1 backward

        # 2. Upsampling2d backward
        

        return dLdA
