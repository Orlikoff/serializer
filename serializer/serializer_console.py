import argparse
from serializer.serializer_tools import Languages, Serializer


parser = argparse.ArgumentParser(
    description='Serializer for JSON, TOML, YAML formats')
parser.add_argument('filepath', type=str, help='Filepath for converting')
parser.add_argument('--format', type=str, help='Format for converting')
parser.add_argument('--new_filepath', type=str, help='Format for converting')
args = parser.parse_args()


filepath = args.filepath
format = args.format
new_filepath = args.new_filepath


if filepath.endswith('.osf'):
    with open(filepath, 'r') as file:
        filepath, format, new_filepath = file.readlines()
        filepath = filepath.strip('\n')
        format = format.strip('\n')
        new_filepath = new_filepath.strip('\n')

if not filepath.endswith('.'+format.lower()):
    serializer = None
    finalizer = None

    # Define the serializer type
    if filepath.endswith('.json'):
        serializer = Serializer(Languages.JSON)
    elif filepath.endswith('.toml'):
        serializer = Serializer(Languages.TOML)
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        serializer = Serializer(Languages.YAML)

    # Define the finalizer type
    if format in ('.json'):
        finalizer = Serializer(Languages.JSON)
    elif format in ('.toml'):
        finalizer = Serializer(Languages.TOML)
    elif format in ('.yaml'):
        finalizer = Serializer(Languages.YAML)

    obj = serializer.load(filepath)
    finalizer.dump(obj, new_filepath)
