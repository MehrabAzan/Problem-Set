def max_audience_performances(audiences):
    freq = {}
    for audience in audiences:
        freq[audience] = freq.get(audience, 0) + 1
    maxTotal = max(freq.keys())
    for key, value in freq.items():
        if key == maxTotal:
            return key * value

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

# Dictionary makes the code more complex conceptually and computationally.
# More resources is needed for the dictionary solution as well.