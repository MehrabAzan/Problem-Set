def expose_superman(trust, n):
    trusts = [0] * (n + 1)
    trustedBy = [0] * (n + 1)

    for ai, bi in trust:
        trusts[ai] += 1
        trustedBy[bi] += 1

    for person in range(1, n + 1):
        if trustedBy[person] == n - 1 and trusts[person] == 0:
            return person

    return -1

n = 2
trust = [[1, 2]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(expose_superman(trust, n))