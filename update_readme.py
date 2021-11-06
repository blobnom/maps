from pathlib import Path

base = """# NekoShabeta maps i've passed so far:
All replays are available on [this discord server](https://discord.gg/F4Dw7qEgRY) too."""

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
        

        replay_str = ' | '.join(replay_str)
        screenshot_str = '\n'.join(screenshot_str)

        maps.append(f"## {folder_name} {replay_str}\n{screenshot_str}")
    return '\n\n\n'.join(maps)

updated_readme = generate()
with open('./README.md', 'w+') as f:
    f.write(base + "\n\n" + updated_readme)
