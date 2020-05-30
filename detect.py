# import cv2 and numpy

import cv2
import os
import numpy as np

size = (400, 520)

# capturing video
# video_path = os.path.join("src", "hand.mp4")
video_path = 0

if video_path == 0:
    size = (640, 480)

cap = cv2.VideoCapture(video_path)

fps = int(cap.get(cv2.CAP_PROP_FPS))
print("The webcam fps is: " + str(fps))
# reading back-to-back frames(images) from video
def capture_frame(cap, size):
    ret, frame1 = cap.read()
    if not ret:
        return ret, None
    frame1 = cv2.resize(frame1, size)

    return ret, frame1


ret, frame1 = capture_frame(cap, size)
ret, frame2 = capture_frame(cap, size)

frame_num = 2

past_detect = False

start_time = 0

in_move = False

history = [0]
while cap.isOpened():
    seconds = round((frame_num / fps), 1)

    # Difference between frame1(image) and frame2(image)
    diff = cv2.absdiff(frame1, frame2)

    # Converting color image to gray_scale image
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Converting gray scale image to GaussianBlur, so that change can be find easily
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # If pixel value is greater than 20, it is assigned white(255) otherwise black
    _, thresh = cv2.threshold(blur, 30, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=4)

    # finding contours of moving object
    contours, hirarchy = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    elapsed_time = seconds - start_time
    # print(elapsed_time)
    # making rectangle around moving object
    detected = False

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 2000:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 20), 2)
        # print("Movement detected at: " + str(seconds) + " seconds.")
        detected = True

        if not (past_detect):

            if elapsed_time > 2:

                if not (in_move):
                    in_move = True
                    start_time = seconds

                    print("Movement started at: " + str(seconds) + " seconds.")

                    # calculate early so no instant shutoff
                    elapsed_time = seconds - start_time
    # no detection in history
    if not (True in history):
        if in_move:
            if elapsed_time > 0.5:
                print("Movement ended at: " + str(seconds) + " seconds.")
                in_move = False
    history.append(detected)
    if len(history) > 7:
        history.pop(0)

    # print(history)

    past_detect = detected

    drawn_thresh = cv2.add(frame1, frame1, mask=thresh)
    # Display original frame
    # cv2.imshow("Motion Detector", frame1)

    # Display Diffrenciate Frame
    # cv2.imshow("Difference Frame", thresh)
    both = np.concatenate((frame1, drawn_thresh), axis=0)
    both = cv2.resize(both, (0, 0), fx=0.8, fy=0.8)
    cv2.imshow("Detected", both)

    # Assign frame2(image) to frame1(image)
    frame1 = frame2

    # Read new frame2
    ret, frame2 = capture_frame(cap, size)
    frame_num += 1

    if not ret:
        break

    # Press 'esc' for quit
    key = cv2.waitKey(1)
    if key == ord("q") or key == 27:
        break

# Release cap resource
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
