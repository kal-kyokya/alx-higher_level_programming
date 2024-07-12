#!/usr/bin/bash
# Uses 'Stream Editor' to extract thr value associated with a key

# Usage: ./sed_test_file <KEY> <TEST_FILE>
"""
	Note that the flag:
	->	-n, --quiet, --silent
			suppress automatic printing of pattern space

	->	's/regexp/replacement/'
			Attempt to match regexp against the pattern space.
			If successful, replace that portion matched with  replacement.

	->	In this particular use case:
			'/p': Print the current pattern space.
"""

sed -n 's/^'$1'=//p' $2
