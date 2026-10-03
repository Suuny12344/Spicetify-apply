import subprocess
import time
import sys

def main():
    print("Applying Spicetify...")

    process = subprocess.Popen("spicetify backup apply", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    frames = ["/", "-", "\\", "|"]
    i = 0

    while process.poll() is None:
        print(f"Applying {frames[i % 4]}", end="\r")
        i += 1
        time.sleep(0.3)

    # Clearing the line
    print(" " * 20, end="\r")

    if process.returncode == 0:
        print("Spicetify applied")
    else:
        print("Spicetify failed to apply, trying to restore...")
        restore = subprocess.run("spicetify restore backup", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        apply = subprocess.run("spicetify apply", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if restore.returncode == 0 and apply.returncode == 0:
            print("Spicetify successfully restored and applied")
        else:
            print("Spicetify failed to restore and apply, trying to update...")
            update = subprocess.run("spicetify update", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            reapply = subprocess.run("spicetify backup apply", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            if update.returncode == 0 and reapply.returncode == 0:
                print("Spicetify successfully updated and applied")
            else:
                print("Spicetify failed to apply, check your Spotify installation!")

if __name__ == "__main__":
    main()
