import cv2
import sys
from random import randint

tracker_type = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']

# for i in range(len(tracker_type)):
tracker_type = tracker_type[6]
# print(tracker_type)

if tracker_type == 'BOOSTING':
	tracker = cv2.legacy.TrackerBoosting_create()
elif tracker_type == 'MIL':
	tracker = cv2.legacy.TrackerMIL_create()
elif tracker_type == 'KCF':
	tracker = cv2.legacy.TrackerKCF_create()
elif tracker_type == 'TLD':
	tracker = cv2.legacy.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
	tracker = cv2.legacy.TrackerMedianFlow_create()
elif tracker_type == 'MOSSE':
	tracker = cv2.legacy.TrackerMOSSE_create()
elif tracker_type == 'CSRT':
	tracker = cv2.legacy.TrackerCSRT_create()


# print(tracker)

# loading the video file
video = cv2.VideoCapture('Videos/race.mp4')
if not video.isOpened():
	print('Error While loading the Video!')
	sys.exit()

# loading the first frame of video
ok, frame = video.read()
if not ok:
	print('Error loading the first frame of video')
	sys.exit()


bbox = cv2.selectROI(frame)
print(bbox)


ok = tracker.init(frame, bbox)
print(ok)

colors = (randint(0, 255), randint(0, 255), randint(0, 255))
print(colors)


while True:
	ok, frame = video.read()
	if not ok:
		break;
	ok, bbox = tracker.update(frame)
	# print(ok, bbox)
	if ok == True:
		(x, y, w, h) = [int(v) for v in bbox]
		cv2.rectangle(frame, (x, y), (x + w, y + h), colors, 2, 1)
	else:
		cv2.putText(frame, 'Tracking Fail', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0,0,255), 2)

	cv2.imshow('Tracking', frame)
	if cv2.waitKey(1) & 0XFF == 27:
		break
