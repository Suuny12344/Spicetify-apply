import os
import shutil
import subprocess
import time

if os.name == "nt":
    os.system("")  # aktiviert ANSI-Farben in der Windows-Konsole

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def main():
    if shutil.which("spicetify") is None:
        print(f"{RED}spicetify was not found in PATH, is it installed?{RESET}")
        return

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
        print(f"{GREEN}Spicetify applied{RESET}")
    else:
        print(f"{RED}Spicetify failed to apply, trying to restore...{RESET}")
        restore = subprocess.run("spicetify restore backup", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        apply = subprocess.run("spicetify apply", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if restore.returncode == 0 and apply.returncode == 0:
            print(f"{GREEN}Spicetify successfully restored and applied{RESET}")
        else:
            print(f"{RED}Spicetify failed to restore and apply, trying to update...{RESET}")
            update = subprocess.run("spicetify update", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            reapply = subprocess.run("spicetify backup apply", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            if update.returncode == 0 and reapply.returncode == 0:
                print(f"{GREEN}Spicetify successfully updated and applied{RESET}")
            else:
                print(f"{RED}Spicetify failed to apply, check your Spotify installation!{RESET}")

if __name__ == "__main__":
    main()
