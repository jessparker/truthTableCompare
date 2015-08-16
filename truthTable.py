import itertools

numOfVars = 3


def create_truth_tables(n):
    """
    :param n: Number of arguments to create columns for.
    :return: Table containing columns for each argument.
    """
    table = list(itertools.product([False, True], repeat=n))
    return table


def create_and(column1, column2):
    """
    :param column1: First column to be compared.
    :param column2: Second column to be compared.
    :return: New column based on an AND compare of the two columns.
    """
    new_column = []
    for a, b in zip(column1, column2):
        if a and b:
            new_column.append(True)
        else:
            new_column.append(False)
    return new_column


def create_or(column1, column2):
    """
    :param column1: First column to be compared.
    :param column2: Second column to be compared.
    :return: New column based on an OR compare of the two columns.
    """
    new_column = []
    for a, b in zip(column1, column2):
        if a or b:
            new_column.append(True)
        else:
            new_column.append(False)
    return new_column


def create_not(column1):
    """
    :param column1: Column to be negated (NOT)
    :return: New column that is the opposite of the original column.
    """
    new_column = []
    for a in column1:
        if a:
            new_column.append(False)
        else:
            new_column.append(True)
    return new_column


def are_columns_equal(column1, column2):
    """
    :param column1: First column to be compared.
    :param column2: Second column to be compared.
    :return: True if the columns are equal, False if they are not.
    """
    """ Compare two columns to determine equality. """
    for a, b in zip(column1, column2):
        if a != b:
            return False
        else:
            return True

truthTable = create_truth_tables(numOfVars)

P = [row[0] for row in truthTable]
Q = [row[1] for row in truthTable]
R = P

print(are_columns_equal(P, R))
print(create_and(P, Q))
print(create_or(P, Q))
print(create_not(P))




