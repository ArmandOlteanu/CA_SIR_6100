import pygame
import numpy as np

def draw(surface, grid, cellsize, S, I, R, col_S, col_I, col_R):
    # PURPOSE: Draw interactive pygame lattice
    # INPUTS: Inputs to pass to other helper functions:
        # surface: Surface that pygame draws the simulation on.
        # grid: Array that simulation is being conducted on 
        # cellsize: size of cells
        # S, I, R: numeric states for each class (S = 0, I = 1, R = 2)
        # col_S, col_I, col_R: hex codes for the colors of the states
    # OUTPUTS: None
    # SIDE EFFECTS: Interactive SIR grid with keyboard commands.
    
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