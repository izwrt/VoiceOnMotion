import serial
import subprocess

try:
    ser = serial.Serial('COM3', 9600)  # Change 'COM3' to the appropriate port
    motion_detected = False

    while True:
        data = ser.readline().decode().strip()
        if data == "motion detected":
            print("motion detected")
            voice_assistance_process = subprocess.Popen(["python", "voiceAssistance.py"])
            motion_detected = True
        else:
            print("No motion detected")
            voice_assistance_process.terminate()
            motion_detected = False

except serial.SerialException as e:
    print(f"Error: {e}")
finally:
    if ser.is_open:
        ser.close()
