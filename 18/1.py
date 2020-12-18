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
    for tok in tokens[1:]:
        if tok == "+":
            op = add
        elif tok == "*":
            op = mul
        else:
            result = op(result, int(tok))

    return str(result)

def eval_line(exp):
    tokens = [e for e in re.findall(r"(\(|\)|\d+|\*|\+|\s)", exp.strip()) if e != ' ']
    return int(eval_exp(tokens))

results = []
for line in lines:
    results.append(eval_line(line))

print(sum(results))
