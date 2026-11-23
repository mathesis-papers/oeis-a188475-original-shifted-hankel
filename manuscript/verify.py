import json
from itertools import combinations
from math import comb


def determinant(matrix):
    size = len(matrix)
    if size == 0:
        return 1
    entries = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        nonzero = next((row for row in range(pivot_index, size)
                        if entries[row][pivot_index]), None)
        if nonzero is None:
            return 0
        if nonzero != pivot_index:
            entries[pivot_index], entries[nonzero] = entries[nonzero], entries[pivot_index]
            sign *= -1
        pivot = entries[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (entries[row][column] * pivot
                             - entries[row][pivot_index] * entries[pivot_index][column])
                assert numerator % previous == 0
                entries[row][column] = numerator // previous
            entries[row][pivot_index] = 0
        previous = pivot
    return sign * entries[-1][-1]


def source_sequence(maximum):
    catalan = [comb(2 * index, index) // (index + 1) for index in range(maximum + 1)]
    sequence = [0, 0, 1, 2]
    for index in range(4, maximum + 1):
        sequence.append(2 * sequence[index - 1] + 2 * sequence[index - 2]
                        + sum(catalan[term] * sequence[index - term - 1]
                              for term in range(1, index - 2)))
    return sequence


def jacobi_moments(maximum):
    vector = [1] + [0] * (maximum + 1)
    moments = []
    for degree in range(maximum + 1):
        moments.append(vector[0])
        updated = [0] * len(vector)
        for index in range(degree + 1):
            updated[index + 1] += vector[index]
            if index:
                updated[index] += 2 * vector[index]
                updated[index - 1] += (2 if index == 1 else 1) * vector[index]
        vector = updated
    return moments


def polynomials(maximum):
    family = [[1], [0, 1]]
    for degree in range(1, maximum):
        current = family[degree]
        prior = family[degree - 1]
        following = [0] * (degree + 2)
        for index, coefficient in enumerate(current):
            following[index + 1] += coefficient
            following[index] -= 2 * coefficient
        for index, coefficient in enumerate(prior):
            following[index] -= (2 if degree == 1 else 1) * coefficient
        family.append(following)
    return family


def parameter_sequence(maximum, parameter):
    catalan = [comb(2 * index, index) // (index + 1) for index in range(maximum + 1)]
    sequence = [0] * (maximum + 1)
    for degree in range(2, maximum + 1):
        sequence[degree] = catalan[degree - 1] + parameter * sum(
            catalan[index - 1] * sequence[degree - index]
            for index in range(2, degree + 1))
    return sequence


def combinatorial_counts(semilength):
    path_count = 0
    partition_count = 0
    for remaining in combinations(range(1, 2 * semilength), semilength - 1):
        first = (0,) + remaining
        first_set = set(first)
        second = tuple(index for index in range(2 * semilength) if index not in first_set)
        steps = [1 if index in first_set else -1 for index in range(2 * semilength)]
        height = 0
        allowed = True
        for index, step in enumerate(steps):
            if index + 1 < len(steps) and height == 0 and step == -steps[index + 1]:
                allowed = False
            height += step
        path_count += allowed
        nonexchangeable = True
        for index in range(semilength):
            changed_first, changed_second = list(first), list(second)
            changed_first[index], changed_second[index] = changed_second[index], changed_first[index]
            first_ordered = all(left < right for left, right in zip(changed_first, changed_first[1:]))
            second_ordered = all(left < right for left, right in zip(changed_second, changed_second[1:]))
            if first_ordered and second_ordered:
                nonexchangeable = False
                break
        assert allowed == nonexchangeable
        partition_count += nonexchangeable
    return path_count, partition_count


def main():
    if not __debug__:
        raise RuntimeError('Run the checker without Python optimization flags.')
    maximum = 52
    sequence = source_sequence(maximum)
    moments = jacobi_moments(maximum)
    assert moments == [1] + [2 * value for value in sequence[1:]]
    assert sequence[1:16] == [0, 1, 2, 7, 22, 74, 252, 875, 3078, 10950,
                              39316, 142278, 518364, 1899668, 6997688]
    assert determinant([]) == 1
    assert determinant([[0, 1], [1, 2]]) == -1
    assert determinant([[1, 2], [2, 4]]) == 0
    values = []
    for size in range(1, 26):
        shifted = determinant([[sequence[row + column + 2] for column in range(size)]
                               for row in range(size)])
        expected = 1 + 2 * sum(index ** 2 for index in range(size))
        index = size - 1
        assert 3 * shifted == 2 * index ** 3 + 3 * index ** 2 + index + 3
        assert shifted == expected
        for shift, target in [(1, 1 - size),
                              (0, -sum(index ** 2 for index in range(size - 1)))]:
            actual = determinant([[sequence[row + column + shift] for column in range(size)]
                                  for row in range(size)])
            assert actual == target, (size, shift, actual, target)
        values.append(shifted)
    family = polynomials(16)
    for left_degree, left in enumerate(family):
        for right_degree, right in enumerate(family):
            value = sum(left_coefficient * right_coefficient * moments[left_index + right_index]
                        for left_index, left_coefficient in enumerate(left)
                        for right_index, right_coefficient in enumerate(right))
            expected = (1 if left_degree == 0 else 2) if left_degree == right_degree else 0
            assert value == expected
    for degree, polynomial in enumerate(family[1:], start=1):
        assert polynomial[-1] == 1
        assert polynomial[0] == 2 * (-1) ** (degree - 1) * (degree - 1)
    parameters = [-3, 0, 1, 2, 5]
    for parameter in parameters:
        parameter_values = parameter_sequence(26, parameter)
        if parameter == 2:
            assert parameter_values == sequence[:27]
        for size in range(1, 13):
            targets = {2: 1 + parameter * sum(index ** 2 for index in range(size)),
                       1: 1 - size,
                       0: -sum(index ** 2 for index in range(size - 1))}
            for shift, target in targets.items():
                assert determinant([[parameter_values[row + column + shift]
                                     for column in range(size)] for row in range(size)]) == target
    path_values = []
    for semilength in range(1, 9):
        paths, partitions = combinatorial_counts(semilength)
        assert paths == partitions == sequence[semilength]
        path_values.append(paths)
    print(json.dumps({
        'status': 'pass',
        'arithmetic': 'exact integers; fraction-free determinants with row pivoting',
        'cubic_parameter_n': [0, 24],
        'adjacent_shift_matrix_orders': [1, 25],
        'moment_degrees': [0, 52],
        'orthogonality_degrees_each': [0, 16],
        'orthogonality_pairs': 289,
        'empty_determinant': 1,
        'first_ten_shifted_determinants': values[:10],
        'parameter_values': parameters,
        'parameter_matrix_orders': [1, 12],
        'parameter_determinants_checked': 180,
        'combinatorial_semilengths': [1, 8],
        'combinatorial_counts': path_values,
        'subsequence_convention': 'Exchanges preserve the order inherited from the ground sequence.',
        'all_index_coverage': 'Written proof in note.tex; finite checks cover the stated ranges.'
    }, indent=2))


if __name__ == '__main__':
    main()
