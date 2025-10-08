def distributeCookies(cookies, k):
    n = len(cookies)
    distribution = [0] * k
    result = float('inf')

    def backtrack(index):
        nonlocal result
        if index == n:
            result = min(result, max(distribution))
            return

        for i in range(k):
            distribution[i] += cookies[index]
            backtrack(index + 1)
            distribution[i] -= cookies[index]

            if distribution[i] == 0:
                break

    backtrack(0)
    return result

cookies = [8, 15, 10, 20, 8]
k = 2
print("Input:", cookies, "k =", k)
print("Output:", distributeCookies(cookies, k))