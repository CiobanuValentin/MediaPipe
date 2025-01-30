import cv2
import mediapipe as mp
import csv
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Load video file
video_path = "about.mp4"  # Change to your video path
cap = cv2.VideoCapture(video_path)

# Define output CSV file
csv_filename = "hand_landmarks.csv"
csv_file = open(csv_filename, "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["frame", "hand", "landmark", "x", "y", "z"])

# Get video properties for output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define video output
output_video_path = "output_with_landmarks.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Process the video frame by frame
with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5) as hands:
    frame_idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        # Convert the BGR frame to RGB (required by MediaPipe)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                for landmark_idx, landmark in enumerate(hand_landmarks.landmark):
                    csv_writer.writerow([
                        frame_idx, hand_idx, landmark_idx,
                        landmark.x, landmark.y, landmark.z
                    ])

                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

        # Write the frame with landmarks to the output video
        out.write(frame)
        frame_idx += 1

# Release video and close CSV
cap.release()
out.release()
csv_file.close()
print(f"Landmark data saved to {csv_filename}")
print(f"Video with landmarks saved as {output_video_path}")
