"""Contains the grid class to create multiple figures."""

from typing import Optional, Tuple
from .figure import Figure
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt


class Grid:
    def __init__(
        self, rows: int, cols: int, size: Optional[Tuple[float, float]] = None
    ):
        """Creates a grid containing multiple subfigures.

        Args:
            rows: Number of figure rows.
            cols: Number of figure columns.
            size: Optional size in inches, (width, height).
        """
        self.rows = rows
        self.cols = cols

        self.grid = gridspec.GridSpec(rows, cols)
        self.figure = plt.figure(figsize=size)

        self.figures = []
        for r in range(rows):
            row = []
            for c in range(cols):
                ax = plt.subplot(self.grid[r, c])
                fig = Figure(ax=ax)
                row.append(fig)
            self.figures.append(row)

    def get_figure(self, row: int, col: int) -> Figure:
        """Return the figure at a specified row and column."""
        return self.figures[row][col]

    def show(self):
        """Show the figure when in interactive mode."""
        self.figure.show()

    def save(self, path):
        """Save the figure to a image or pdf file path."""
        self.figure.savefig(path, bbox_inches="tight")
