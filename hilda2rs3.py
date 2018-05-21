#!/usr/bin/env python2

import argparse
import sys
import discoursegraphs as dg


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help="HILDA file to be converted")
    parser.add_argument('output_file', help="path to .rs3 output file.")
    args = parser.parse_args(sys.argv[1:])
    
    hilda_tree = dg.read_hilda(args.input_file)
    dg.write_rs3(hilda_tree, args.output_file)
