def max_audience_performances(audiences):
    maxSize = max(audiences)
    result = 0
    for audience in audiences:
        if audience == maxSize:
            result += audience
    return result

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))