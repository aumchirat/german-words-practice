import tkinter as tk
from tkinter import messagebox, ttk
from infinite_random_with_ui import get_random_word, check_answer

word = ""
def show_random_word():
    global word
    word = get_random_word()
    randomed_word.config(text=word)

def submit_input():
    user_text = user_entry.get()
    print("User input:", user_text)
    correct_answer = check_answer(word, user_text)
    feedback.config(text=correct_answer)
    user_entry.delete(0, tk.END)

    
root = tk.Tk()
root.title("Common Nouns Practice")
root.geometry("500x500")

# main content
content = tk.Frame(root)
content.grid(row=0, column=0, sticky="nsew")

tk.Label(
    root,
    text="Common German words",
    font=("Helvetica", 16, "bold")
).grid(row=0,column=0,padx=10, pady=10)

# random word show
randomed_word = tk.Label(
    root,
    text="Click next word",
    font=("Helvetica", 14, "bold")
)
randomed_word.grid(row=1,column=0, columnspan=2)

feedback = tk.Label(
    root,
    text="",
    font=("Helvetica", 12, "bold")
)
feedback.grid(row=4,column=0, columnspan=2)

# input answer
tk.Label(
    root,
    text="Your answer",
    font=("Helvetica", 12)
).grid(row=2, column=0)

user_entry = ttk.Entry(root)
user_entry.grid(row=2, column=1)
# check input


# next word button
next_btn = tk.Button(
    root,
    text="Next word",
    font=("Helvetica", 12),
    command=show_random_word
).grid(row=3,column=0)

# submit answer
submit_btn = tk.Button(
    root,
    text="Submit",
    font=("Helvetica", 12),
    command=submit_input
).grid(row=3,column=1)

root.mainloop()