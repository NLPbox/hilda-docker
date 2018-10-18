#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author: Arne Neumann <nlpbox.programming@arne.cl>

"""
Tests for the HILDA RST parser and our preprocessor/wrapper
hilda_wrapper.py.
"""

import pytest

from hilda_wrapper import parse_file

EXPECTED_PARSETREE_SHORT = """ParseTree('Contrast[S][N]', ["Although they did n't like it ,", 'they accepted the offer .'])"""
EXPECTED_PARSETREE_LONG = """ParseTree('Joint[N][N]', [ParseTree('Joint[N][N]', ['Henryk Szeryng ( 22 September 1918 - 8 March 1988 )', ParseTree('Joint[N][N]', ['was a violin virtuoso of Polish and Jewish heritage .', ParseTree('Joint[N][N]', ['He was born in Zelazowa Wola , Poland .', ParseTree('Joint[N][N]', [ParseTree('Background[N][S]', ['Henryk started piano and harmony training with his mother', 'when he was 5 ,']), 'and at age 7 turned to the violin ,'])])])]), ParseTree('Joint[N][N]', [ParseTree('Elaboration[N][S]', [ParseTree('Background[N][S]', ['receiving instruction from Maurice Frenkel .', ParseTree('Elaboration[N][S]', [ParseTree('Elaboration[N][S]', [ParseTree('Attribution[N][S]', [ParseTree('Elaboration[N][S]', ['After studies with Carl Flesch in Berlin', '( 1929-32 ) ,']), 'he went to Paris to continue his training with Jacques Thibaud at the Conservatory ,']), 'graduating with a premier prix in 1937 .']), ParseTree('Elaboration[N][S]', [ParseTree('Elaboration[N][S]', ['He made his solo debut in 1933', 'playing the Brahms Violin Concerto .']), ParseTree('Joint[N][N]', ['From 1933 to 1939 he studied composition in Paris with Nadia Boulanger ,', ParseTree('same-unit[N][N]', [ParseTree('Elaboration[N][S]', ['and during World War II he worked as an interpreter for the Polish government in exile', '( Szeryng was fluent in seven languages )']), 'and gave concerts for Allied troops all over the world .'])])])])]), ParseTree('Elaboration[N][S]', ['During one of these concerts in Mexico City he received an offer to take over the string department of the university there .', 'In 1946 ,'])]), ParseTree('Joint[N][N]', [ParseTree('Elaboration[N][S]', ['he became a naturalized citizen of Mexico .', ParseTree('Elaboration[N][S]', ['Szeryng subsequently focused on teaching before resuming his concert career in 1954 .', 'His debut in New York City brought him great acclaim ,'])]), ParseTree('Elaboration[N][S]', ['and he toured widely for the rest of his life .', ParseTree('Attribution[S][N]', ['He died', ParseTree('Elaboration[N][S]', [ParseTree('Elaboration[N][S]', ['in Kassel .', ParseTree('Elaboration[N][S]', [ParseTree('Elaboration[N][S]', ['Szeryng made a number of recordings ,', 'including two of the complete sonatas and partitas for violin by Johann Sebastian Bach , and several of sonatas of Beethoven and Brahms with the pianist Arthur Rubinstein .']), 'He also composed ;'])]), ParseTree('Elaboration[N][S]', ['his works include a number of violin concertos and pieces of chamber music .', ParseTree('Elaboration[N][S]', [ParseTree('Elaboration[N][S]', ["He owned the Del Gesu `` Le Duc '' , the Stradivarius `` King David '' as well as the Messiah Strad copy by Jean-Baptiste Vuillaume", 'which he gave to Prince Rainier III of Monaco .']), ParseTree('Elaboration[N][S]', [ParseTree('Temporal[N][S]', [ParseTree('Elaboration[N][S]', ["The `` Le Duc '' was the instrument", 'on which he performed and recorded mostly ,']), ParseTree('same-unit[N][N]', [ParseTree('Elaboration[N][S]', ['while the latter', "( `` King David ''"]), 'Strad )'])]), 'was donated to the State of Israel .'])])])])])])])])])"""


def test_hilda():
    """The HILDA parser produces the expected output."""
    result = parse_file('input_short.txt')
    assert result == EXPECTED_PARSETREE_SHORT

    result = parse_file('input_long.txt')
    assert result == EXPECTED_PARSETREE_LONG

    with pytest.raises(Exception) as excinfo:
        result = parse_file('input_broken.txt')
        assert "Syntactic parsing of the following sentence failed" in excinfo.value.message
