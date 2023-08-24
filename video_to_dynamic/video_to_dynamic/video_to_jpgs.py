import cv2
import os

def video_to_jpgs(video_path):
    # Directory to save frames
    output_dir = 'frames_output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the video using OpenCV
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Couldn't open the video file.")
        exit()

    # Read the frames one by one and save them as JPEG
    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Construct the frame name
        frame_name = os.path.join(output_dir, f'frame_{frame_number:04d}.jpg')
        
        # Save the frame as a JPEG file
        cv2.imwrite(frame_name, frame)
        
        frame_number += 1

    # Release the video capture object
    cap.release()
    print(f"Extracted {frame_number} frames and saved in {output_dir}")