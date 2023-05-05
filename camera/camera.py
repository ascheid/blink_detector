"""
This module contains functions related to camera operations.
"""
import cv2

def initialize_camera():
    """
    Initialize the camera.
    """
    cap = cv2.VideoCapture(0)
    return cap

def get_frame(cap):
    """
    Capture a single frame from the camera.
    """
    ret, frame = cap.read()
    return frame

def release_camera(cap):
    """
    Release the camera resources.
    """
    cap.release()
