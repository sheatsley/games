xResolution := 3860
yResolution := 1600
tickRate := 100
tickRateDeviation := 200
clickDeviation := 10
pauseKey := Del

xCenter := xResolution // 2 - 20
yCenter := yResolution // 2 - 20
clickRadius := yCenter // 2 + 400
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

#NoEnv
#Persistent
#MaxHotKeysPerInterval, 200
SendMode Input
SetTitleMatchMode, 3
paused := false
xPrev := xCenter
yPrev := yCenter
WinWaitActive, Diablo IV
Sleep 1000
SoundBeep
SetTimer, Main, %tickRate%
return

Main:
	if (WinActive("Diablo IV"))
	{
		xPos := xCenter
		yPos := yCenter
		yPos := yPos + (GetKeyState("w", "P") ? -clickRadius : 0)
		xPos := xPos + (GetKeyState("a", "P") ? -clickRadius : 0)
		yPos := yPos + (GetKeyState("s", "P") ? clickRadius : 0)
		xPos := xPos + (GetKeyState("d", "P") ? clickRadius : 0)
		if !(xPos = xCenter and yPos = yCenter and xPrev = xPos and yPrev = yPos)
		{
			Tooltip, yes x%xPos% y%yPos%, %xPos%, %yPos%
			ControlClick, x%xPos% y%yPos%
		}
		else
		{
			ToolTip
		}
		xPrev := xPos
		yPrev := yPos
		Sleep 40
	}
return

#IfWinActive Diablo IV
;w::
;Critical
;yPos := yCenter - clickRadius
;ControlClick,x%xCenter% y%yPos%
;return

;w & d::
;Critical
;xPos := xCenter + clickRadius
;yPos := yCenter - clickRadius
;ControlClick,x%xPos% y%yPos%
;return

;a::
;Critical
;xPos := xCenter - clickRadius
;ControlClick,x%xPos% y%yCenter%
;return

;s::
;Critical
;YPos := yCenter + clickRadius
;ControlClick,x%xCenter% y%yPos%
;return

;d::
;Critical
;xPos := xCenter + clickRadius
;ControlClick,x%xPos% y%yCenter%
;return

;w up::
;a up::
;s up::
;d up::
;Critical
;ControlClick,x1920 y777
;return
