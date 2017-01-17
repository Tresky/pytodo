import yaml
from os.path import expanduser

class YAML:
    @staticmethod
    def load(filepath):
        print('Loading file \'' + filepath + '\'')

        # If the file is absolute, expand the path
        if filepath[0] == '~':
            filepath = expanduser('~') + filepath[1:]
        return yaml.load(open(filepath, 'r'))
