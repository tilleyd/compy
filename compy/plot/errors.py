"""Contains custom exception classes."""


class PlotError(Exception):
    """Parent class of all image related errors."""

    def __init__(self, message):
        super().__init__(message)


class NotShowableError(PlotError):
    """Error if trying to show a figure that belongs to a grid."""

    def __init__(self):
        self.message = "Attempted to call show() on a figure that belongs to a grid. Use Grid.show()."
        super().__init__(self.message)
