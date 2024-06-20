import tkinter as tk
from tkinter import messagebox
import pyshorteners

# Function to shorten URL
def shorten_url():
    try:
        long_url = url_entry.get()
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)
        result_label.config(text=f"{short_url}")
        copy_button.config(state=tk.NORMAL)  # Enable copy button
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Function to copy shortened URL
def copy_url():
    window.clipboard_append(result_label.cget("text").split(": ")[-1])  # Extract and copy URL
    messagebox.showinfo("Success", "Shortened URL copied to clipboard!")


# Create the main window
window = tk.Tk()
window.title("URL Shortener")

# Set window size and styling (customizable)
window.geometry("450x350")
window.configure(bg="#3498db")

# Input field (stylish)
url_label = tk.Label(window, text="Enter Long URL:", font=("Arial", 14, "bold"), fg="thistle",bg="black")
url_label.pack(pady=20)
url_entry = tk.Entry(window, width=40, font=("Arial", 12), bg="#ececec")
url_entry.pack()

# Shorten button (rounded)
shorten_button = tk.Button(window, text="Shorten", command=shorten_url, font=("Arial", 12, "bold"), bg="sky blue", fg="white", borderwidth=5, relief=tk.RAISED)
shorten_button.pack(pady=15)

url_label = tk.Label(window, text="Shortened URL:", font=("Arial", 14, "bold"), fg="thistle",bg="black")
url_label.pack(pady=20)

# Result label (clear display)
result_label = tk.Label(window, font=("Arial", 12), fg="black")
result_label.pack()

# Copy button (consistent style)
copy_button = tk.Button(
    window, text="Copy", command=copy_url, state=tk.DISABLED, font=("Arial", 12, "bold"), bg="sky blue", fg="white", borderwidth=5, relief=tk.RAISED)
copy_button.pack(pady=15)

# Run the main loop
window.mainloop()
