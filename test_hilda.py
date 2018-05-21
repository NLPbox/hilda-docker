#!/usr/bin/env python2
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

EXPECTED_PARSETREE = """ParseTree('Contrast[S][N]', ["Although they did n't like it ,", 'they accepted the offer .'])"""

EXPECTED_RS3 = """<?xml version='1.0' encoding='UTF-8'?>
<rst>
  <header>
    <relations>
      <rel name="Contrast" type="rst"/>
    </relations>
  </header>
  <body>
    <segment id="3" parent="5" relname="Contrast">Although they did n't like it ,</segment>
    <segment id="5" parent="1" relname="span">they accepted the offer .</segment>
    <group id="1" type="span"/>
  </body>
</rst>
"""

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

    with open('input_short.txt.parsetree') as edu_file:
        parsetree_str = edu_file.read()
        assert parsetree_str == EXPECTED_PARSETREE, result.stderr.encode('utf-8')

    converter = sh.Command('./hilda2rs3.sh')
    result = converter('input_short.txt.parsetree')
    
    with open('input_short.txt.parsetree.rs3') as rs3_file:
        rs3_str = rs3_file.read()
        assert rs3_str == EXPECTED_RS3, result.stderr.encode('utf-8')
