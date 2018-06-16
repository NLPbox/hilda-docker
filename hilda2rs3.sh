#!/bin/bash

source ~/.profile
workon discoursegraphs
python hilda2rs3.py $1 $1.rs3
deactivate
