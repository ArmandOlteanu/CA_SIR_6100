import pygame
import numpy as np
def draw(surface, grid, cellsize, S, I, R, col_S, col_I, col_R):
    """Draw the grid."""
    for state in [S, I, R]:
        rows, cols = np.where(grid == state)
        if state == S:
            color = col_S
        elif state == I:
            color = col_I
        else:
            color = col_R
        for r, c in zip(rows, cols):
            pygame.draw.rect(
                surface,
                color,
                (c * cellsize, r * cellsize, cellsize - 1, cellsize - 1),
            )
