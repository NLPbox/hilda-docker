#!/usr/bin/env python2

import codecs
import sys

from hilda import main

"""
Simple wrapper around The original hilda.py (Hernault et al. 2010) that
outputs parse tree in a string format that can easily be parsed into
nltk.tree.ParentedTree objects.
"""

if __name__ == "__main__":
    parse_tree = main()
    input_filename = sys.argv[-1]
    with codecs.open('{}.parsetree'.format(input_filename), 'w', 'utf-8') as outfile:
        outfile.write(parse_tree.__repr__())
