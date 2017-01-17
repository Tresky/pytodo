import yaml
from os.path import expanduser

def fix_filepath(filepath):
    # If the file is absolute, expand the path
    if filepath[0] == '~':
        filepath = expanduser('~') + filepath[1:]
    return filepath

class YAML:
    @staticmethod
    def parse_yaml(raw):
        return yaml.load(raw)

    @staticmethod
    def load(filepath):
        print('Loading file \'' + filepath + '\'')
        return yaml.load(open(fix_filepath(filepath), 'r'))

    @staticmethod
    def write(filepath, data):
        print('Writing file \'' + filepath + '\'', data)
        yaml.dump(data, open(fix_filepath(filepath), 'w'))
