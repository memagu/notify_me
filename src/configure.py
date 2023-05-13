import winreg

from constants import APP_NAME, PROJECT_ROOT, WINREG_SUB_KEY


def toggle_autostart() -> None:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, WINREG_SUB_KEY, 0, winreg.KEY_ALL_ACCESS) as key:
        if APP_NAME in (winreg.EnumValue(key, i)[0] for i in range(0, winreg.QueryInfoKey(key)[1])):
            winreg.DeleteValue(key, APP_NAME)
            return

        winreg.SetValueEx(
            key,
            APP_NAME,
            0,
            1,
            fr'"{PROJECT_ROOT / "venv/Scripts/pythonw"}" "{PROJECT_ROOT / "src/notify.py"}"'
        )
