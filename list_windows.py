import win32gui

def enum_handler(hwnd, results):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        if title:
            results.append(title)

results = []
win32gui.EnumWindows(enum_handler, results)

print("Visible Windows:")
for title in results:
    print(f"- {title}")
