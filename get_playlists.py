#
# To use this:
#   copy spotify web player view with visible playlists (html from F12)
#   run this script
#   paste in https://playlists.dags.dev/playlists/import and press Import
#

import pickle
import pyperclip

# with open("in/1.html", "r", encoding="utf-8") as file:
#     data = file.read()

# get from clipboard
data = pyperclip.paste()

splits = data.split('href="/playlist/')
playlist_ids = [s[:22] for s in splits][1:]
d = dict.fromkeys(playlist_ids)


with open ("out/db", "rb") as db:
    all_playlists = pickle.load(db)

print("had: ", len(all_playlists))

have = all_playlists | d  # merge
print(f"added {len(have)-len(all_playlists)}")

with open ("out/db", "wb") as db:
    pickle.dump(have, db)

playlist_ids = list(set(d) - set(all_playlists))  # dedup

joined = ",".join(playlist_ids)
print(len(playlist_ids))

# to clipboard
pyperclip.copy(joined)