# esolang ![](https://github.com/alexcnsf/esolang/workflows/tests/badge.svg)

A simple esolang for experimenting with different syntax and semantics of programming languages.

Here is an example output of running all the level1 doctests!

```
$ python3 -m doctest --verbose esolang/level1_statements.py
Trying:
    interpreter = Interpreter()
Expecting nothing
ok
Trying:
    interpreter.visit(parser.parse("a = 2"))
Expecting:
    2
ok
Trying:
    interpreter.visit(parser.parse("a + 2"))
Expecting:
    4
ok
Trying:
    interpreter.visit(parser.parse("a = a + 3"))
Expecting:
    5
ok
Trying:
    interpreter.visit(parser.parse("b = 3"))
Expecting:
    3
ok
Trying:
    interpreter.visit(parser.parse("a * b"))
Expecting:
    15
ok
Trying:
    interpreter.visit(parser.parse("a = 3; {a+5}"))
Expecting:
    8
ok
Trying:
    interpreter.visit(parser.parse("a = 3; {a=5; a+5}"))
Expecting:
    10
ok
Trying:
    interpreter.visit(parser.parse("a = 3; {a=5}; a+5"))
Expecting:
    10
ok
Trying:
    interpreter.visit(parser.parse("a = 3; {c=5}; c+5")) # doctest: +IGNORE_EXCEPTION_DETAIL
Expecting:
    Traceback (most recent call last):
        ...
    ValueError: Variable c undefined
ok
Trying:
    interpreter.visit(parser.parse("if (0): { 10 } else 5"))  
Expecting:
    5
ok
Trying:
    interpreter.visit(parser.parse("if (1): { 10 } else 5"))  
Expecting:
    5
ok
Trying:
    interpreter.visit(parser.parse("a = 10; if (a): { 10 } else 0"))
Expecting:
    0
ok
Trying:
    interpreter.visit(parser.parse("a = 1; if (a): { 10 } else 100"))
Expecting:
    100
ok
Trying:
    interpreter.visit(parser.parse("a=2; b=1; if (a-b): { 5 } else 1"))
Expecting:
    1
ok
Trying:
    interpreter.visit(parser.parse("x = 2; { x = x + 3; x + 5 }"))
Expecting:
    10
ok
8 items had no tests:
    level1_statements
    level1_statements.Interpreter.__init__
    level1_statements.Interpreter._assign_to_stack
    level1_statements.Interpreter._get_from_stack
    level1_statements.Interpreter.access_var
    level1_statements.Interpreter.assign_var
    level1_statements.Interpreter.block
    level1_statements.Interpreter.if_statement
1 items passed all tests:
  16 tests in level1_statements.Interpreter
16 tests in 9 items.
16 passed and 0 failed.
Test passed.
```

You can view my code passing all levels of doctest on recent successful runs in the actions tabs of the repository!
