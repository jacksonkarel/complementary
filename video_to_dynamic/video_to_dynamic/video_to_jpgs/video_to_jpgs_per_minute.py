import cv2
import os

def video_to_jpgs_per_minute(video_path, output_folder, frames_per_minute):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Couldn't open the video file.")
        return
    
    # Get the total number of frames and the FPS (frames per second) of the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Calculate the interval (in frames) at which to save frames based on the desired frames per minute
    frames_per_second = frames_per_minute / 60
    interval = int(fps / frames_per_second)
    
    output_files_dict = {}

    frame_no = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_no % interval == 0:
            # Calculate the timestamp for the current frame
            time_in_seconds = frame_no / fps
            timestamp = "{:.2f}".format(time_in_seconds)
            
            # Construct the output path
            output_path = os.path.join(output_folder, f"frame_{frame_no}.jpg")
            
            # Save the frame
            cv2.imwrite(output_path, frame)
            
            # Update the dictionary
            output_files_dict[output_path] = timestamp

        frame_no += 1

    # Release the video capture object
    cap.release()

    return output_files_dict