#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# https://projecteuler.net/problem=1

def find_all_numbers(divA,divB,bound):
    results = []
    for i in range(1, bound):
        # print(i)
        if i % divA == 0 or i % divB == 0:
            # print(i)
            results.append(i)
    # print(results)
    return results



if __name__ == "__main__":
    results = find_all_numbers(3,5,1000)
    # print("#",results)
    print(sum(results))