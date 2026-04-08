def mouse_to_cell(pos, cellsize):
    """Convert mouse position to grid cell."""
    x, y = pos
    return y // cellsize, x // cellsize
