import tkinter as tk
from tkinter import *
import wikipedia as wk

# Initialize the main window
window = Tk()
window.title("MY Mini Wikipedia")
window.config(bg="black")

# Heading label
Label(window, text="MY Mini Wikipedia", font=("Times", 30, "bold"), bg="#00A86B").pack(side=TOP, pady=10)

# Search label and entry box
Label(window, text="Search", font=("Arial", 20, "bold"), bg="yellow").pack(side=TOP, pady=5)
entry_box = Entry(window, width=40, font=("Arial", 20, "bold"))
entry_box.pack(side=TOP, pady=5)
entry_box.focus_set()

# Search button function
def text_Search():
    text.delete('1.0', END)  # Clear previous results
    query = entry_box.get()
    try:
        # Fetch full Wikipedia page content
        page = wk.page(query)
        full_content = page.content  # Retrieve full content of the page
        text.insert('1.0', full_content)
    except wk.exceptions.PageError:
        text.insert('1.0', "No page found for your query. Please try again.")
    except wk.exceptions.DisambiguationError as e:
        text.insert('1.0', f"Your search query is ambiguous. Suggestions:\n\n{e.options}")
    except Exception as e:
        text.insert('1.0', f"An error occurred: {str(e)}")

# Search button
button1 = Button(window, text="Search", font=("Arial", 15, "bold"), bg="red", fg="white", command=text_Search)
button1.pack(side=TOP, pady=5)

# Searched results label
Label(window, text="Searched Results", font=("Arial", 25, "bold"), bg="#FFFDD0").pack(side=TOP, pady=10)

# Text widget for displaying results
text = Text(window, font=("Arial", 17, "bold"), bg="gray", padx=20, pady=10, wrap=WORD)
text.pack(pady=10, padx=10)

# Start the main event loop
window.mainloop()
