# ALS Assistance Blink Detector

This project is designed to assist people with Amyotrophic Lateral Sclerosis (ALS) who have limited mobility and cannot use conventional methods to request assistance. The program uses a camera feed to detect and count the user's eye blinks, and when it detects 5 blinks within 5 seconds, it triggers an alarm to alert caregivers around or family members on telegram that the person needs help.

## How it works

The program utilizes computer vision techniques and facial landmark detection to monitor the user's eyes in real-time. When the user blinks 5 times within a 5-second interval, an alarm is activated to call for assistance. To turn off the alarm, the user needs to blink 5 times again within 5 seconds.

The algorithm calculates the Eye Aspect Ratio (EAR) to determine whether the eyes are open or closed. It uses the dlib library for face detection and facial landmark prediction, and OpenCV for video processing.

## Features

- Real-time eye blink detection.
- Alarm system which is triggered based on the frequency of blinks.
- Support for both live video feed and pre-recorded video.
- Alarm system can be toggled on or off by the user.
- Integrates with Telegram for remote monitoring.

## Dependencies

- Python 3
- OpenCV
- dlib
- imutils
- requests
- scipy

## Environment Variables

- `TELEGRAM_CHAT_ID`: Your Telegram Chat ID.
- `TELEGRAM_BOT_TOKEN`: Your Telegram Bot Token.

## Usage

1. Clone this repository.
2. Install the dependencies.
3. Set your environment variables.
4. Run the program: `python blink_detector.py --video camera --threshold 0.27 --frames 5`

### Arguments

- `-v` or `--video`: Path to input video file or "camera" for live video feed.
- `-t` or `--threshold`: Threshold to determine closed eyes. Default is 0.27.
- `-f` or `--frames`: The number of consecutive frames the eye must be below the threshold. Default is 5.

### Control

- Press `q` to quit the program.
- Press `s` to toggle the program enable.

### Alarm

The alarm is triggered when the user blinks more than 5 times in 5 seconds. To turn off the alarm, the user must blink 5 times in 5 seconds again. The alarm is played using the default system sound.

### Telegram

If `TELEGRAM_CHAT_ID` and `TELEGRAM_BOT_TOKEN` are set, the program will send photos and alerts to the specified Telegram chat when the alarm is triggered, stopped, or when the program is quit. The photos will show the state of the user's eyes at the time of the alert.

## Logging

Logs are saved to `blink_detector.log` and are also output to the console. The log level is set to DEBUG. The log file is rotated when it reaches 10mb, and the two most recent log files are kept.

