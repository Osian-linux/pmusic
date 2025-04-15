import subprocess


def music():
    try:
        title = subprocess.check_output(["playerctl", "metadata", "title"], stderr=subprocess.DEVNULL).decode().strip()
        artist = subprocess.check_output(["playerctl", "metadata", "artist"], stderr=subprocess.DEVNULL).decode().strip()
        return f"{artist} - {title}" if title else ""
    except subprocess.CalledProcessError:
        return ""

print(music())
