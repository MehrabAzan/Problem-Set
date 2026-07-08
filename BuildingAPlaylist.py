class SongNode:
    def __init__(self, song, artist_or_next=None, next=None):
        self.song = song
        if next is not None:
            self.artist = artist_or_next
            self.next = next
        elif isinstance(artist_or_next, SongNode) or artist_or_next is None:
            self.artist = None
            self.next = artist_or_next
        else:
            self.artist = artist_or_next
            self.next = None

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()

def get_artist_frequency(playlist):
    freq = {}
    current = playlist
    while current:
        artist = current.artist
        freq[artist] = freq.get(artist, 0) + 1
        current = current.next
    return freq

# time complexity: O(n)
# space complexity: O(n)

# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

print_linked_list(top_hits_2010s)
print("\n")

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))
print("\n")

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))
print("\n")