import yaml
import re
from os.path import expanduser
from src.utils.logger import Logger

# Perform any processing to a filepath to make
# sure that it is valid.
# @param filepath Raw filepath to process
# @return Processed filepath string
def process_filepath(filepath):
    # If the file is absolute, expand the path
    filepath = re.sub('~', expanduser('~'), filepath)
    return filepath

# @class YAML
# @desc Simple class that makes interacting with YAML files
# simple and easy with a few functions. All methods are static.
class YAML:
    # Parses raw YAML into a Python object.
    # @param raw String of raw YAML syntax
    # @return Python object with the given YAML data
    @staticmethod
    def parse_yaml(raw):
        return yaml.load(raw)

    # Loads a YAML file into a Python object.
    # @param filepath Filepath to the YAML file to load
    # @return Python object with the given YAML data
    @staticmethod
    def load(filepath):
        Logger.debug('Loading file \'' + filepath + '\'')
        return yaml.load(open(process_filepath(filepath), 'r'))

    # Writes a YAML file with a given Python object. The
    # written file will be truncated, not appended.
    # @param filepath Filepath to the YAML file to write to
    # @param data Python object with data to write
    @staticmethod
    def write(filepath, data):
        Logger.debug('Writing file \'' + filepath + '\'')
        yaml.dump(data, open(process_filepath(filepath), 'w'))
