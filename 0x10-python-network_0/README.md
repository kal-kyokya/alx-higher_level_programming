# REQUIREMENTS

## GENERAL

	->	Allowed editors:
			vi, vim, emacs
	->	A README.md file, at the root of the folder of the project, is mandatory
	->	All scripts will be tested on:
			Ubuntu 20.04 LTS
	->	All Bash scripts should be exactly 3 lines long:
			wc -l file
				should print 3
	->	All files should end with a new line
	->	All files must be executable
	->	The first line of all bash files should be exactly:
			#!/bin/bash
	->	The second line of all Bash scripts should be:
			<A comment explaining what is the script doing>
	->	All curl commands must have the option:
			-s (silent mode)
	->	All files will be interpreted/compiled on:
			Ubuntu 20.04 LTS
				using:
					python3 (version 3.8.5)
	->	The first line of all Python files should be exactly:
			#!/usr/bin/python3
	->	Code should use:
			pycodestyle (version 2.8.*)
	->	All modules should be documented:
			python3 -c 'print(__import__("Mymodule").__doc__)'
	->	All classes should be documented:
			python3 -c 'print(__import__("Mymodule").MyClass.__doc__)'
	->	All functions (inside and outside a class) should be documented:
			python3 -c 'print(__import__("Mymodule").Myfunction.__doc__)'
			python3 -c 'print(__import__("Mymodule").MyClass.Myfunction.__doc__)'
	->	A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method
