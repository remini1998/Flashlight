on run argv
    set device_name to item 1 of argv
    set action_name to item 2 of argv
    tell application "System Events"
        tell process "SystemUIServer"
            tell (menu bar item 1 of menu bar 1 where description is "bluetooth")
                click
                if menu item device_name of menu 1 exists then
                    tell (menu item device_name of menu 1)
                        click
                        set menu_name to name of menu item 1 of menu 1
                        if action_name is "Toggle" or action_name is menu_name then
                            click menu item 1 of menu 1
                        else
                            key code 53
                        end if
                    end tell
                else
                    key code 53
                end if
            end tell
        end tell
    end tell
end run