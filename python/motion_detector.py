import serial

ser = serial.Serial('COM3', 9600)  # Change 'COM3' to the appropriate port
motion_detected = False

while True:
    data = ser.readline().decode().strip()
    if data == "Hy there":
            print("Hmotion detected")
            motion_detected = True
    else:
            print("No motion detected")
            motion_detected = False
