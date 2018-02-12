#!/bin/bash
python hilda.py $1 > $1.hilda
cat $1.hilda
