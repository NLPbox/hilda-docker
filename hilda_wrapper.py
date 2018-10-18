#!/usr/bin/env python2

"""
Simple wrapper around the original hilda.py (Hernault et al. 2010) that
outputs parse tree in a string format that can easily be parsed into
nltk.tree.ParentedTree objects.

Original output:

(Contrast[S][N]
  Although they did n't like it ,
  they accepted the offer .)

What we actually want:

ParseTree('Contrast[S][N]', ["Although they did n't like it ,", 'they accepted the offer .'])
"""

import sys
import tempfile

from hilda import main
import nltk


SENT_DETECTOR = nltk.data.load('tokenizers/punkt/english.pickle')


def parse_file(input_filepath):
    """Takes plain text input, splits it into sentences, marks them in
    HILDA's input format, calls HILDA on the preprocessed input and returns
    a string representation of the parse tree.
    """
    with open(input_filepath) as input_file:
        input_text = input_file.read()

    with tempfile.NamedTemporaryFile() as tokenized_input_file:
        for sent in SENT_DETECTOR.tokenize(input_text):
            tokenized_input_file.write(u"{0}<s>\n".format(sent.rstrip()))
        tokenized_input_file.flush()

        # sys.argv[1] is where the original hilda.py expects the input file
        sys.argv = ['hilda.py', tokenized_input_file.name]
        parse_tree = main()

    return parse_tree.__repr__()


if __name__ == "__main__":
    INPUT = sys.argv[-1]
    OUTPUT = parse_file(INPUT)
    sys.stdout.write(OUTPUT)
    sys.stdout.write("\n")
