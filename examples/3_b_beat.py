import RPi.GPIO as GPIO
import time

touch_pin = 5
buzzer_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(touch_pin, GPIO.IN)

# Define rhythm pattern (in seconds)
# 0.25 = sixteenth note, 0.5 = eighth note, 1 = quarter note
rhythm_pattern = [
    0.25, 0.25, 0.5,  # ♪♪♩
    0.25, 0.25, 0.5,  # ♪♪♩
    0.5, 0.5,         # ♩♩
    1.0               # 𝅗𝅥
]

def play_rhythm():
    """Play one cycle of the rhythm pattern"""
    for duration in rhythm_pattern:
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(duration * 0.6)  # On time
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(duration * 0.4)  # Off time (creates articulation)

try:
    print("Musical doorbell ready! Press Ctrl+C to exit")
    while True:
        if GPIO.input(touch_pin) == 1:
            play_rhythm()
        else:
            GPIO.output(buzzer_pin, GPIO.LOW)
            time.sleep(0.1)  # Small delay to prevent CPU overload
            
except KeyboardInterrupt:
    print("\nProgram stopped by user")
    GPIO.cleanup()
except Exception as e:
    print(f"Error occurred: {e}")
    GPIO.cleanup()
