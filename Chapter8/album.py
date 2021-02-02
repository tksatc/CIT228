def make_album(artist, title, numberSongs=0):
    """Return a dictionary of album information"""
    if numberSongs>0:
        album = {"artist": artist, "title": title, "numberOfSongs": numberSongs}
    else:
        album = {"artist": artist, "title": title}
    return album

record1 = make_album("Elvis Presley", "Jailhouse Rock")
record2 = make_album("George Michael", "Last Christmas")
record3 = make_album("TSO", "Christmas in Sarajevo")

print(record1)
print(record2)
print(record3)

record4 = make_album("Mannheim Steamroller", "Carol of the Bells", 13)
print(record4)

run = True

while run:
    response = input("\nWould you like to create an albmut?  Enter 'q' to quit or any other key to continue: ")
    if response.lower() == "q":
        print("Come back again later.")
        run = False
        break
    else:
        artistName = input("Enter the name of the artist: ")
        albumTitle = input("Enter the title of the album: ")
        songNumber = int(input("Enter the number of songs on the album, or '0' if unknown: "))

        if songNumber > 0:
            newAlbum = make_album(artistName.lower(), albumTitle.lower(), songNumber)
        else:
            newAlbum = make_album(artistName.lower(), albumTitle.lower())

        print("\n", newAlbum)