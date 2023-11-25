def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fib_fast(n):
    if n <= 1:
        return n
    p,c,s=0,1,1

    for i in range((n-1)%60):

        p,c=c%10,(p+c)%10
        s+=c%10
    
    return s%10

if __name__ == '__main__':
    n = int(input())
    print(fib_fast(n))
