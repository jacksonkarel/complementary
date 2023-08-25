import os
from video_to_dynamic.video_to_jpgs.video_to_jpgs_per_minute import video_to_jpgs_per_minute
from video_to_dynamic.jpg_to_dynamic.jpg_to_dynamic import jpg_to_dynamic
from video_to_dynamic.extact_emotions import extract_emotions

def video_to_dynamic():
    # Path to the video
    video_path = "[FULL] Uncut video of Cavaliers' bench before, during and after JR Smith's Game 1 blunder _ ESPN.mp4"

    jpg_dir = "frames_output"

    file_timestamps = video_to_jpgs_per_minute(video_path, jpg_dir, 12)


    with os.scandir(jpg_dir) as entries:
        for entry in entries:
            response_content = jpg_to_dynamic(entry.path)
            emotions = extract_emotions(response_content)
            timestamp = file_timestamps[entry.path]
            print(f"{timestamp}: {emotions}")

    
