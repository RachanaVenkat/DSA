from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0
    numbers.sort()
    rev = numbers[::-1]
    for i in range(len(numbers)):
        largest += numbers[i]



    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
