
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

# #==========For Display with GTTS=========
import cv2
from simple_facerec import SimpleFacerec
from gtts import gTTS
import os
import tkinter as tk
from tkinter import messagebox
from pyfiglet import Figlet

# Function to speak the known name using gTTS
def speak_name(name):
    text_to_speech = gTTS(f"Hello, {name}", lang='en', tld='co.in')
    text_to_speech.save("temp.mp3")
    os.system("mpg321 temp.mp3")  # You may need to install mpg321 or use another player

# Function to speak the unknown name using gTTS
def speak_unknown_name():
    text_to_speech = gTTS(f"Hello, My Friend, Welcome to SSIT ", lang='en', tld='co.in')
    text_to_speech.save("unknown.mp3")
    os.system("mpg321 unknown.mp3")  # You may need to install mpg321 or use another player

# Function to create a tkinter window to open the known face to display the name
def create_window(name):
    window = tk.Tk()
    window.geometry("1360x688+0+0")
    window.title("Recognition Window")
    window.configure(bg="black")

    figlet = Figlet(font='slant')
    ascii_text = figlet.renderText(f"Hello, {name} \nWelcome to\nS. S. I. T.")

    label = tk.Label(window, text=ascii_text, font=("Courier", 20), fg="white", bg="black", justify=tk.LEFT)
    label.pack(padx=20, pady=20)

    window.after(3000, window.destroy)

    window.mainloop()

# Function for unknown person to have the menu
def window_unknown():
    def show_description(choice):
        descriptions = {
            1: "Prof. Niraj Sir",
            2: "Prof. Dharmesh Sir",
            3: "Prof. Hitesh Sir",
            4: "Dr. Ramesh Sir(IT Dep.)\nProf. Darshan Sir(CE Dep.)",
            5: "Gautam Prajapati"
        }

        description_window = tk.Toplevel(root)
        description_window.title(f"Choice {choice} Description")

        label = tk.Label(description_window, text=descriptions[choice], font=("Courier", 14))
        label.pack(padx=20, pady=20)

    # Function to handle the choice selection
    def handle_choice():
        try:
            choice = int(entry.get())
            if 1 <= choice <= 5:
                show_description(choice)
            else:
                messagebox.showwarning("Invalid Choice", "Please enter a valid choice between 1 and 7.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a numeric value.")
    # Create the main window
    root = tk.Tk()
    root.geometry("1360x688+0+0")
    root.title("Choice Description App")
    root.configure(bg = "black")





    # Add widgets to the main window
    menu = "1.Addmission Process Faculty Detail \n2.Director Sir Details\n3.Principal Details\n4.HOD'sDetails\n5.Admin Contact"
    label = tk.Label(root, text=menu, font=("Courier", 14))
    label.pack(padx=20, pady=20)

    entry = tk.Entry(root, font=("Courier", 14))
    entry.pack(padx=20, pady=20)

    button = tk.Button(root, text="Show Description", command=handle_choice, font=("Courier", 14))
    button.pack(padx=20, pady=20)
    
    root.after(5000, root.destroy)
    # Start the Tkinter event loop
    root.mainloop()

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

prev_name = None  # Variable to store the previous name

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
            if name != "Unknown":
                speak_name(name)
                create_window(name)
            else:
                speak_unknown_name()
                window_unknown()
            prev_name = name
        # if name != "Unknown":
        #     speak_name(name)
        #     create_window(name)
        # else:
        #     window_unknown()
        # prev_name = name


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 13:
        break

cap.release()
cv2.destroyAllWindows()
















