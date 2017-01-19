from src.utils.environment import Env

# @class Logger
# @desc Simple class that allows us to easily
# print out logs to the command-line.
class Logger:
    # Static method that prints a debug message to the terminal
    # if, and only if, the 'DEBUG' environment variable is set True.
    @staticmethod
    def debug(message):
        if Env.get('DEBUG'):
            print(message)
