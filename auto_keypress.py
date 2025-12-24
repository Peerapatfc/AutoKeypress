import pydirectinput
import keyboard
import time
import win32gui
import win32con

running = True

def stop_script():
    global running
    running = False
    print("\nStopping script...")

def find_window_by_partial_title(partial_title):
    target_hwnd = None
    def enum_windows_callback(hwnd, _):
        nonlocal target_hwnd
        title = win32gui.GetWindowText(hwnd)
        if partial_title.lower() in title.lower():
            target_hwnd = hwnd
            return False 
        return True
    try:
        win32gui.EnumWindows(enum_windows_callback, None)
    except:
        pass
    return target_hwnd

def main():
    global running
    
    print("Auto Keypress Script (Focus-Steal Mode)")
    print("---------------------------------------")
    print("This script will briefly focus eFootball, press Enter,")
    print("then return focus to your current window.")
    print("")
    print("  F10 = Stop script")
    print("---------------------------------------")
    
    target_title = "eFootball"
    game_hwnd = find_window_by_partial_title(target_title)
    
    if not game_hwnd:
        print(f"Error: Window containing '{target_title}' not found!")
        return
    
    print(f"Target found: '{win32gui.GetWindowText(game_hwnd)}'")
    print("Starting in 3 seconds...")
    
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    keyboard.add_hotkey('f10', stop_script)
    
    print("[RUNNING] Press F10 to stop.")
    
    try:
        while running:
            # Remember current foreground window
            current_hwnd = win32gui.GetForegroundWindow()
            
            # Briefly focus game
            try:
                win32gui.SetForegroundWindow(game_hwnd)
                time.sleep(0.05)  # Small delay to ensure focus
                
                # Press Enter
                pydirectinput.press('enter')
                
                time.sleep(0.05)
                
                # Restore previous window
                if current_hwnd and current_hwnd != game_hwnd:
                    win32gui.SetForegroundWindow(current_hwnd)
            except Exception as e:
                pass  # Window might be minimized, etc.
            
            time.sleep(1)
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        keyboard.unhook_all_hotkeys()
        print("Script finished.")

if __name__ == "__main__":
    main()
