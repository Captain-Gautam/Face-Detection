import serial

port = serial.Serial('/dev/ttyUSB0', 9600)

# while (port.isOpen()):
#     data = input("Enter 1 to ""ON"" the led and 0 to ""OFF"" the led: ")
#     if (data == '1'):
#         port.write('1')
#     elif (data == '0'):
#         port.write('0')
#     else:
#         print("Invalid Input")

while port.isOpen():
    data = input("Enter 1 to 'ON' the led and 0 to 'OFF' the led: ")
    if data == '1' or data == '0':
        port.write(data.encode())  # Convert string to bytes before sending
    else:
        print("Invalid Input")

        