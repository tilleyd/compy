"""Contains the figure class, which represents a single plot."""

from typing import Optional, Tuple
import matplotlib.pyplot as plt


class Figure:
    def __init__(
        self,
        title: Optional[str] = None,
        xlabel: Optional[str] = None,
        ylabel: Optional[str] = None,
        xrange: Optional[Tuple[float, float]] = None,
        yrange: Optional[Tuple[float, float]] = None,
        size: Optional[Tuple[float, float]] = None,
        ax: Optional[plt.Axes] = None,
    ):
        """Creates a standalone figure.

        Args:
            title: Optional plot title.
            xlabel: Optional label for the x-axis.
            ylabel: Optional label for the y-axis.
            xrange: Optional (min, max) range for the x-axis. Will be determined
                automatically if not specified.
            yrange: Optional (min, max) range for the y-axis. Will be determined
                automatically if not specified.
            size: Optional size in inches, (width, height). Ignored if ax is
                specified.
            ax: Optional matplotlib Axes object to draw to instead of creating
                a new figure.
        """
        self.figure = None

        # Keep track of colours used
        self.colours = ["tomato", "orange", "steelblue"]
        self.line_count = 0
        self.point_count = 0

        if ax is None:
            self.figure = plt.figure(figsize=size)
            self.ax = self.figure.add_subplot()
        else:
            self.ax = ax

        if title is not None:
            self.set_title(title)
        if xlabel is not None:
            self.set_xlabel(xlabel)
        if ylabel is not None:
            self.set_ylabel(ylabel)
        if xrange is not None:
            self.set_xrange(xrange)
        if yrange is not None:
            self.set_yrange(yrange)
        self.ax.set_facecolor("whitesmoke")

    def plot_line(self, x, y, label=None):
        """Plots a line passing through the given coordinates."""
        if self.line_count < len(self.colours):
            clr = self.colours[self.line_count]
        else:
            clr = None
        self.line_count += 1
        self.ax.plot(x, y, c=clr, label=label)
        if label is not None:
            self.enable_legend()

    def plot_points(self, x, y, label=None):
        """Plots (scatters) points at the given coordinates."""
        if self.point_count < len(self.colours):
            clr = self.colours[self.point_count]
        else:
            clr = None
        self.point_count += 1
        self.ax.scatter(x, y, c=clr, label=label)
        if label is not None:
            self.enable_legend()

    def plot_image(self, image):
        """Plots the pixels of an image.

        Args:
            image: Array of shape (h, w) or (h, w, c), either in floating point
                values with range [0, 1] or int values in range [0, 255].
        """
        cmap = "gist_gray"
        self.ax.imshow(image, cmap=cmap)

    def set_title(self, title):
        self.ax.set_title(title)

    def set_xlabel(self, xlabel):
        self.ax.set_xlabel(xlabel)

    def set_ylabel(self, ylabel):
        self.ax.set_ylabel(ylabel)

    def set_xrange(self, xrange):
        self.ax.set_xlim(xrange[0], xrange[1])

    def set_yrange(self, yrange):
        self.ax.set_ylim(yrange[0], yrange[1])

    def enable_grid(self):
        """Shows vertical and horizontal grid lines."""
        self.ax.grid()
        self.ax.set_axisbelow(True)

    def enable_legend(self):
        """Shows the legend."""
        self.ax.legend()

    def show(self):
        """Show the figure when in interactive mode."""
        from .errors import NotShowableError

        if self.figure is not None:
            self.figure.show()
        else:
            raise NotShowableError()

    def save(self, path):
        """Save the figure to a image or pdf file path."""
        from .errors import NotShowableError

        if self.figure is not None:
            self.figure.savefig(path, bbox_inches="tight")
        else:
            raise NotShowableError()
