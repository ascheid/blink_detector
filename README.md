# ALS Assistance Blink Detector

This project is designed to assist people with Amyotrophic Lateral Sclerosis (ALS) who have limited mobility and cannot use conventional methods to request assistance. The program uses a camera feed to detect and count the user's eye blinks, and when it detects 5 blinks within 5 seconds, it triggers an alarm to alert caregivers or family members that the person needs help.

## How it works

The program utilizes computer vision techniques and facial landmark detection to monitor the user's eyes in real-time. When the user blinks 5 times within a 5-second interval, an alarm is activated to call for assistance. To turn off the alarm, the user needs to blink 5 times again within 5 seconds.

The algorithm calculates the Eye Aspect Ratio (EAR) to determine whether the eyes are open or closed. It uses the dlib library for face detection and facial landmark prediction, and OpenCV for video processing.

## Requirements

- Python 3.6+
- OpenCV
- dlib
- imutils
- scipy

## Usage

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the program with the command `python blink_detector.py`.

You can customize the blink threshold and the number of consecutive frames the eyes must be closed for by modifying the `--threshold` and `--frames` command-line arguments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
