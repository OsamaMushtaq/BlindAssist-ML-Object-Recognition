"""
BlindAssist Main Controller
Integrates object detection, obstacle sensing, GPS, speech feedback,
and emergency alerts.
"""

from object_detection.detector import detect_objects
from obstacle_detection.ultrasonic import detect_obstacle
from navigation.gps_tracker import get_location
from speech_feedback.tts import speak
from emergency.gsm_alert import send_emergency_alert

def main():
    speak("BlindAssist system initialized.")

    obstacle_distance = detect_obstacle()
    if obstacle_distance:
        speak(f"Obstacle detected at {obstacle_distance} centimeters")

    detected_objects = detect_objects()
    if detected_objects:
        for obj in detected_objects:
            speak(f"Detected {obj}")

    location = get_location()
    if location:
        speak(f"Current location latitude {location[0]} longitude {location[1]}")

if __name__ == "__main__":
    main()
