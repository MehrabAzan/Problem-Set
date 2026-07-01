def best_set(votes):
    freq = {}
    for attendeesId, artist in votes.items():
        freq[artist] = freq.get(artist, 0) + 1
    maxVotes = max(freq.values())
    for artist, count in freq.items():
        if count == maxVotes:
            return artist

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))