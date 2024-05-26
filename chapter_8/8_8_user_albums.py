# Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, track_count=0):
    """Return a dictionary describing a music album."""
    if track_count:
        music_album = {'artist': artist_name, 'title': album_title, 'track_count': track_count}
    else:
        music_album = {'artist': artist_name, 'title': album_title}

    return music_album

while True:

    print("\nPlease enter the album info:")
    print("(enter 'q' at any time to quit)")

    artist = input("\nEnter the artist name: ")
    if artist == 'q':
        break

    title = input("Enter the album title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)