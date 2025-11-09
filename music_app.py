import random

class Artist:
    def __init__(self, artist_navn, medlemmer_liste):
        self.artist_navn = artist_navn
        self.medlemmer_liste = medlemmer_liste

    def er_solo_artist(self):
        """Return True if the artist has only one member."""
        return len(self.medlemmer_liste) < 2


class Sanger:
    def __init__(self, sang_tittel, komponist):
        self.sang_tittel = sang_tittel
        self.komponist = komponist

    def hentsang(self):
        """Print the song title."""
        print(f"🎵 {self.sang_tittel} – {self.komponist}")


class Album:
    antall_album = 0

    def __init__(self, album_tittel, artist, sangliste):
        Album.antall_album += 1
        self.serienummer = Album.antall_album
        self.album_tittel = album_tittel
        self.artist = artist
        self.sangliste = sangliste

    def hent_serienummer(self):
        """Return the album's serial number."""
        return self.serienummer

    def hent_album_info(self):
        """Print info about the album and its songs."""
        print("\n📀 Album:", self.album_tittel)
        print("👩‍🎤 Artist:", self.artist.artist_navn)
        print("Solo artist:", self.artist.er_solo_artist())
        print("Sanger:")
        for s in self.sangliste:
            print(f"  - {s.sang_tittel} ({s.komponist})")


def velg_album(albumliste):
    """Let the user choose an album by artist name."""
    artist_navn = input("Hvilken artist? (eller trykk Enter for alle): ")

    found = False
    for album in albumliste:
        if artist_navn.lower() == album.artist.artist_navn.lower() or artist_navn == "":
            album.hent_album_info()
            found = True

    if not found:
        print("Ingen album funnet for den artisten.")


mine_album = []

artist1 = Artist("Nina Simone", ["Nina Simone"])
sanger1 = [
    Sanger("I Put a Spell on You", "Nina Simone"),
    Sanger("Feeling Good", "Nina Simone")
]
mine_album.append(Album("Smooth Jams", artist1, sanger1))

artist2 = Artist("Frank Sinatra", ["Frank Sinatra"])
sanger2 = [
    Sanger("Fly Me to the Moon", "Frank Sinatra"),
    Sanger("That's Life", "Frank Sinatra")
]
mine_album.append(Album("Classic Sinatra", artist2, sanger2))

print(f"\n📚 Antall album: {len(mine_album)}")
for album in mine_album:
    print(f"{album.serienummer}. {album.album_tittel} – {album.artist.artist_navn}")

# Let user pick an album
velg_album(mine_album)
