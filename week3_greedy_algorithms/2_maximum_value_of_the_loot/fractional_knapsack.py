from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0
    pervalue=[]

    while capacity!=0:
        for i in range(len(weights)):
            pervalue.append(values[i]/weights[i])
        m = pervalue.index(max(pervalue))
        amount = min(capacity,weights[m])
        value+=amount[m]*(pervalue[m])
        pervalue[m]=0
        capacity-=amount
            



    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
