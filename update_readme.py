from pathlib import Path
import requests
import os

base = """# This repository was made to keep track of which maps created by NekoShabeta I've passed so far as I'm trying to pass all of them :)
## I thought I'd revive this since it was a lot of fun.
## Current Progress: {} / {} ({:.2f}%)"""

# for progress
count = 0
maxcount = 0

# for retrieving of user's map count
APIKEY = os.environ["APIKEY"]
USERID = 12017880

def get_map_count():
    url = "https://osu.ppy.sh/api/get_beatmaps?k={}&u={}".format(APIKEY, USERID)
    r = requests.get(url)
    return len(r.json())

def generate():
    maps = []
    for folder in Path("./maps/").iterdir():
        if folder.is_file():
            continue

        folder_name = folder.name

        replay_str = []
        screenshot_str = []

        for file in folder.iterdir():
            file_name = file.name
            if file_name.endswith(".osr"):
                mods = ""
                if "+" in file_name:
                    mods = " " + file_name.split(" ")[1].split(".osr")[0]
                replay_str.append(f"<a href='maps/{folder_name}/{file_name}'>Replay{mods}</a>")
            elif file_name.endswith(".jpg"):
                screenshot_str.append(f"<img src='maps/{folder_name}/{file_name}'></img>")
            count += 1
        

        replay_str = ' | '.join(replay_str)
        screenshot_str = '\n'.join(screenshot_str)

        maps.append(f"## {folder_name} {replay_str}\n{screenshot_str}")
    return '\n\n\n'.join(maps)

updated_readme = generate()
maxcount = get_map_count()
with open('./README.md', 'w+') as f:
    f.write(base.format(count, maxcount, ((count / maxcount) * 100)) + "\n\n" + updated_readme)
