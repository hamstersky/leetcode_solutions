def equationsPossible(equations) -> bool:
    variables = []
    for equation in equations:
        variables.append(equation[0])
        variables.append(equation[3])
    variables = list(set(variables))


arr = [0, 1, 2]
# res = []
# for x in arr:
#     subres = []
#     for y in arr:


equationsPossible(["a==b", "b!=a"])
