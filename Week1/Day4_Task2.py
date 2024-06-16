def knapSack(capacity, wt, profit, n):


    if n == 0 or capacity == 0:
        return 0

    if (wt[n-1] > capacity):
        return knapSack(capacity, wt, profit, n-1)


    else:
        return max(
            profit[n-1] + knapSack(
                capacity-wt[n-1], wt, profit, n-1),
            knapSack(capacity, wt, profit, n-1))


profit = [1, 4, 5, 7]
weight =  [1, 3, 4, 5]
capacity = 7
n = len(profit)
print (knapSack(capacity, weight, profit, n))

