SendMode Input
SetTitleMatchMode, 3
WinWaitActive, Diablo IV
Sleep 1000
SoundBeep
#IfWinActive Diablo IV
w::
Critical
ControlClick,x1920 y10
return

a::
Critical
ControlClick,x10 y760
return

s::
Critical
ControlClick,x1920 y1430
return

d::
Critical
ControlClick,x3850 y760
return

w up::
a up::
s up::
d up::
Critical
Sleep 200
ControlClick,x1920 y777,,,L
return
