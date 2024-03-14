import tkinter as tk
from tkinter import Label, ttk, messagebox, Text, Scrollbar
from PIL import Image, ImageTk

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x688+0+0")
        self.root.title("SSIT Information Center")
        self.root.config(bg='#282b30')

        # Logo
        default_logo = Image.open(r"images/ssit_logo2.jpg")
        default_logo = default_logo.resize((140, 100), Image.BICUBIC)
        self.default_photoimg = ImageTk.PhotoImage(default_logo)

        first_label = Label(self.root, image=self.default_photoimg)
        first_label.place(x=0, y=0, width=140, height=100)

        # Title Of Institute
        default_college_name = "SHREE SWAMINARAYAN INSTITUTE OF TECHNOLOGY"
        title_label = Label(text=default_college_name, font=("palatino", 32, "bold",),
                            bg='black', fg='#f5f5f5')
        title_label.place(x=140, y=0, width=1220, height=100)

        # Creator's Logo
        default_creator_logo = Image.open("GP_Logo.png")
        default_creator_logo = default_creator_logo.resize((150, 150), Image.BICUBIC)
        self.default_creator_photoimg = ImageTk.PhotoImage(default_creator_logo)

        second_label = Label(self.root, image=self.default_creator_photoimg)
        second_label.place(x=620, y=560, width=150, height=150)

        # Title Of Project
        title_label1 = Label(text="SSIT Information", font=("palatino", 26, "bold", "underline"), bg='#282b30', fg='#f5f5f5')
        title_label1.place(x=0, y=120, width=1360, height=50)

        # List of choices
        choices = [
            "Admission Enquiry Details",
            "Managing Director Sir's  Detail",
            "Principal Sir's Details",
            "Faculties",
            "Other Information"
        ]

        # Labels for choices
        label_height = 40
        for i, choice in enumerate(choices, start=1):
            tk.Label(root, text=f"{i}. {choice}", font=("palatino", 24, "italic"), bg='#282b30', fg='#f5f5f5').place(
                x=510, y=205 + (i - 1) * label_height, anchor="w")

        # Entry for entering choice
        self.choice_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.choice_entry.place(x=570, y=190 + i * label_height, width=250, height=30)
        self.choice_entry.bind("<Return>", self.on_enter_pressed)
        self.choice_entry.focus()
    
    def on_enter_pressed(self, choice):
        try:
            choice = int(self.choice_entry.get())
            if choice in range(1, 6):
                self.show_details_window(choice)
                self.choice_entry.delete(0, tk.END)
            else:
                tk.messagebox.showwarning("Invalid Input", "Please enter a valid choice.")
        
        except ValueError:
            tk.messagebox.showwarning("Invalid Input", "Please enter a numeric value.")


    #=====For the Choices Windows=========
            
    def show_details_window(self, choice):
        new_window = tk.Toplevel(self.root)
        new_window.geometry("1360x688+0+0")
        new_window.config(bg='black')
        new_window.title("SSIT Information Center")

        # Logo
        img = Image.open(r"images/topic_1.png")
        #img = img.resize((140, 100), Image.BICUBIC)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(new_window, image=self.photoimg)
        first_label.place(x=0, y=0, width=1360, height=100)

        # Creator's Logo
        img1 = Image.open("GP_Logo1.png")
        img1 = img1.resize((100, 100), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        second_label = Label(new_window, image=self.photoimg1)
        second_label.place(x=1270, y=615, width=100, height=100)

        # Title Of Project
        title_label1 = Label(text="SSIT Information", font=("palatino", 26, "bold", "underline"), bg='#282b30', fg='#f5f5f5')
        title_label1.place(x=0, y=120, width=1360, height=50)

        def on_escape(event):
            new_window.destroy()

        new_window.bind("<Escape>", on_escape)

        if choice == 1:  # Row wise: first photo and then its details
            self.show_row_wise(new_window, 1)

        elif choice == 2:  # Center photo and its details
            self.show_centered(new_window, 2)

        elif choice == 3:  # Column wise: photo and its details
            self.show_column_wise(new_window, 3)

        elif choice == 4:  # Column wise: first photo, then below its photos
            self.show_column_wise_multiple_photos(new_window, 4)

        elif choice == 5:  # One photo for feedback, college URL, study material sites
            self.show_feedback_and_urls(new_window, 5)
        

    #========Admission Enquiry Detail Function=========
    def show_row_wise(self, window, choice):
        # Title Of Project
        title_label2 = Label(window, text="Admission Enquiry", font=("palatino", 26, "bold", "underline"), bg='black', fg='#f5f5f5')
        title_label2.place(x=0, y=120, width=1360, height=50)

        img = Image.open(r"images/modi.jpg")
        img = img.resize((100, 100), Image.BICUBIC)
        photoimg = ImageTk.PhotoImage(img)

        photo_label = Label(window)
        photo_label.image = photoimg  # Keep a reference to the image
        photo_label.configure(image=photoimg)
        photo_label.place(x=80, y=200, width=100, height=100)

        details_label = Label(window, text="Prof. Neeraj Thakor\nContact No.03980948289 ", font=("palatino", 16), bg='black', fg='#f5f5f5')
        details_label.place(x=0, y=300, width=250, height=100)

       
    #========Managing Director's Sir Details Function=========
    def show_centered(self, window, choice):
        # Title Of Project
        title_label2 = Label(window, text="Managing Director", font=("palatino", 26, "bold", "underline"), bg='black', fg='#f5f5f5')
        title_label2.place(x=0, y=120, width=1360, height=50)

        #Director's Sir Photo
        img = Image.open(r"images/modi.jpg")
        img = img.resize((200, 200), Image.BICUBIC)
        photoimg = ImageTk.PhotoImage(img)

        photo_label = Label(window)
        photo_label.image = photoimg  # Keep a reference to the image
        photo_label.configure(image=photoimg)
        photo_label.place(x=580, y=170, width=200, height=200)

        #Director's Sir Name
        details_label = Label(window, text="Prof.Dharmesh Vandra", font=("palatino", 16, "bold"), bg='black', fg='#f5f5f5')
        details_label.place(x=560, y=380, width=250, height=20)

        #Director's Sir Detail
        detailed_text = """
        Prof.Dharmesh Vandra is the Managing Director of SSIT. 
        He is a very experienced person and has a great knowledge of the field. 
        He is a very helpful person and always ready to help the students. 
        He is a very good person. He is a professor of EC department."""
        
        details_label1 = Label(window, text=detailed_text, font=("palatino", 16), bg='black', fg='#f5f5f5', justify=tk.LEFT)
        details_label1.place(x=0, y=400, width=1360, height=150)

    def show_column_wise(self, window, choice):
        # Column wise: photo and its details
        img = Image.open(r"images/modi.jpg")
        img = img.resize((100, 100), Image.BICUBIC)
        photoimg = ImageTk.PhotoImage(img)

        photo_label = Label(window, image=photoimg)
        photo_label.place(x=150, y=250, width=100, height=100)

        details_label = Label(window, text="Details for Column Wise", font=("palatino", 16), bg='#282b30', fg='#f5f5f5')
        details_label.place(x=200, y=250, width=300, height=100)

    def show_column_wise_multiple_photos(self, window, choice):
        # Column wise: first photo, then below its photos
        for i in range(3):
            img = Image.open(r"images/modi.jpg")
            img = img.resize((100, 100), Image.BICUBIC)
            photoimg = ImageTk.PhotoImage(img)

            photo_label = Label(window, image=photoimg)
            photo_label.place(x=50, y=250 + i * 120, width=100, height=100)

            details_label = Label(window, text=f"Details for Photo {i + 1}", font=("palatino", 16), bg='#282b30', fg='#f5f5f5')
            details_label.place(x=200, y=250 + i * 120, width=300, height=100)

    def show_feedback_and_urls(self, window, choice):
        # One photo for feedback, college URL, study material sites
        img = Image.open(r"images/modi.jpg")
        img = img.resize((100, 100), Image.BICUBIC)
        photoimg = ImageTk.PhotoImage(img)

        photo_label = Label(window, image=photoimg)
        photo_label.place(x=50, y=250, width=100, height=100)

        details_label = Label(window, text="Feedback and URLs", font=("palatino", 16), bg='#282b30', fg='#f5f5f5')
        details_label.place(x=200, y=250, width=300, height=100)

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)

    # Function to exit on "Esc" key press
    def on_escape(event):
        root.destroy()

    root.bind("<Escape>", on_escape)

    root.mainloop()
