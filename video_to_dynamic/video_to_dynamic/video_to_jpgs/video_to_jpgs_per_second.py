import cv2
import os

def video_to_jpgs_per_second(video_path, output_dir, fps_to_extract):
     # Check if the output directory exists, if not create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the video using OpenCV
    cap = cv2.VideoCapture(video_path)

    # Get the actual FPS of the video
    video_fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Calculate the frame skip rate to meet the desired extraction FPS
    frame_skip = video_fps // fps_to_extract

    # Ensure that the skip rate is at least 1
    if frame_skip < 1:
        frame_skip = 1
        fps_to_extract = video_fps
        print(f"Warning: Video FPS ({video_fps}) is less than the desired extraction FPS. Setting extraction FPS to {video_fps}.")

    print(f"Extracting every {frame_skip} frame to get {fps_to_extract} FPS...")

    frame_num = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_num % frame_skip == 0:
            output_filename = os.path.join(output_dir, f"frame_{frame_num:04}.jpg")
            cv2.imwrite(output_filename, frame)
            print(f"Written {output_filename}")

        frame_num += 1

    cap.release()
    print("Extraction finished.")


