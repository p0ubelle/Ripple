import subprocess

def launch_riot_client():
    riot_client_path = r"C:\Riot Games\Riot Client\RiotClientServices.exe"

    try:
        subprocess.Popen([riot_client_path, "--launch-product=league_of_legends", "--launch-patchline=live"], shell=True)
    except FileNotFoundError:
        print("Error: Riot Client executable not found!")

