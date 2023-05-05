import cv2
from blink_detection.blink_detector import detect_faces, track_blinks
from camera.camera import initialize_camera, get_frame
from overlay.overlay import draw_overlay

BLINK_THRESHOLD = 0.3
SCALE_FACTOR = 0.5

def show_preview(blink_counter, alarm_sounding):
    """
    Show the video preview with integrated blink detection.
    """
    cap = initialize_camera()

    while True:
        frame = get_frame(cap)
        scaled_frame = cv2.resize(frame, (0, 0), fx=SCALE_FACTOR, fy=SCALE_FACTOR)
        gray, faces = detect_faces(scaled_frame)

        blink_detected = False
        for face in faces:
            left_eye_ratio, right_eye_ratio = track_blinks(gray, face)

            if left_eye_ratio > BLINK_THRESHOLD or right_eye_ratio > BLINK_THRESHOLD:
                blink_detected = True

        draw_overlay(scaled_frame, blink_counter.counter, alarm_sounding, blink_detected)
        cv2.imshow("Frame", scaled_frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
