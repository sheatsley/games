; user configuration
xResolution := 3860																	    ; display resolution width
yResolution := 1600					                       							    ; display resolution height
pauseKey := "\"																			; script pause key

; script configuration
xOffset := 10						                       							    ; x offset from center of screen
yOffset := 35						                       							    ; y offset from center of screen
xCenter := xResolution // 2 - xOffset                       						    ; character x position
yCenter := yResolution // 2 - yOffset                       						    ; character y position
clickDistance := 115				                       							    ; distance from center to click
clickRate := 100					                       							    ; click rate in milliseconds
horizontalBias := 35				                       							    ; further extends horizontal click distance

; WASD relative click positions
wClick := -clickDistance															    ; vertical click position for W
aClick := -clickDistance - horizontalBias											    ; horizontal click position for A
sClick := clickDistance																    ; vertical click position for S
dClick := clickDistance + horizontalBias										        ; horizontal click position for D

; gui drawing
lineLength := clickDistance * 2					           							    ; line length for bounding box
topLeft := % "x"xCenter + aClick " y"yCenter + wClick								    ; top left corner of the bounding box
bottomLeft := % "x"xCenter + aClick " y"yCenter + sClick							    ; bottom left corner of the bounding box
topRight := % "x"xCenter + dClick " y"yCenter + wClick								    ; top right corner of the bounding box
Gui, topLine:-Caption +ToolWindow						   							    ; top line of the bounding box
Gui, topLine:Show, % topLeft " h2 w"lineLength + horizontalBias * 2					    ; draw a line from top left to top right
Gui, bottomLine:-Caption +ToolWindow					   							    ; bottom line of the bounding box
Gui, bottomLine:Show, % bottomLeft " h2 w"lineLength + horizontalBias * 2			    ; draw a line from bottom left to bottom right
Gui, leftLine:-Caption +ToolWindow						   							    ; left line of the bounding box
Gui, leftLine:Show, % topleft " h"lineLength " w2"									    ; draw a line from top left to bottom left
Gui, rightLine:-Caption +ToolWindow 					   							    ; right line of the bounding box
Gui, rightLine:Show, % topRight " h"lineLength " w2"								    ; draw a line from top right to bottom right
Gui, xLine:-Caption +ToolWindow														    ; horizontal line at yCenter
Gui, xLine:Show % "x"xCenter + aClick - 10 " y"yCenter " h1 w"dClick * 2 + 20			; draw a horizontal line at yCenter
Gui, yLine:-Caption +ToolWindow														    ; vertical line at xCenter
Gui, yLine:Show % "x"xCenter " y"yCenter + wClick - 10 " h"sClick * 2 + 20 " w1"	    ; draw a vertical line at xCenter

; main script
WinWaitActive, Diablo IV															    ; wait for Diablo IV to be the active window
Sleep 1000																			    ; wait 1 second before starting the timer
SoundBeep, 261, 93																	    ; (1) low-high beep to indicate WASD scanning
SoundBeep, 523, 93 																	    ; (2) low-high beep to indicate WASD scanning
Gui, Destroy																		    ; remove the bounding box and click positions
isPaused := false																	    ; initialize script pause state
HotKey, %pauseKey%, Pause															    ; register the pause key
SetTimer, Main, %clickRate%															    ; scan for WASD keys at the specified rate
Main:
	if !WinExist("Diablo IV")														    ; exit if Diablo IV has been closed
	{
		SoundBeep, 523, 93 															    ; (1) high-low beep to indicate WASD scanning
		SoundBeep, 261, 93 															    ; (2) high-low beep to indicate WASD scanning
		ExitApp																		    ; exit the script
	}
	if WinActive("Diablo IV") and !isPaused											    ; confirm Diablo IV is active and the script is not paused
	{
		yClick := GetKeyState("w", "P") ? wClick : 0							        ; compute click position from W state
		xClick := GetKeyState("a", "P") ? aClick : 0								    ; compute click position from A state
		yClick += GetKeyState("s", "P") ? sClick : 0								    ; compute click position from S state
		xClick += GetKeyState("d", "P") ? dClick : 0								    ; compute click position from D state
		if !(xClick = 0 and yClick = 0)												    ; check if the calculated position is not the center
		{
			ControlClick, % "x"xCenter + xClick " y"yCenter + yClick				    ; click the mouse at the calculated position
		}
		Sleep 40																	    ; ensure clicks are at least 40ms apart
	}
return
Pause:
if WinActive("Diablo IV")
{
	isPaused := !isPaused															    ; toggle the pause state
	SoundBeep, 523, 125															        ; long-high beep to indicate script pause state
}
return
