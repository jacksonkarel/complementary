import os
from video_to_dynamic.video_to_jpgs import video_to_jpgs
from video_to_dynamic.jpg_to_dynamic import jpg_to_dynamic

def video_to_dynamic():
    # # Path to the video
    # video_path = "[FULL] Uncut video of Cavaliers' bench before, during and after JR Smith's Game 1 blunder _ ESPN.mp4"

    # video_to_jpgs(video_path)

    # jpg_dir = "frames_output"
    jpg_dir = "scoutr_imgs"

    with os.scandir(jpg_dir) as entries:
        for entry in entries:
            jpg_to_dynamic(entry.path)
    
