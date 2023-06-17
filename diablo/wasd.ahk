xResolution := 3860
yResolution := 1600
tickRate := 100
tickRateDeviation := 200
clickDeviation := 10
pauseKey := Del

xCenter := xResolution // 2 - 10
yCenter := yResolution // 2 - 35
;clickRadius := yCenter // 2 + 25
clickRadius := 115
angleAdjust := 35
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
fuge := 10

xL := xCenter - clickRadius
xR := xCenter + clickRadius
yT := yCenter - clickRadius
yB := yCenter + clickRadius
length := clickRadius*2
Gui, top:-Caption +ToolWindow
Gui, top:Show, x%xL% y%yT% h2 w%length%
Gui, bot:-Caption +ToolWindow
Gui, bot:Show, x%xL% y%yB% h2 w%length%
Gui, left:-Caption +ToolWindow
Gui, left:Show, x%xL% y%yT% h%length% w2
Gui, right:-Caption +ToolWindow
Gui, right:Show, x%xR% y%yT% h%length% w2

Gui, wPos:-Caption +ToolWindow
Gui, wPos:Color, Red
Gui, wPos:Show, x%xCenter% y%yT% h15 w15
Gui, aPos:-Caption +ToolWindow
Gui, aPos:Color, Red
Gui, aPos:Show, x%xL% y%yCenter% h15 w15
Gui, sPos:-Caption +ToolWindow
Gui, sPos:Color, Red
Gui, sPos:Show, x%xCenter% y%yB% h15 w15
Gui, dPos:-Caption +ToolWindow
Gui, dPos:Color, Red
Gui, dPos:Show, x%xR% y%yCenter% h15 w15

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
		;yPos := yPos + (GetKeyState("w", "P") ? -clickRadius : yPrev < yCenter ? fuge : 0)
		;xPos := xPos + (GetKeyState("a", "P") ? -clickRadius : xPrev < xCenter ? fuge : 0)
		;yPos := yPos + (GetKeyState("s", "P") ? clickRadius : yPrev > yCenter ? -fuge : 0)
		;xPos := xPos + (GetKeyState("d", "P") ? clickRadius : xPrev > xCenter ? -fuge : 0)
		yPos := yPos + (GetKeyState("w", "P") ? -clickRadius : 0)
		xPos := xPos + (GetKeyState("a", "P") ? -clickRadius - angleAdjust : 0)
		yPos := yPos + (GetKeyState("s", "P") ? clickRadius : 0)
		xPos := xPos + (GetKeyState("d", "P") ? clickRadius + angleAdjust : 0)
		;if !(xPos = xCenter and yPos = yCenter and xPrev = xPos and yPrev = yPos)
		if !(xPos = xCenter and yPos = yCenter)
		{
			Tooltip, xM %xPos% yM %yPos%`nxC %xCenter% yC %yCenter%, %xPos%, %yPos%
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


; exit script on quit
