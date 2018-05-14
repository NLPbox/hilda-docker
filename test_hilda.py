#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arne Neumann <nlpbox.programming@arne.cl>

import sh
import sys
import pytest

EXPECTED_EDUS = """<edu>Although they did n't like it ,</edu>
<edu>they accepted the offer .</edu>
"""
EXPECTED_TREE = """(Contrast[S][N]
  Although they did n't like it ,
  they accepted the offer .)"""

def test_hilda():
    """The HILDA parser produces the expected output."""
    parser = sh.Command('./hilda.sh')
    result = parser('input_short.txt')
    
    with open('input_short.txt.edus') as edu_file:
        edu_str = edu_file.read()
        assert edu_str == EXPECTED_EDUS, result.stderr.encode('utf-8')

    with open('input_short.txt.tree') as edu_file:
        tree_str = edu_file.read()
        assert tree_str == EXPECTED_TREE, result.stderr.encode('utf-8')
