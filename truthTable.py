import itertools

numOfVars = 3


def build_table(n):
    table = list(itertools.product([False, True], repeat=n))
    return table

print(build_table(numOfVars))
