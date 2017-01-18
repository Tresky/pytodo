import os

class Env:
    @staticmethod
    def get(var):
        if var in os.environ:
            return os.environ[var]
        return None
