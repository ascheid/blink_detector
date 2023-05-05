import cv2
import dlib
import numpy as np


def detect_faces(frame):
    """
    Detect faces in the given frame.
    """
    detector = dlib.get_frontal_face_detector()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    return gray, faces

def track_blinks(gray, face_rect):
    """
    Track blinks in the given face data.
    """
    predictor = dlib.shape_predictor('blink_detector/shape_predictor_68_face_landmarks.dat')
    landmarks = predictor(gray, face_rect)
    points = np.zeros((68, 2), dtype=int)

    for i in range(0, 68):
        points[i] = (landmarks.part(i).x, landmarks.part(i).y)

    left_eye_ratio = eye_aspect_ratio(points[42:48])
    right_eye_ratio = eye_aspect_ratio(points[36:42])

    return (left_eye_ratio, right_eye_ratio)

def eye_aspect_ratio(eye_points):
    """
    Calculate the eye aspect ratio for given eye points.
    """
    A = np.linalg.norm(eye_points[1] - eye_points[5])
    B = np.linalg.norm(eye_points[2] - eye_points[4])
    C = np.linalg.norm(eye_points[0] - eye_points[3])

    ear = (A + B) / (2.0 * C)
    return ear
