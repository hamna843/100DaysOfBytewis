def longest_common_subsequence(s1, s2):
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    longest = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                longest[i][j] = s1[i - 1]
            else:
                if matrix[i - 1][j] > matrix[i][j - 1]:
                    matrix[i][j] = matrix[i - 1][j]
                    longest[i][j] = longest[i - 1][j]
                else:
                    matrix[i][j] = matrix[i][j - 1]
                    longest[i][j] = longest[i][j - 1]

    result = ""
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result = s1[i - 1] + result
            i -= 1
            j -= 1
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return result

str1 = "AGGTAB"
str2 = "GXTXAYB"
print(longest_common_subsequence(str1, str2))