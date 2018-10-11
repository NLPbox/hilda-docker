#!/bin/sh
python hilda_wrapper.py -o $1
cat $1.edus $1.tree > $1.hilda
cat $1.hilda
echo # add newline to output
