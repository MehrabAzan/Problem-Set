def delete_minimum_elements(hunny_jar_sizes):
    result = []
    while hunny_jar_sizes:
        for num in hunny_jar_sizes:
            if num == min(hunny_jar_sizes):
                hunny_jar_sizes.remove(num)
                result.append(num)
    return result

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))