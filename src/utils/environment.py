import os

# @class Env
# @desc Simple class the allows us to easily
# interact with environment variables.
class Env:
    # Static method that will retrieve the value of a single
    # environment variable from the OS.
    # @param var Title of the variable to retrieve
    @staticmethod
    def get(var):
        if var in os.environ:
            return os.environ[var]
        return None
