# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W


def knapSack(capacity, wt, profit, n):

    # Base Case
    if n == 0 or capacity == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > capacity):
        return knapSack(capacity, wt, profit, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
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

