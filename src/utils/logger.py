from src.utils.environment import Env

class Logger:
    @staticmethod
    def debug(message):
        if Env.get('DEBUG'):
            print(message)
