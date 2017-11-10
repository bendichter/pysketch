import matplotlib.pyplot as plt
from copy import copy


class NewPad:
    def __init__(self):
        self.pos = [0, 0]
        self.heading = 'up'
        fig, self.ax = plt.subplots()

    def draw(self, length, color='k', linewidth=2, **kwargs):
        new_pos = copy(self.pos)
        if self.heading == 'up':
            new_pos[1] += length
        elif self.heading == 'down':
            new_pos[1] -= length
        elif self.heading == 'right':
            new_pos[0] += length
        else:
            new_pos[0] -= length

        self.ax.plot([self.pos[0], new_pos[0]], [self.pos[1], new_pos[1]],
                     color=color, linewidth=linewidth, **kwargs)
        self.pos = new_pos
        self.ax.axis('scaled')
        self.ax.axis('off')

        xl = self.ax.get_xlim()
        yl = self.ax.get_ylim()
        for x in range(int(xl[0]), int(xl[1])+1):
            for y in range(int(yl[0]), int(yl[1])+1):
                plt.scatter(x, y, 3, color='grey')

    def turn_left(self):
        if self.heading == 'up':
            self.heading = 'left'
        elif self.heading == 'left':
            self.heading = 'down'
        elif self.heading == 'down':
            self.heading = 'right'
        else:
            self.heading = 'up'

    def turn_right(self):
        if self.heading == 'up':
            self.heading = 'right'
        elif self.heading == 'right':
            self.heading = 'down'
        elif self.heading == 'down':
            self.heading = 'left'
        else:
            self.heading = 'up'
