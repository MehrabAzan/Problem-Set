def find_villain(crowd, villain):
    result = []
    for i in range(len(crowd)):
        if villain == crowd[i]:
            result.append(i)
    return result

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
print(find_villain(crowd, villain))