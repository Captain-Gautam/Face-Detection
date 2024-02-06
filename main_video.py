# #==============Speak with blink=====================
# import cv2
# from simple_facerec import SimpleFacerec
# import pyttsx3
# import serial

# # Function to speak the name using TTS
# def speak_name(name):
#     engine = pyttsx3.init()
#     engine.say(f"Hello, {name}")
#     engine.runAndWait()

# # Initialize Serial communication with Arduino
# arduino_port = '/dev/ttyUSB0'  # Change this to the correct port
# arduino_baudrate = 9600
# arduino = serial.Serial(arduino_port, arduino_baudrate)

# # Encode faces from a folder
# sfr = SimpleFacerec()
# sfr.load_encoding_images("images/")

# # Load Camera
# cap = cv2.VideoCapture(0)

# prev_name = None  # Variable to store the previous name

# while True:
#     ret, frame = cap.read()

#     # Detect Faces
#     face_locations, face_names = sfr.detect_known_faces(frame)
#     for face_loc, name in zip(face_locations, face_names):
#         y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

#         cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

#         # Speak the name only if it's different from the previous name
#         if name != prev_name:
#             speak_name(name)
#             prev_name = name

#             # Send signal to Arduino for green LED
#             arduino.write(b'G')

#     # If no known face is detected, send signal for red LED
#     if not face_names:
#         arduino.write(b'R')

#     cv2.imshow("Frame", frame)

#     key = cv2.waitKey(1)
#     if key == 13:
#         break

# cap.release()
# cv2.destroyAllWindows()

# #===========Intial Code==================
# import cv2
# from simple_facerec import SimpleFacerec

# # Encode faces from a folder
# sfr = SimpleFacerec()
# sfr.load_encoding_images("images/")

# # Load Camera
# cap = cv2.VideoCapture(0)


# while True:
#     ret, frame = cap.read()

#     # Detect Faces
#     face_locations, face_names = sfr.detect_known_faces(frame)
#     for face_loc, name in zip(face_locations, face_names):
#         y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

#         cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

#     cv2.imshow("Frame", frame)

#     key = cv2.waitKey(1)
#     if key == 13:
#         break

# cap.release()
# cv2.destroyAllWindows()


# #=============With GTTS code==================
# import cv2
# from simple_facerec import SimpleFacerec
# from gtts import gTTS
# import os

# # Function to speak the name using gTTS
# def speak_name(name):
#     text_to_speech = gTTS(f"Hello, {name}", lang='en', tld='co.in')
#     text_to_speech.save("temp.mp3")
#     os.system("mpg321 temp.mp3")  # You may need to install mpg321 or use another player

# # Encode faces from a folder
# sfr = SimpleFacerec()
# sfr.load_encoding_images("images/")

# # Load Camera
# cap = cv2.VideoCapture(0)

# prev_name = None  # Variable to store the previous name

# while True:
#     ret, frame = cap.read()

#     # Detect Faces
#     face_locations, face_names = sfr.detect_known_faces(frame)
#     for face_loc, name in zip(face_locations, face_names):
#         y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

#         cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

#         # Speak the name only if it's different from the previous name
#         if name != prev_name:
#             speak_name(name)
#             prev_name = name

#     cv2.imshow("Frame", frame)

#     key = cv2.waitKey(1)
#     if key == 13:
#         break

# cap.release()
# cv2.destroyAllWindows()

# #===========With display and speak============
import cv2
from simple_facerec import SimpleFacerec
from gtts import gTTS
import os
import serial
import time

# Function to speak the name using gTTS
def speak_name(name):
    text_to_speech = gTTS(f"Hello, {name}", lang='en', tld='co.in')
    text_to_speech.save("temp.mp3")
    os.system("mpg321 temp.mp3")  # You may need to install mpg321 or use another player

# Function to send data to Arduino Uno through serial
def send_to_arduino(name):
    #data = data.ljust(16)[:16]
    arduino_serial.write(name.encode())

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

prev_name = None  # Variable to store the previous name

# Initialize serial communication with Arduino Uno
arduino_serial = serial.Serial('/dev/ttyUSB0', 9600)  # Change 'COM3' to your Arduino port

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        # Speak the name only if it's different from the previous name
        if name != prev_name:
            speak_name(name)
            send_to_arduino(name)  # Send the name to Arduino for display
            prev_name = name

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 13:
        break

cap.release()
cv2.destroyAllWindows()



