#!/bin/bash
python hilda.py -o $1
cat $1.edus
cat $1.tree
