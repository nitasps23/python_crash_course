# Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number
# of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.


def make_album(artist_name, album_title, track_count=0):
    """Return a dictionary describing a music album."""
    if track_count:
        music_album = {'artist': artist_name, 'title': album_title, 'track_count': track_count}
    else:
        music_album = {'artist': artist_name, 'title': album_title}

    return music_album



album = make_album('alicia keys', 'unplugged')
print(album)

album = make_album('the beatles', 'rubber soul')
print(album)

album = make_album('beyonce', 'lemonade')
print(album)

album = make_album('rihanna', 'unapologetic', track_count=14)
print(album)

