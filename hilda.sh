#!/bin/sh
python hilda_wrapper.py -o $1
cat $1.edus
cat $1.tree
echo # add newline to output
