import re
from operator import add, mul
with open("input.txt") as f:
    lines = f.readlines()

def find_parens(tokens):
    toret = {}
    pstack = []
    for i, c in enumerate(tokens):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            toret[pstack.pop()] = i
    return toret

def do_op(tokens, op):
    while True:
        try:
            leftmost_op = tokens.index(op)
            a = tokens[leftmost_op - 1]
            b = tokens[leftmost_op + 1]
            tokens[leftmost_op - 1] = str(eval(a + op + b))
            tokens.pop(leftmost_op)
            tokens.pop(leftmost_op)
        except ValueError:
            break
    return tokens

def eval_exp(tokens):
    parens = find_parens(tokens)
    while True:
        if len(parens.keys()) == 0:
            break
        last_paren = max(parens)
        closing_paren = parens[last_paren]
        tokens = tokens[0:last_paren] + [eval_exp(tokens[last_paren + 1 :closing_paren])] + tokens[closing_paren + 1:]
        parens = find_parens(tokens)
    result = int(tokens[0])
    tokens = do_op(tokens, "+")
    tokens = do_op(tokens, "*")
    return tokens[0]

def eval_line(exp):
    tokens = [e for e in re.findall(r"(\(|\)|\d+|\*|\+|\s)", exp.strip()) if e != ' ']
    return int(eval_exp(tokens))

results = []
for line in lines:
    results.append(eval_line(line))

print(sum(results))


