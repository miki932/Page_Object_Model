from os import environ
import sys

try:
    environ.get("SAUCE_USERNAME")
except KeyError:
    print("ERROR: SAUCE_USERNAME environment variable required !")
    sys.exit(1)

try:
    environ.get("SAUCE_ACCESS_KEY")
except KeyError:
    print("ERROR: SAUCE_ACCESS_KEY environment variable required !")
    sys.exit(1)
