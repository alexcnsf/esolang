import lark
import esolang.level1_statements

grammar = esolang.level1_statements.grammar + r"""
    %extend start: forloop | whileloop

    forloop: "for" NAME "in" range block
    whileloop: "while" while_condition block
    range: "range" "(" start ")"
    while_condition: start comparison_operator start

    comparison_operator: ">" | "<" | ">=" | "<=" | "==" | "!="
"""
parser = lark.Lark(grammar)


class Interpreter(esolang.level1_statements.Interpreter):
    '''
    >>> interpreter = Interpreter()
    >>> interpreter.visit(parser.parse("for i in range(10) {i}"))
    9
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}"))
    45
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}; a"))
    45
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}; i")) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValueError: Variable i undefined
    >>> interpreter.visit(parser.parse("a=5; for i in range(a) {a = a + i}; a"))
    15
    >>> interpreter.visit(parser.parse("a=0; while a < 10 {a = a + 1}"))
    10
    >>> interpreter.visit(parser.parse("a=0; while a < 5 {a = a + 1}; a"))
    5
    '''
    def range(self, tree):
        return range(int(self.visit(tree.children[0])))

    def forloop(self, tree):
        varname = tree.children[0].value
        xs = self.visit(tree.children[1])
        self.stack.append({})
        result = None
        for x in xs:
            self.stack[-1][varname] = x
            result = self.visit(tree.children[2])
        self.stack.pop()
        return result

    def whileloop(self, tree):
        while self.evaluate_condition(tree.children[0]):
            self.visit(tree.children[1])

    def evaluate_condition(self, tree):
        left = self.visit(tree.children[0])
        op = tree.children[1].value
        right = self.visit(tree.children[2])
        return {
            ">": left > right,
            "<": left < right,
            ">=": left >= right,
            "<=": left <= right,
            "==": left == right,
            "!=": left != right
        }[op]

