import serial
import subprocess

ser = serial.Serial('COM3', 9600)  # Change 'COM3' to the appropriate port
motion_detected = False

while True:
    data = ser.readline().decode().strip()
    if data == "Hy there":
            print("motion detected")
            subprocess.run(["python", "voiceAssistance.py"])
            motion_detected = True
    else:
            print("No motion detected")
            motion_detected = False
            ser.close()
