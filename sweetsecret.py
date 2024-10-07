import tkinter as tk
import random

root = tk.Tk()
root.title("Password Protected Animation")
root.attributes("-fullscreen", True)


PASSWORD = "sweetsecret"

def check_password(event=None): 
    entered_password = password_entry.get()
    
    if entered_password == PASSWORD:
        show_thoughts_animation()
    else:
        tk.messagebox.showerror("Error", "Incorrect Password!")

def show_thoughts_animation():
    animation_window = tk.Toplevel(root)
    animation_window.title("Random Thoughts Animation")
    animation_window.attributes("-fullscreen", True)

    canvas = tk.Canvas(animation_window, width=600, height=600, bg='black')
    canvas.pack(fill="both", expand=True)

    # List of random thoughts
    random_thoughts = [
        "Why are we here?", "What is life?", "Nothing matters.", 
        "All is chaos.", "Time is an illusion.", "Who am I?", 
        "This is a simulation.", "The future is uncertain.", 
        "Life is a dream.", "Everything is connected.", "Does it even matter?", 
        "Where is everyone?", "Existence is strange.", "What’s beyond?", 
        "All we know is nothing.", "I think, therefore I am.", 
        "Can we change fate?", "The stars are calling.", 
        "Do we have free will?", "Perception is reality.", 
        "Truth is subjective.", "Where does time go?", 
        "Dreams are our escape.", "Why do we fear?", 
        "The past is gone.", "Everything fades.", 
        "We are stardust.", "Reality bends.", 
        "Endless possibilities.", "Eternal questions.", 
        "What is the point?", "It’s all temporary."
    ]

    def animate_thoughts():

        thought_texts = []
        for _ in range(30): 
            thought = random.choice(random_thoughts)
            x = random.randint(50, animation_window.winfo_width() - 50)
            y = random.randint(50, animation_window.winfo_height() - 50)
            thought_text = canvas.create_text(x, y, text=thought, font=("Arial", 18), fill='green')
            thought_texts.append(thought_text)

        def move_thoughts():
            for thought_text in thought_texts:
                canvas.move(thought_text, 0, -3)  
            root.update()

        for _ in range(80):  
            move_thoughts()
            canvas.after(50)  

        canvas.delete("all")
        canvas.create_text(animation_window.winfo_width() // 2, animation_window.winfo_height() // 2, 
                           text="You are hacked!", font=("Arial", 40), fill='red')

  
        root.bind('<Return>', close_application)

    root.after(100, animate_thoughts)

def close_application(event=None):
    root.quit()


password_label = tk.Label(root, text="Enter Password:", font=("Arial", 14))
password_label.pack(pady=20)
password_entry = tk.Entry(root, show="*", font=("Arial", 14))
password_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=check_password)
submit_button.pack(pady=20)


root.bind('<Return>', check_password)

root.mainloop()
