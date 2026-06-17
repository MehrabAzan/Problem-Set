def num_popular_pairs(popularity_scores):
    result = 0
    for i in range(len(popularity_scores)):
        for j in range(len(popularity_scores)):
            if i < j and popularity_scores[i] == popularity_scores[j]:
                result += 1
    return result

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 