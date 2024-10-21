from tkinter import *
from PIL import ImageTk, Image
import speech_to_text
import action

root = Tk()
root.title("Virtual Assistant")
root.geometry("800x700")
root.resizable(False, False)
root.config(bg="#2b2b2b")

# Function for ask
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.actions(user_val)
    history_text_box.insert(END, 'User--->'+user_val+'\n')
    if bot_val is not None:
        history_text_box.insert(END, 'Bot--->'+str(bot_val)+'\n')
    if bot_val == "Shutting Down":
        root.destroy()

# Function for insert
def insert():
    insert = text_entry.get()
    bot = action.actions(insert)
    history_text_box.insert(END, 'User--->'+insert+'\n')
    if bot is not None:
        history_text_box.insert(END, 'Bot--->'+str(bot)+'\n')
    if bot == "Shutting Down":
        root.destroy()

# Function for delete
def delete():
    history_text_box.delete('1.0', END)

# Main frame
main_frame = Frame(root, bg="#2b2b2b")
main_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

# Text label
text_label = Label(main_frame, text="Welcome to Virtual Assistant", font=("Poppins", 24, "bold"), bg="#2b2b2b", fg="#fff")
text_label.pack(pady=20)

# Load and display the image
image = Image.open("image/vir_assistant.png")
resized_image = image.resize((200, 200))
tk_image = ImageTk.PhotoImage(resized_image)
image_label = Label(main_frame, image=tk_image, bg="#2b2b2b")
image_label.pack(pady=20)

# History text box
history_text_box = Text(main_frame, font=("Poppins", 12), bg="#3b3b3b", fg="#fff", height=10, width=50, wrap=WORD, bd=0, padx=10, pady=10)
history_text_box.pack(pady=10)

# Text entry
text_entry = Entry(main_frame, justify="center", font=("Poppins", 12), bg="#3b3b3b", fg="#fff", width=50, bd=0, insertbackground='white')
text_entry.pack(pady=10)

# Button frame
button_frame = Frame(main_frame, bg="#2b2b2b")
button_frame.pack(pady=20)

# Button styling
button_style = {
    "font": ("Poppins", 12),
    "bg": "#4CAF50",
    "fg": "#fff",
    "padx": 20,
    "pady": 10,
    "borderwidth": 0,
    "relief": "flat"
}

# Buttons
Button(button_frame, text="Ask", command=ask, **button_style).pack(side=LEFT, padx=10)
Button(button_frame, text="Insert", command=insert, **button_style).pack(side=LEFT, padx=10)
Button(button_frame, text="Delete", command=delete, **button_style).pack(side=LEFT, padx=10)

root.mainloop()