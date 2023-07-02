; directives
#Requires AutoHotkey >=2.0                                          ; require AutoHotkey v2

; user configuration
mapKey := "Delete"                                                  ; key to intiate recording
pauseKey := "\"                                                     ; script pause key
resetKey := "Home"                                                  ; key to remove all hotkeys

; script configuration
windowName := "Heroes of the Storm"                                 ; name of the HotS window

; script setup
isPaused := false                                                   ; initialize script pause state
mappedKeys := Map()                                                 ; initialize set of mapped keys
WinWaitActive(windowName)                                           ; wait for HotS to be the active window
Sleep(1000)                                                         ; wait 1 second before starting the timer
SoundBeep(261, 100)                                                 ; (1) low-high beep to indicate key scanning
SoundBeep(523, 100)                                                 ; (2) low-high beep to indicate key scanning

; hotkey configuration
HotIfWinActive(windowName)                                          ; only register hotkeys if HotS is active
Hotkey(mapKey, MapKeys)                                             ; register the map key
Hotkey(pauseKey, PauseScript)                                       ; register the pause key
Hotkey(resetKey, ResetHotkeys)                                      ; register the reset key

;functions
MapKeys(ThisHotKey) {
    if !WinExist(windowName) {                                      ; exit if the window has been closed
        SoundBeep 523, 100                                          ; (1) high-low beep to indicate WASD scanning
        SoundBeep 261, 100                                          ; (2) high-low beep to indicate WASD scanning
        ExitApp                                                     ; exit the script
    }
    if WinActive(windowName) and !isPaused  {                       ; confirm HotS is active and the script is not paused
        SoundBeep 523, 100                                          ; (1) double-high beep to indicate key mapping
        SoundBeep 523, 100                                          ; (2) double-high beep to indicate key mapping
        ih := InputHook("L1")                                       ; read the next key
        ih.Start()                                                  ; start reading keys
        ih.Wait()                                                   ; wait for a key press
        Hotkey(ih.Input, ToggleKey)                                 ; register the key as togglable
        ih.Stop()                                                   ; stop reading keys
        mappedKeys[ih.Input] := 0                                   ; add the key to the array of mapped keys
        SoundBeep 523, 100                                          ; (1) double-high beep to indicate key mapping successful
        SoundBeep 523, 100                                          ; (2) double-high beep to indicate key mapping successful

    }
}
PauseScript(ThisHotKey) {
    if !WinExist(windowName) {                                      ; exit if the window has been closed
        SoundBeep 523, 100                                          ; (1) high-low beep to indicate WASD scanning
        SoundBeep 261, 100                                          ; (2) high-low beep to indicate WASD scanning
        ExitApp                                                     ; exit the script
    }
    global isPaused := !isPaused                                    ; toggle the pause state
    if WinActive(windowName) and isPaused {                         ; confirm HotS is active and the script is paused
        For key in mappedKeys {                                     ; loop through the mapped keys
            if GetKeyState(key) {                                   ; check if the key was toggled
                Send("{" key " up}")                                ; release the key if so
            }
        }
    }
    SoundBeep 523, 200                                              ; long-high beep to indicate script pause state
}
ResetHotkeys(ThisHotKey) {
    if !WinExist(windowName) {                                      ; exit if the window has been closed
        SoundBeep 523, 100                                          ; (1) high-low beep to indicate WASD scanning
        SoundBeep 261, 100                                          ; (2) high-low beep to indicate WASD scanning
        ExitApp                                                     ; exit the script
    }
    if WinActive(windowName) and !isPaused  {                       ; confirm HotS is active and the script is not paused
        For key in mappedKeys {                                     ; loop through the mapped keys
            if GetKeyState(key) {                                   ; check if the key was toggled
                Send("{" key " up}")                                ; release the key if so
            }
        }
        Reload                                                      ; reload the script
        SoundBeep 523, 100                                          ; (1) low-low beep to indicate reload failed
        SoundBeep 261, 100                                          ; (2) low-low beep to indicate reload failed
    }
}
ToggleKey(ThisHotKey) {
    if !WinExist(windowName) {                                      ; exit if the window has been closed
        SoundBeep 523, 100                                          ; (1) high-low beep to indicate WASD scanning
        SoundBeep 261, 100                                          ; (2) high-low beep to indicate WASD scanning
        ExitApp                                                     ; exit the script
    }
    if WinActive(windowName) {                                      ; confirm HotS is active
        isPaused ?  Send(ThisHotKey) :                              ; press the mapped key as normal if the script is paused
            GetKeyState(ThisHotKey) ? Send("{" ThisHotKey " up}") : ; release the key if it is down
                Send("{" ThisHotKey " down}")                       ; press the key if it is up
    }
}
