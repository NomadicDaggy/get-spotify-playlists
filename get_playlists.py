with open("in/1.html", "r", encoding="utf-8") as file:
    data = file.read()
    splits = data.split('href="/playlist/')
    playlist_ids = [s[:22] for s in splits][1:]
    # dedup
    playlist_ids = list(dict.fromkeys(playlist_ids))
    print(",".join(playlist_ids))
