import cv2
import os

def video_to_jpgs_per_minute(video_path, output_dir, frames_per_minute):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the video's frames per second (fps) rate
    fps = int(video.get(cv2.CAP_PROP_FPS))
    
    # Calculate the interval (in terms of frames) at which to save frames
    interval = fps * 60 // frames_per_minute

    frame_num = 0
    saved_frame_count = 0

    while True:
        ret, frame = video.read()

        if not ret:
            break

        if frame_num % interval == 0:
            output_file = os.path.join(output_dir, f'frame_{saved_frame_count:04}.jpeg')
            cv2.imwrite(output_file, frame)
            saved_frame_count += 1

        frame_num += 1

    video.release()
