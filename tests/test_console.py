#!/usr/bin/python3

""" unittests for 'console.py', all features """

with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
