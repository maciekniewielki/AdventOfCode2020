import re
import ast
import operator


def solve_1(data):
    return sum(evaluate(line) for line in data)


def find_top_tokens(s):
    t = []
    counter = 0
    for i, c in enumerate(s):
        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1
        elif c in "+*" and counter == 0:
            t.append((i, c))
    return t

def find_number_end(s):
    m = re.search(r'\d+', s)
    return m.end()

def find_matching_parenthesis(s):
    counter = 0
    for i, c in enumerate(s):
        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1
        if counter == 0:
            return i

def evaluate(expr):
    expr = expr.replace(" ", "")
    if expr.startswith("(") and find_matching_parenthesis(expr) == len(expr) - 1:
        return evaluate(expr[1:-1])

    if expr[0] in "0123456789":
        end = find_number_end(expr)
        num = int(expr[:end])
        if len(expr) == end:
            return num

    tokens = find_top_tokens(expr)
    value = evaluate(expr[:tokens[0][0]])
    values = [evaluate(expr[t1[0]+1:t2[0]]) for t1, t2 in zip([(-1, None)]+tokens, tokens+[(len(expr), None)])]
    operators = ["+"] + [t[1] for t in tokens]
    value = 0
    for v, op in zip(values, operators):
        if op == "+":
            value += v
        elif op == "*":
            value *= v
    return value


def solve_2(data):
    return sum(Calc.evaluate(swap_operators(line)) for line in data)

def swap_operators(line):
    return line.replace('+', '%temp%').replace('*', '+').replace('%temp%', '*')

_OP_MAP = {
    ast.Add: operator.mul,
    ast.Mult: operator.add,
}


class Calc(ast.NodeVisitor):

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return _OP_MAP[type(node.op)](left, right)

    def visit_Num(self, node):
        return node.n

    def visit_Expr(self, node):
        return self.visit(node.value)

    @classmethod
    def evaluate(cls, expression):
        tree = ast.parse(expression)
        calc = cls()
        return calc.visit(tree.body[0])


# IO
data = [line.rstrip() for line in open("input.txt").readlines()]

# 1st
print(solve_1(data))

# 2nd
print(solve_2(data))
