import pickle
import pyperclip

with open ("out/db", "rb") as db:
    all_playlists = pickle.load(db)

joined = ",".join(all_playlists)
print(len(all_playlists))
with open("out/all.txt", "w") as f:
    f.write(joined)

# to clipboard
#pyperclip.copy(joined)
