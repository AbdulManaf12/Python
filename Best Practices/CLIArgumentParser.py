# Import the library
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
args = parser.parse_args()
print('Hello,', args.name)

# $ python .\CLIArgumentParser.py --name MANAF
#  Hello, MANAF