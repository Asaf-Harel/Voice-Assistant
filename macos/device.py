import subprocess
import os
from speech import get_voice


def set_volume(volume: int):
    """Set the speakers volume

    Args:
        volume (int): The volume level (0-100)
    """
    subprocess.call(
        [f"osascript -e 'set volume output volume {volume}'"], shell=True)


def get_volume() -> int:
    """Get the current volume level

    Returns:
        int: The current volume level
    """
    command = subprocess.run(
        "osascript -e 'get volume settings'", stdout=subprocess.PIPE, shell=True)

    volume = int(command.stdout.strip().decode(
        'ascii').split(',')[0].split(':')[1])

    return volume


def set_brightness(brightness):
    subprocess.call(["brightness", str(brightness)])


def get_brightness() -> float:
    """Get the current brightness

    Returns:
        float: The current brightness level (0-1)
    """
    command = subprocess.run(
        "brightness -l", stdout=subprocess.PIPE, shell=True)

    brightness = float(command.stdout.decode(
        "ascii").split('brightness')[1].strip())

    return brightness


def turn_wifi(state: bool):
    """Turn on and off WiFi

    Args:
        state (bool): True to turn on and False to turn off
    """
    if state:
        subprocess.call(["networksetup", "-setairportpower",
                         "airport", "on"], stdout=subprocess.PIPE)
        notify("Turned On WiFi")
    else:
        subprocess.call(["networksetup", "-setairportpower",
                         "airport", "off"], stdout=subprocess.PIPE)
        notify("Turned Off WiFi")


def turn_bluetooth(state: bool):
    """Turn on and off bluetooth

    Args:
        state (bool): True to turn on and False to turn off
    """
    if state:
        subprocess.call(["blueutil", "-p", "1"])
        notify("Turned On Bluetooth")

    else:
        subprocess.call(["blueutil", "-p", "0"])
        notify("Turned Off Bluetooth")


def notify(title="", subtitle="", msg="", sound=None, url=None):
    if get_voice() == "Jarvis":
        icon = "icons/jarvis-icon.png"
    elif get_voice() == "Friday":
        icon = "icons/friday-icon.png"

    if sound and url:
        subprocess.call(["terminal-notifier", "-title",
                         f'"{title}"', "-subtitle", f'"{subtitle}"', "-message", f'"{msg}"', "-appIcon", icon, "-sound", sound, "-open", f'"{url}"'])
    elif sound:
        subprocess.call(["terminal-notifier", "-title",
                         f'"{title}"', "-subtitle", f'"{subtitle}"', "-message", f'"{msg}"', "-appIcon", icon, "-sound", sound])
    elif url:
        subprocess.call(["terminal-notifier", "-title",
                         f'"{title}"', "-subtitle", f'"{subtitle}"', "-message", f'"{msg}"', "-appIcon", icon, "-open", f'"{url}"'])
    else:
        subprocess.call(["terminal-notifier", "-title",
                         f'"{title}"', "-subtitle", f'"{subtitle}"', "-message", f'"{msg}"', "-appIcon", icon])


def open_app(app_name):
    subprocess.call(['open', f'/Applications/{app_name}'])


def hide(app_name):
    os.system(
        f"""osascript -e 'tell application "System Events" to set visible of process "{app_name}" to false'""")


def quit(app_name):
    subprocess.call(['pkill', app_name])
