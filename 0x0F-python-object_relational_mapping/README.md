# PYTHON - OBJECT-RELATIONAL MAPPING

This directory is home to all files required for completion of the '0x0F-python-object_relational_mapping' project by ALX-Africa to its Software Engineering program.

## REQUIREMENTS

```GENERAL```

	->	Allowed editors:
			vi, vim, emacs
	->	All files will be interpreted/compiled on:
			Ubuntu 20.04 LTS,
				using:
					python3 (version 3.8.5)
	->	Files will be executed with:
			MySQLdb version 2.0.x
			SQLAlchemy version 1.4.x
	->	All files should end with a new line
	->	The first line of all files should be exactly:
			#!/usr/bin/python3
	->	A README.md file, at the root of the folder of the project, is mandatory
	->	Code should use:
			pycodestyle (version 2.8.*)
	->	All files must be executable
	->	The length of files will be tested using:
			wc
	->	All modules should have a documentation:
			python3 -c 'print(__import__("my_module").__doc__)'
	->	All classes should have a documentation:
			python3 -c 'print(__import__("my_module").MyClass.__doc__)'
	->	All functions (inside and outside a class) should have a documentation:
			python3 -c 'print(__import__("my_module").my_function.__doc__)'
			python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
	->	A documentation is not a simple word: a real sentence explaining what’s the purpose of the module, class or method
	->	It is not allowed to use:
			execute with sqlalchemy

## MORE INFO

```Install and activate venv```

To create a Python Virtual Environment, allowing to install specific dependencies for this python project, we will install venv:
	$ sudo apt-get install python3.8-venv
	$ python3 -m venv venv
	$ source venv/bin/activate

```Install MySQLdb module version 2.0.x```

For installing MySQLdb, MySQL must have been installed:
	$ sudo apt-get install python3-dev
	$ sudo apt-get install libmysqlclient-dev
	$ sudo apt-get install zlib1g-dev
	$ sudo pip3 install mysqlclient
	...
	$ python3
	>>> import MySQLdb
	>>> MySQLdb.version_info 
	(2, 0, 3, 'final', 0)

```Install SQLAlchemy module version 1.4.x```

	$ sudo pip3 install SQLAlchemy
	...
	$ python3
	>>> import sqlalchemy
	>>> sqlalchemy.__version__ 
	'1.4.22'
Also, for the warning message:

	/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")
	cursor.execute(statement, parameters)

One can ignore it.