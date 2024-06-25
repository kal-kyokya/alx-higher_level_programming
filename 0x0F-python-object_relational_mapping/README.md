# PYTHON - OBJECT-RELATIONAL MAPPING

This directory is home to all files required for completion of the '0x0F-python-object_relational_mapping' project by ALX-Africa to its Software Engineering program.

## Background Context

In this project, we will link two amazing worlds: ```Databases and Python!```

In the first part, we will use the module ```MySQLdb``` to connect to a MySQL database and execute wer SQL queries.

In the second, we will use the module ```SQLAlchemy``` an Object-Relational Mapper (ORM).

The biggest difference is: ```no more SQL queries!```
Indeed, the purpose of an ORM is to abstract the storage to the usage.
With an ORM, the biggest concern will be “What can one do with my objects” and not “How this object is stored? where? when?”.
We won’t write any SQL queries only Python code.

Last thing, code won’t be “storage type” dependent. We will be able to change storage easily without re-writing the entire project.

```Without ORM:```

	conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
	cur = conn.cursor()
	cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
	query_rows = cur.fetchall()
	for row in query_rows:
	    print(row)
	cur.close()
	conn.close()

```With an ORM:```

	engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
	Base.metadata.create_all(engine)

	session = Session(engine)
	for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
	    print("{}: {}".format(state.id, state.name))
	session.close()

Do we see the difference? Cool, right?

The biggest difficulty with ORM is: ```The syntax!```

Indeed, all of them have the same type of syntax, but not always.
Please read/watch many tutorials and don’t try to read the entire related documentation before starting, just refer to them if you don’t get something.

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