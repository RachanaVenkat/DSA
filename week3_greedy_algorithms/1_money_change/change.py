def change(money):
    ten=0
    five=0
    one=0
    while money!=0:
        if money>=10:
            a=int(money/10)
            ten+=a
            money-= 10*a
        elif money>=5:
            b=int(money/5)
            five += b
            money-=5*b
        else:
            one += 1
            money -= 1
        

    return (ten+five+one)


if __name__ == '__main__':
    m = int(input())
    print(change(m))
