def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fib_fast(n):
    if n <= 1:
        return n
    p,c=0,1
    lst=[1]
    for i in range(2,61):
        f=p%10+c%10
        lst.append(lst[-1]+((f%10)**2))
        p,c=c%10,f%10
    return lst[n%60-1]%10

if __name__ == '__main__':
    n = int(input())
    print(fib_fast(n))
