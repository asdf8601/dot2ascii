#!python3
"""
Examples
--------
>>> pipx run main.py help
... text = '''
... graph {
...     rankdir=LR
...     A [label="Christmas"]
...     B [label="Go shopping"]
...     C [label="Let me think"]
...     D [label="Laptop"]
...     E [label="iPhone"]
...     F [label="Car"]
...     A -> B [label="Get money"]
...     B -> C
...     C -> D [label="One"]
...     C -> E [label="Two"]
...     C -> F [label="Three"]
... }
... '''

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


if __name__ == '__main__':
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
