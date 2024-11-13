import RPi.GPIO as GPIO
import time

buzzer_pin = 4
led_pin = 5
touch_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(touch_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

# Seven Nation Army rhythm pattern
# Each note is represented by its duration in seconds
# Quarter note = 0.5 seconds (120 BPM)
rhythm_pattern = [
    0.5,    # E (quarter note)
    0.5,    # E (quarter note)
    0.25,   # G (eighth note)
    0.25,   # E (eighth note)
    0.5,    # D (quarter note)
    0.5,    # C (quarter note)
    1.0     # B (half note)
]

def play_rhythm():
    """Play one cycle of Seven Nation Army riff"""
    for duration in rhythm_pattern:
        GPIO.output(buzzer_pin, GPIO.HIGH)
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(duration * 0.8)  # On time (increased from 0.6 for more sustained notes)
        GPIO.output(buzzer_pin, GPIO.LOW)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(duration * 0.2)  # Off time (reduced for more sustained sound)

try:
    print("Seven Nation Army doorbell ready! Press Ctrl+C to exit")
    while True:
        if GPIO.input(touch_pin) == 1:
            play_rhythm()
        else:
            GPIO.output(buzzer_pin, GPIO.LOW)
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(0.1)  # Small delay to prevent CPU overload
            
except KeyboardInterrupt:
    print("\nProgram stopped by user")
    GPIO.cleanup()
except Exception as e:
    print(f"Error occurred: {e}")
    GPIO.cleanup()
