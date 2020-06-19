import subprocess


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
    else:
        subprocess.call(["networksetup", "-setairportpower",
                         "airport", "off"], stdout=subprocess.PIPE)


def check_ethernet():
    command = subprocess.run("ifconfig", stdout=subprocess.PIPE, shell=True)
    text = command.stdout.strip().decode("ascii")
    print(text)


def turn_bluetooth(state: bool):
    """Turn on and off bluetooth

    Args:
        state (bool): True to turn on and False to turn off
    """
    if state:
        subprocess.call(["blueutil", "-p", "1"])
    else:
        subprocess.call(["blueutil", "-p", "0"])


check_ethernet()
