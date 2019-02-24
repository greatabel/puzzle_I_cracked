'''
Let S(A) represent the sum of elements in set A of size n. 
We shall call it a special sum set if for any two non-empty disjoint subsets, 
B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
If S(A) is minimised for a given n, we shall call it an optimum special sum set. 
The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set 
is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24},
 with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to 
 provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 
 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

NOTE: This problem is related to Problem 105 and Problem 106.
'''

# skip this problem ,use https://bartriordan.wordpress.com/2014/04/16/project-euler-problem-103-solution/
# solution, I am not interested in this problem
import itertools
import time


def power_set(members):
    '''(tuple OR set OR list) -> list of sets

    Takes members, which is a tuple, set, or list representing the elements of
    the set for which a power set is desired. Populates a list with all the
    subsets of the group of members including the null set. Returns this list
    of sets.

    Note: in Python creating sets of sets is complicated and requires ordered
        sets, so this implementation actually returns a list of sets, not a
        set of sets.

    >>> power_set(set([1, 2, 3]))
    [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]

    >>> power_set([4, 21])
    [set(), {4}, {21}, {4, 21}]

    >>> power_set((10, 9, 4))
    [set(), {10}, {9}, {9, 10}, {4}, {10, 4}, {9, 4}, {9, 10, 4}]
    '''
    subsets = [[]]
    for member in members:
        subsets.extend([subset + [member] for subset in subsets])
    return [set(x) for x in subsets]  # Converts to list of sets.


def has_unique_subset_sums(members):
    '''(tuple OR set OR list) -> bool

    Takes members, which is a tuple, set, or list representing the elements of
    the set for which we would like to know if all subset sums are unique. The
    parameter members will henceforth be referred to as a set for convenience.
    Returns True if the number of non-empty subsets of members is equal to the
    number of elements in a set containing the sum of each subset. Returns
    False if the lengths differ, as this implies that at least two subsets
    have the same sum.

    >>> has_unique_subset_sums({2, 3, 4})
    True

    >>> has_unique_subset_sums((3, 5, 6, 7))
    True

    >>> has_unique_subset_sums([1, 3, 4])
    False
    '''
    # Lists all subsets of members and removes the null set from consideration:
    subsets = power_set(members)
    del subsets[0]  # We are interested only in non-empty subsets.

    # Creates a set containing the sums of all the subsets of members:
    sums = set(sum(subset) for subset in subsets)
    return len(sums) == 2 ** len(members) - 1


def has_duplicates(members):
    '''(tuple OR list) -> bool

    Takes members, which is a tuple or list representing the elements of the
    set for which a power set is desired. The parameter members will
    henceforth be referred to as a set for convenience. Returns True if
    members contains no duplicate values. Returns False otherwise.

    >>> has_duplicates([1, 2, 1, 3])
    True

    >>> has_duplicates((2, 3, 4, 5))
    False
    '''
    if len(members) != len(set(members)):
        return True
    else:
        return False


def is_special_sum_set(members):
    '''(tuple OR set OR list) -> bool

    Takes members, which is a tuple, set, or list representing the elements of
    the set for which a power set is desired. The parameter members will
    henceforth be referred to as a set for convenience. Returns True only if
    these two conditions both hold:
        1. The sum of each subset of members is unique. This is checked by
            the function has_unique_subset_sums; and,
        2. For any non-empty, disjoint subsets B and C, if B has more elements
            than C, then sum(B) > sum(C).

    Returns False otherwise.

    >>> is_special_sum_set({2, 3, 4})
    True

    >>> is_special_sum_set((3, 5, 6, 7))
    True

    >>> is_special_sum_set([1, 3, 4])
    False
    '''
    if (has_unique_subset_sums(members) and
        larger_subsets_have_larger_sums(members)):
            return True
    else:
        return False


def larger_subsets_have_larger_sums(members):
    '''(tuple OR set OR list) -> bool

    Takes members, which is a tuple, set, or list representing the elements of
    the set for which a power set is desired. The parameter members will
    henceforth be referred to as a set for convenience. Checks that for any
    non-empty, disjoint subsets B and C, if B has more elements than C, then
    sum(B) > sum(C). Returns True if this condition holds. Returns False
    otherwise.

    This condition is checked by comparing extreme cases: we consider every
    possible pair of disjoint subset sizes n and n - 1 for 1 < n. For each
    pair of sizes we compare the smallest possible sum of a subset of size n
    to the largest sum of a subset of size n - 1. (We increment n until any
    further increase in n would imply that the two subsets would not be
    disjoint. This occurs when n is equal to the integer portion of the length
    of members divided by two.) If the sums of the subsets of size n are
    larger than the sums of the subsets of size n - 1 in every case we know
    that the condition holds and we return True. If any sum of the subset of
    size n - 1 is larger than the associated sum of the subset of size n then
    we have proven that there is at least pair of sizes for which the
    condition does not hold and we return False.

    For example, if members contains 7 elements we compare the sums of these
    pairs of subsets:
        i. The smallest-sum subset of size 2 vs. the largest-sum
            subset of size 1;
        ii. The smallest-sum subset of size 3 vs. the largest-sum
            subset of size 2;
        iii. The smallest-sum subset of size 4 vs. the largest-sum
            subset of size 3.

    >>> larger_subsets_have_larger_sums({3, 5, 6, 7})
    True

    >>> larger_subsets_have_larger_sums([2, 5, 6, 7])
    False

    >>> larger_subsets_have_larger_sums((1, 2))
    True
    '''
    members_count = len(members)
    sorted_members = sorted(members)  # Sorted to make indexing easier.
    smallest_n_sum = sorted_members[0]  # Smallest sum of an n-member subset.
    largest_n_minus_one_sum = 0  # Largest sum of an (n - 1)-member subset.

    # Compares all n and n - 1 disjoint subset size pairs:
    for index in range(members_count // 2):
        # Adds next-largest item to smallest_n_sum:
        smallest_n_sum += sorted_members[index + 1]

        # Adds next-smallest item to largest_n_minus_one_sum:
        largest_n_minus_one_sum += sorted_members[members_count - index - 1]

        # Condition fails if any smaller subset doesn't have a smaller sum:
        if smallest_n_sum <= largest_n_minus_one_sum:
            return False

    # Returns True if both conditions hold:
    return True


if __name__ == '__main__':
    start_time = time.time()

    # Initializes variables that track the most-optimum special sum set so far:
    current_best = set([20, 31, 38, 39, 40, 44, 46])
    current_best_sum = sum(current_best)

    # Loops over each candidate tuple close to the baseline set:
    for candidate in itertools.product(*[list(range(x - 3, x + 4)) for
                                         x in current_best]):

        # Skips any candidate tuples with larger sums than the current minimum:
        if sum(candidate) >= current_best_sum:
            continue

        # Skips any candidate tuples containing duplicate values:
        elif has_duplicates(candidate):
            continue

        # Checks if the candidate is a special sum set:
        elif is_special_sum_set(candidate):
            # Records the new most-optimum candidate set and its sum:
            current_best = set(candidate)
            current_best_sum = sum(candidate)

    # Converts optimum set to a sorted list and then the associated set string:
    optimum_list = sorted(list(current_best))
    solution_set_string = "".join([str(item) for item in optimum_list])
    print("The set string of the optimum special sum set for n = 7 is {}."
          .format(solution_set_string))

    end_time = time.time()
    print("Execution time: {}".format(end_time - start_time))