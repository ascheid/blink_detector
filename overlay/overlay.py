import cv2

def draw_overlay(frame, blink_count, alarm_status, blink_detected):
    """
    Draw an overlay on the frame with the blink count, alarm status, and blink detection.
    """
    cv2.putText(frame, f"Blink count: {blink_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, f"Alarm status: {'ON' if alarm_status else 'OFF'}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, f"Blink detected: {blink_detected}", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
