
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TDRC, APIC, TRCK, error

# Load the MP3 file
audio = ID3("Nlimpoteza-my-mum.mp3")

# Set title
audio["TIT2"] = TIT2(encoding=3, text="Nilimpoteza my mum")

# Set artist
audio["TPE1"] = TPE1(encoding=3, text="Okinyo Violet")

# Set album
audio["TALB"] = TALB(encoding=3, text="Startre 2024")

# Set genre
audio["TCON"] = TCON(encoding=3, text="General")

# Set year/date
audio["TDRC"] = TDRC(encoding=3, text="2024")

# Set track number (optional)
audio["TRCK"] = TRCK(encoding=3, text="1/12")  # Track 1 of 12

# Add album art (cover image)
with open("../DCIM/Screenshots/Screenshot_20240806_212427_Lite.jpg", "rb") as albumart:
    audio["APIC"] = APIC(
        encoding=3,          # UTF-8 encoding
        mime="image/jpeg",   # MIME type of the image
        type=3,              # Front cover image
        desc=u"Cover",       # Description
        data=albumart.read()  # Read the image data
    )

# Save changes
audio.save()

print("Metadata has been added successfully.")
