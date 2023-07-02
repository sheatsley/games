## HotS

This is *HoTs* - a repo for adding toggleable abilities in [Heroes of the
Storm](https://heroesofthestorm.blizzard.com/en-us/). Specifically, it's a
simple [AutoHotkey](https://www.autohotkey.com) script that: (1) scans for an
incoming key press initiated via the `mapKey` (defaulted to `Delete`), and (2)
creates a dynamic Hotkey that keeps the key held down until it pressed again.

## How to use this repo

Requirements:
- [AutoHotkey v2.0](https://www.autohotkey.com)

Start the `hots.ahk` script and the game. The script will wait until the Heroes
of the Storm window is active, which will induce audible beeps to designate
that the script is ready to read keys. When you quit the game, the script
induce an audible beep and will automatically terminate itself. The script can
be dynamically paused via `pauseKey` (defaulted to the `\` key), denoted with a
beep.

After pressing the `mapKey`, two audible beeps designate that the next incoming
key press will become a map. Afterwards, two additional audible beeps denote
that the mapping was successful. The `resetKey` (defaulted to `Home`) resets
all mappings by releasing any currently pressed key and subsequently reloads
the script.
