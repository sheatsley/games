## Diablo

This is *Diablo* - a repo for adding WASD movement in [Diablo
IV](https://diablo4.blizzard.com). Specifically, it's a simple
[AutoHotkey](https://www.autohotkey.com) script that: (1) scans if W, A, S, or
D is pressed down at a parameterized click rate (via `clickRate`), and (2)
left-clicks above, to the left, below, or to the right of your character (with
distance set by `clickDistance`) based on what is pressed down (including
diagonals). 

## How to use this repo

Requirements:
- [AutoHotkey v2.0](https://www.autohotkey.com)

Start the `diablo.ahk` script and the game. The script will wait until the
Diablo IV window is active, which will induce an audible beep to designate that
the script is now scanning for W, A, S, or D. Before the game is detected, a
white bounding box with red squares is drawn on the screen which shows where
the script considers the center of the screen to be as well as the locations
that are mapped to W, A, S, and D (which was helpful in designing this script
since characters are slightly offset from the center, as parameterized by
`xOffset` and `yOffset`). When you quit the game, the script induce an audible
beep and will automatically terminate itself. Finally, the script can be
dynamically paused via `pauseKey` (defaulted to the `\` key), denoted with a
beep.

For most users, simply changing `xResolution` and `yResolution` to match your
monitor should be sufficient to get this to work out of the box. If character
movement isn't smooth, I'd try manipulating: (1) `clickDistance` (this should
be as small as possible to ensure your character stops moving on key release),
(2) `xCenter` and `yCenter`, and (3) `angleAdjust` (which biases movement to
the right and left when moving diagonally). Notably, ensure you have no
abilities bound to W, A, S, or D  and ensure "Combine Move/Interact/Basic Skill
Slot" is toggled off (to prevent interacting with the environment during
movement).

This script was inspired by [Universal
WASD](https://www.desiquintans.com/wasdcontrols) and
[Diablo-IV_AHK-WASD](https://github.com/hwnd-git/Diablo-IV-AHK-WASD).
