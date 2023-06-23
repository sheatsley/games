; directives
#Requires AutoHotkey >=2.0                                                  ; require AutoHotkey v2

; user configuration
xResolution := 3860                                                         ; display resolution width
yResolution := 1600                                                         ; display resolution height
pauseKey := "\"                                                             ; script pause key
basicSkillKey := "LButton"                                                  ; basic skill slot key
coreSkillKey := "RButton"                                                   ; core skill slot key
skill1Key := "q"                                                            ; skill slot 1 key
skill2Key := "3"                                                            ; skill slot 2 key
skill3Key := "e"                                                            ; skill slot 3 key
skill4Key := "r"                                                            ; skill slot 4 key
moveKey := "Middle"                                                         ; move key
holdPositionKey := "Tab"                                                    ; hold position key

; script configuration
windowName := "Diablo IV"                                                   ; name of the Diablo IV window
xOffset := 10                                                               ; x offset from center of screen
yOffset := 35                                                               ; y offset from center of screen
xCenter := xResolution // 2 - xOffset                                       ; character x position
yCenter := yResolution // 2 - yOffset                                       ; character y position
clickDistance := 115                                                        ; distance from center to click
clickPrecision := 10                                                        ; randomness added to click position
clickRate := 100                                                            ; click rate in milliseconds
horizontalBias := 35                                                        ; further extends horizontal click distance

; script setup
isPaused := false                                                           ; initialize script pause state
SetControlDelay(0)                                                          ; minimize mouse control delay (enables middle-mouse to move)
WinWaitActive(windowName)                                                   ; wait for Diablo IV to be the active window
Sleep(1000)                                                                 ; wait 1 second before starting the timer
SoundBeep(261, 100)                                                         ; (1) low-high beep to indicate WASD scanning
SoundBeep(523, 100)                                                         ; (2) low-high beep to indicate WASD scanning
SetTimer(Main, clickRate)                                                   ; scan for WASD keys at the specified rate

; hotkey configuration
HotIfWinActive(windowName)                                                  ; only register hotkeys if Diablo IV is active
Hotkey(pauseKey, PauseScript)                                               ; register the pause key
Hotkey("~" basicSkillKey, HoldOnSkill)                                      ; set basic skill key to attack without moving (1)
Hotkey("~" basicSkillKey " Up", ReleaseHold)                                ; set basic skill key to attack without moving (2)

;functions
Main() {
    if !WinExist(windowName) {                                              ; exit if the window has been closed
        SoundBeep 523, 100                                                  ; (1) high-low beep to indicate WASD scanning
        SoundBeep 261, 100                                                  ; (2) high-low beep to indicate WASD scanning
        ExitApp                                                             ; exit the script
    }
    if WinActive(windowName) and !isPaused  {                               ; confirm Diablo IV is active and the script is not paused
        yClick := GetKeyState("w") ? -clickDistance : 0                     ; compute click position from W state
        xClick := GetKeyState("a") ? -clickDistance - horizontalBias : 0    ; compute click position from A state
        yClick += GetKeyState("s") ? clickDistance : 0                      ; compute click position from S state
        xClick += GetKeyState("d") ? clickDistance + horizontalBias : 0     ; compute click position from D state
        if !(xClick = 0 and yClick = 0) {                                   ; check if the calculated position is not the center
            ControlClick "x" xCenter + xClick + Random(clickPrecision)
                . " y" yCenter + yClick + Random(clickPrecision),,, moveKey ; click the moveKey at the calculated position
        }
    }
}
PauseScript(ThisHotKey) {
    global isPaused := !isPaused                                            ; toggle the pause state
    SoundBeep 523, 200                                                      ; long-high beep to indicate script pause state
}
HoldOnSkill(ThisHotKey) {
    Send("{" holdPositionKey " down}")                                      ; press the hold position key on skill press
}
ReleaseHold(ThisHotKey) {
    Send("{" holdPositionKey " up}")                                        ; release the hold position key on skill release
}
