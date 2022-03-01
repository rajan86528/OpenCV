import cv2

# cap = cv2.VideoCapture(0)

# Playing Webcam video
"""while True:
    ret_, frame = cap.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()"""

# Capture Video Using OpenCv

"""if cap.isOpened() == 'False':
    print('Camera Could not open')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Video coded

video_coded = cv2.VideoWriter_fourcc(*'XVID')
video_output = cv2.VideoWriter('Capture.mp4', video_coded, 0, (frame_width, frame_height)) 

while True:
    ret_, frame = cap.read()
    if ret_ == True:
        video_output.write(frame)
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
video_output.release()
cv2.destroyAllWindows()"""

# Play Vidoe from file
cap = cv2.VideoCapture('Capture.mp4')

while True:
    ret_, frame = cap.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()