"""Exception Classes file."""


class WrongExtensionError(Exception):
    """WrongFileTypeException Class."""

    def __init__(self, message):
        """WrongFileTypeException Constructor."""
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """WrongFileTypeException String Representation."""
        return render_template('meme_error.html', message="Wrong Extension")
