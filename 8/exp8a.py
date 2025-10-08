from functools import lru_cache

def countWays(caps, n):
    cap_to_persons = {i: [] for i in range(1, 101)}
    for person in range(n):
        for cap in caps[person]:
            cap_to_persons[cap].append(person)

    full_mask = (1 << n) - 1  

    @lru_cache(None)
    def solve(mask, cap):
        if mask == full_mask:
            return 1
        if cap > 100:
            return 0

        ways = solve(mask, cap + 1)

        for person in cap_to_persons[cap]:
            if not (mask & (1 << person)):
                ways += solve(mask | (1 << person), cap + 1)

        return ways

    return solve(0, 1)

caps1 = [[3, 4], [4, 5], [5]]
print("Input:", caps1)
print("Output:", countWays(caps1, len(caps1)))