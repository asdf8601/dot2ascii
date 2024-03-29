#!python3
"""
Examples
--------
$ pipx run https://gist.githubusercontent.com/mmngreco/2d3bc321405b1991277fd6001060df0d/raw/dot2ascii.py help
$ pipx run https://gist.githubusercontent.com/mmngreco/2d3bc321405b1991277fd6001060df0d/raw/dot2ascii.py "graph {a -- b -- c}"
$ echo "graph {rankdir=LR; a -- b -- c }" | pipx run https://gist.githubusercontent.com/mmngreco/2d3bc321405b1991277fd6001060df0d/raw/dot2ascii.py
"""
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "requests",
# ]
# ///

import requests

def dot_to_ascii(dot: str, fancy: bool = True):
    url = 'https://dot-to-ascii.ggerganov.com/dot-to-ascii.php'
    boxart = 0
    if fancy:
        # use nice box drawing char instead of + , | , -
        boxart = 1
    params = {
        'boxart': boxart,
        'src': dot,
    }
    response = requests.get(url, params=params).text
    if response == '':
        raise SyntaxError('DOT string is not formatted correctly')
    return response


def app():
    import sys
    if len(sys.argv) > 1:
        text = sys.argv[1]
        if text == "help":
            print("Usage: python main.py [dot_string]")
            sys.exit(0)
    else:
        text = sys.stdin.read()
    ascii = dot_to_ascii(text)
    print(ascii)


if __name__ == '__main__':
    app()
