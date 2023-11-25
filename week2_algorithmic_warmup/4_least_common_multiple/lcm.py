def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False

def gcd_fast(a,b):
    if b==0:
      return a
    c=a%b
    return gcd_fast(b,c)
def lcm_fast(a,b):
    return int((a*b)/gcd_fast(a,b))


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm_fast(a, b))

