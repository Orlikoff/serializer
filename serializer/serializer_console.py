# import argparse
import sys
from serializer import Languages, Serializer


# parser = argparse.ArgumentParser(
#     description='Serializer for JSON, TOML, YAML formats')
# parser.add_argument('filepath', type=str, help='Filepath for converting')
# parser.add_argument('format', type=str, help='Format for converting')
# parser.add_argument('new_filepath', type=str, help='Format for converting')
# args = parser.parse_args()
if len(sys.argv) < 4:
    print('Usage: <filepath to change> <format> <new filepath>')
    exit(1)

filepath = sys.argv[1]
format = sys.argv[2]
new_filepath = sys.argv[3]


if not filepath.ends_with('.'+format.lower()):
    deserializer = None
    finalizer = None

    # Define the serializer type
    if filepath.ends_with('.json'):
        serializer = Serializer(Languages.JSON)
    elif filepath.ends_with('.toml'):
        serializer = Serializer(Languages.TOML)
    elif filepath.ends_with('.yaml') or filepath.ends_with('.yml'):
        serializer = Serializer(Languages.YAML)

    # Define the finalizer type
    if format.ends_with('.json'):
        finalizer = Serializer(Languages.JSON)
    elif format.ends_with('.toml'):
        finalizer = Serializer(Languages.TOML)
    elif format.ends_with('.yaml'):
        finalizer = Serializer(Languages.YAML)

    data = deserializer.load(filepath)
    finalizer.dump(new_filepath)
