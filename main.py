import argparse

from lib.systemspecific import SystemSpecific

# init
parser = argparse.ArgumentParser(description="analyze the narou")
parser.add_argument("-r", "--reload", help="Updating novel data")
parser.add_argument("-f", "--function", help="choice a function")

# parse
args = parser.parse_args()

reload = False
if args.reload != None:
    reload = True

ss = SystemSpecific(reload)

if args.function == 'keyword' or args.function == 'k':
    ss.keyword()

elif args.function == 'similarity' or args.function == 's':
    ss.similarity()
