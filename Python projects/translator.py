# importing tkinter
import tkinter as tk

# importing ttk module from tkinter as it has the combobox class
from tkinter import ttk

# creating root gui
root = tk.Tk()

# properties of root gui
root.geometry('700x400')
root.resizable(width=False, height=False)
root.title('Language Translator')
root.config(bg='#f5fefd')

# Universal variables
py = 10 # This is padding not pixels
px = 30
bg_color = '#7b3f00'
fg_color = 'white'
button_font = 'Helvetica'
button_font_size = 12

# Adding widgets
welcome_label = tk.Label(root, text='LANGUAGE TRANSLATOR', bg='#f5fefd', font=('Comic Sans MS', 30))
welcome_label.pack(pady = 20)

# creating a frame to arrange my widget in grid layout
frame = tk.Frame(root, bg='#e7decc', width=500, height=100)
frame.pack(padx = 10, pady=10, fill='both')

# source and target language labels
source_label = tk.Label(frame, text='Source Language', bg=bg_color, fg=fg_color, font=('Comic Sans MS', 20))
target_label = tk.Label(frame, text='Target Language', bg=bg_color, fg=fg_color, font=('Comic Sans MS', 20))
source_label.grid(row=0, column=0, padx=px, pady=py)
target_label.grid(row=0, column=2, padx=px, pady=py)

# Add comboboxes
source_cb = ttk.Combobox(frame, values=['English', 'Hindi'], width=30)
target_cb = ttk.Combobox(frame, values=['English', 'Hindi', 'French'], width=30)
source_cb.grid(row=1, column=0, padx=px, pady=py)
target_cb.grid(row=1, column=2, padx=px, pady=py)

# Adding row 2 elements --> Input text area, translate button, Output label
input_text = tk.Text(frame, width=25, height=5)
translate_button = tk.Button(frame, text='Translate', bg=bg_color, fg=fg_color, font=(button_font, button_font_size))
output_label = tk.Label(frame, text='No Translations Yet!', bg=bg_color, fg=fg_color, width=30, height=5)
input_text.grid(row=2, column=0, padx=px, pady=py)
translate_button.grid(row=2, column=1, padx=px, pady=py)
output_label.grid(row=2, column=2, padx=px, pady=py)

# Adding row 3 elements --> voice,  clear, speak button
voice_button = tk.Button(frame, text='Say Something', bg=bg_color, fg=fg_color, font=(button_font, button_font_size))
clear_button = tk.Button(frame, text='Clear', bg=bg_color, fg=fg_color, font=(button_font, button_font_size))
speak_button = tk.Button(frame, text='Speak Translation', bg=bg_color, fg=fg_color, font=(button_font, button_font_size))
voice_button.grid(row=3, column=0, padx=px, pady=py)
clear_button.grid(row=3, column=1, padx=px, pady=py)
speak_button.grid(row=3, column=2, padx=px, pady=py)

# for continuous display
root.mainloop()