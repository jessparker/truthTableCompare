import itertools

numOfVars = 2


def build_truth_table(n):
    table = list(itertools.product([False, True], repeat=n))
    return table


def compare_tables(table1, table2):
    for a, b in zip(table1, table2):
        if a != b:
            return False
        else:
            return True

truthTable = build_truth_table(numOfVars)

P = [row[0] for row in truthTable]
Q = [row[1] for row in truthTable]
R = P

print(compare_tables(P, R))


"""
print("P or Q = ")
print(P)
print(Q)
print("---")
print(P or Q)

print("------")
if P[1] or Q[1]:
    print(True)
else:
    print(False)
print("------")

for element in P:
    print("\nP[row] =")
    print(P[element])
    print("Q[row] =")
    print(Q[element])
    print("P[row] or Q[row] =")
    if P[element] or Q[element]:
        print(True)
    else:
        print(False)

# i = 0
# while i < numOfVars:
#     print("\nColumn " + str(i))
#     for row in truthTable:
#         print(row[i])
#     i += 1
"""




