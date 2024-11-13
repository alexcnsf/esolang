import lark
import pprint
import esolang.level2_loops

grammar = esolang.level2_loops.grammar + r"""
    %extend start: function_call
        | function_def

    function_def: "lambda" NAME ("," NAME)* ":" start

    ?args_list: start ("," start)*

    function_call: NAME "(" args_list? ")"
"""
parser = lark.Lark(grammar)


class Interpreter(esolang.level2_loops.Interpreter):
    '''
    >>> interpreter = Interpreter()
    >>> interpreter.visit(parser.parse("a=3; print(a)"))
    3
    >>> interpreter.visit(parser.parse("a=4; b=5; stack()"))
    [{'a': 4, 'b': 5}]
    >>> interpreter.visit(parser.parse("a=4; b=5; {c=6}; stack()"))
    [{'a': 4, 'b': 5}]
    >>> interpreter.visit(parser.parse("print(10)"))
    10
    >>> interpreter.visit(parser.parse("for i in range(10) {print(i)}"))
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    >>> interpreter.visit(parser.parse(r"f = lambda x : x; f(5)"))
    5
    >>> interpreter.visit(parser.parse(r"f = lambda x,y : x+y; f(5, 6)"))
    11
    >>> interpreter.visit(parser.parse(r"f = lambda x,y,z : x+y-z; f(5, 6, 7)"))
    4
    >>> interpreter.visit(parser.parse(r"f = lambda x,y,z : {print(x); print(y); print(z); {z = 10; print(z);}; print(z);}; f(5, 6, 7)"))
    5
    6
    7
    10
    7
    '''
    def __init__(self):
        super().__init__()
        # Built-in functions are stored in the first frame
        self.stack.append({})
        self.stack[0]['print'] = print
        self.stack[0]['stack'] = lambda: pprint.pprint(self.stack[1:])

    def function_def(self, tree):
        names = [token.value for token in tree.children[:-1]]
        body = tree.children[-1]

        def foo(*args):
            self.stack.append({})
            for name, arg in zip(names, args):
                self._assign_to_stack(name, arg)
            ret = self.visit(body)
            self.stack.pop()
            return ret

        return foo

    def function_call(self, tree):
        name = tree.children[0].value
        args = [self.visit(arg) for arg in tree.children[1:]] if len(tree.children) > 1 else []
        return self._get_from_stack(name)(*args)

