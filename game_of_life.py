# Conway's game of life v0

# Import libs
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation


class GAME_OF_LIFE(object):
    # Perform convolution with kernal of ones([3,3])
    def convolution2d(self, x):
        # Variable init
        conv = np.zeros_like(x)
        m, n = conv.shape
        # For conv2d  output size = (N - F) / stride + 1
        # F = 3 and stride = 1
        # Hence the input matrix should be padded with on each side by 1
        x = np.lib.pad(x, ((1,), (1,)), 'constant')

        # Convolve
        for i in range(m):
            for j in range(n):
                conv[i][j] = np.sum(x[i:i+3, j:j+3])

        return conv

    def find_next_state(self, old_state):
        # Find the 2D convolution
        conv = self.convolution2d(old_state)
        # Initialize output
        new_state = np.zeros_like(old_state)
        # If sum is 3, inner box is always 1
        new_state[conv == 3] = 1
        # If sum is 4, inner box continues to have initial value
        new_state[conv == 4] = old_state[conv == 4]

        return new_state

    # Renders the graph in matplotlib
    # Params: initial state, number of itrations
    def render_matplotlib(self, x, count):
        # Initialize the plot
        fig = plt.figure()
        fig.show()
        # Draw initial state
        im = plt.imshow(x, animated=True)
        fig.canvas.draw()
        # Loop
        for i in range(count):
            x = self.find_next_state(x)
            im.set_array(x)
            fig.canvas.draw()

    # Renders the graph in matplotlib
    # Params: initial state, number of itrations
    def save_as_video(self, x, count):
        # Initialize video writer
        FFMpegWriter = manimation.writers['ffmpeg']
        metadata = dict(title='Game of Life')
        writer = FFMpegWriter(fps=15, metadata=metadata)
        # Initialize the plot
        fig = plt.figure()
        # Loop
        with writer.saving(fig, "game_of_life.mp4", count+1):
            # Draw initial state
            im = plt.imshow(x, animated=True)
            fig.canvas.draw()
            writer.grab_frame()
            for i in range(count):
                x = self.find_next_state(x)
                im.set_array(x)
                fig.canvas.draw()
                writer.grab_frame()

    # Renders the graph on terminal
    # Params: initial state, number of itrations
    def render_terminal(self, x, count):
        # Draw initial state
        self.print_on_terminal(x)
        # Loop
        for i in range(count):
            x = self.find_next_state(x)
            self.print_on_terminal(x)
        # Makes sure that cursor is at right place after exceution of programm
        sys.stdout.write('\n')

    # Print loop for terminal
    def print_on_terminal(self, x):
        m, n = x.shape

        for i in range(m):
            for j in range(n):
                if (x[i][j] == 1):
                    sys.stdout.write(u'\u2588')
                else:
                    sys.stdout.write(' ')
            sys.stdout.write('\n')
        # A bit of hack: moves cursor to start of previous line
        for i in range(m):
            sys.stdout.write(u'\033[F')
