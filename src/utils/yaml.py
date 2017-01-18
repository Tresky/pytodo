import yaml
import re
from os.path import expanduser
from src.utils.logger import Logger

def process_filepath(filepath):
    # If the file is absolute, expand the path
    filepath = re.sub('~', expanduser('~'), filepath)
    return filepath

class YAML:
    @staticmethod
    def parse_yaml(raw):
        return yaml.load(raw)

    @staticmethod
    def load(filepath):
        Logger.debug('Loading file \'' + filepath + '\'')
        return yaml.load(open(process_filepath(filepath), 'r'))

    @staticmethod
    def write(filepath, data):
        Logger.debug('Writing file \'' + filepath + '\'')
        yaml.dump(data, open(process_filepath(filepath), 'w'))
