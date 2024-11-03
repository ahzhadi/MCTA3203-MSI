import serial
import time

# Set up serial connection (use the correct COM port or tty)
# For example, COM3 on Windows or '/dev/ttyACM0' on Linux/Mac
ser = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)  # Allow time for Arduino to reset

try:
    while True:
        if ser.in_waiting > 0:  # Check if there's data from Arduino
            data = ser.readline().decode('utf-8').strip()  # Read and decode data
            if data:
                print(data)  # Print the potentiometer and servo angle values

        # Check for user input to send the stop command to Arduino
        user_input = input("Enter 's' to stop servo control: ").strip().lower()
        if user_input == 's':
            ser.write(b's')  # Send stop command to Arduino
            print("Stop command sent to Arduino.")
            break

finally:
    ser.close()  # Close the serial connection
