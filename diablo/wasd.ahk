xResolution := 3860
yResolution := 1600
tickRate := 400
tickRateDeviation := 200
clickDeviation := 10
pauseKey := Del

xCenter := xResolution // 2 + 0
yCenter := yResolution // 2 - 36
clickRadius := yCenter // 2
xStop := 45
yStop := 35
wStop := {x: xCenter, y: yCenter - yStop}
wdStop := {x: xCenter + xStop, y: yCenter - yStop}
dStop := {x: xCenter + xStop, y: yCenter}
dsStop := {x: xCenter + xStop, y: yCenter + yStop}
sStop := {x: xCenter, y: yCenter + yStop}
saStop := {x: xCenter - xStop, y: yCenter + yStop}
aStop := {x: xCenter - xStop, y: yCenter}
awStop := {x: xCenter - xStop, y: y - yStop}

SendMode Input
SetTitleMatchMode, 3
paused := false
WinWaitActive, Diablo IV
Sleep 1000
SoundBeep

#IfWinActive Diablo IV
w::
Critical
yPos := yCenter - clickRadius
ControlClick,x%xCenter% y%yPos%
return

w & d::
Critical
xPos := xCenter + clickRadius
yPos := yCenter - clickRadius
ControlClick,x%xPos% y%yPos%
return

a::
Critical
xPos := xCenter - clickRadius
ControlClick,x%xPos% y%yCenter%
return

s::
Critical
YPos := yCenter + clickRadius
ControlClick,x%xCenter% y%yPos%
return

d::
Critical
xPos := xCenter + clickRadius
ControlClick,x%xPos% y%yCenter%
return

;w up::
;a up::
;s up::
;d up::
;Critical
;ControlClick,x1920 y777
;return
