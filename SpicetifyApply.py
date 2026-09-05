import subprocess
import time
import sys

def main():
    print("Applying Spicetify...")

    process = subprocess.Popen("spicetify backup apply", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    frames = ["/", "-", "\\", "|"]
    i = 0

    while process.poll() is None:
        print(f"Applying {frames[i % 4 ]}", end="\r")
        i += 1
        time.sleep(0.3)

        #Clearing the line
        print(" " * 20, end="\r")

    if process.returncode == 0:
        print("Spicetify applied")
    else:
        print("Spicetify failed to apply, trying to restore...")
        subprocess.run("spicetify restore backup", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run("spicetify apply", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Spicetify successfully restored and applied")

if __name__ == "__main__":
    main()