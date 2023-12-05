from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0
    numbers.sort()
    rev = numbers[::-1]
    for i in range(len(numbers)):
        largest += numbers[i]



    return largest

def max_sal(numbers):
    numbers = list(map(str,numbers))
    largest=''
    # largest1 = ''
    # for i in range(len(numbers)):
    #     largest1 += numbers[i]
    # largest1=[*largest1]
    for i in range(len(numbers)):
        m=max(numbers)
        largest += m
        numbers.remove(m)
        
        
    return int(largest)

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(max_sal(input_numbers))
