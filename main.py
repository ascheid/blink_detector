import cv2
import time
import threading
from camera.camera import initialize_camera, get_frame, release_camera
from blink_detection.blink_detector import detect_faces, track_blinks
from blink_detection.blink_counter import BlinkCounter
from alarm.alarm import sound_alarm, stop_alarm
from overlay.preview import show_preview

BLINK_THRESHOLD = 0.25
BLINKS_REQUIRED = 5
TIME_WINDOW = 5
SCALE_FACTOR = 0.4


BLINK_THRESHOLD = 0.3
BLINKS_REQUIRED = 5
TIME_WINDOW = 5

def main():
    """
    Main function that runs the blink detection and alarm system.
    """
    cap = initialize_camera()
    blink_counter = BlinkCounter()
    alarm_sounding = False
    start_time = time.time()

    while True:
        frame = get_frame(cap)
        gray, faces = detect_faces(frame)

        for face in faces:
            left_eye_ratio, right_eye_ratio = track_blinks(gray, face)

            if left_eye_ratio > BLINK_THRESHOLD or right_eye_ratio > BLINK_THRESHOLD:
                blink_counter.increment_counter()
                start_time = time.time()

            if blink_counter.check_blink_threshold(BLINKS_REQUIRED):
                time_elapsed = time.time() - start_time
                if time_elapsed <= TIME_WINDOW:
                    if not alarm_sounding:
                        sound_alarm()
                        alarm_sounding = True
                else:
                    blink_counter.reset_counter()

        show_preview(blink_counter, alarm_sounding)
        
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        elif key == ord("s"):
            if alarm_sounding:
                stop_alarm()
                alarm_sounding = False

    release_camera(cap)

if __name__ == "__main__":
    main()