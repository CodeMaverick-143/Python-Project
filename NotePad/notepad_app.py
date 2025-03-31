import tkinter as tk
from tkinter import messagebox, simpledialog
import pyttsx3
import sqlite3
import os

# Initialize Text-to-Speech Engine.
engine = pyttsx3.init()

# Database Setup
def create_db():
    conn = sqlite3.connect('notepad.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, category TEXT)''')
    conn.commit()
    conn.close()

create_db()

# Function to Add Note to Database
def save_note(title, content, category):
    conn = sqlite3.connect('notepad.db')
    c = conn.cursor()
    c.execute('INSERT INTO notes (title, content, category) VALUES (?, ?, ?)', (title, content, category))
    conn.commit()
    conn.close()

# Function to Fetch Notes
def fetch_notes(category_filter=None):
    conn = sqlite3.connect('notepad.db')
    c = conn.cursor()
    if category_filter:
        c.execute('SELECT * FROM notes WHERE category=?', (category_filter,))
    else:
        c.execute('SELECT * FROM notes')
    notes = c.fetchall()
    conn.close()
    return notes

# Function to Search Notes by Content
def search_notes(query):
    conn = sqlite3.connect('notepad.db')
    c = conn.cursor()
    c.execute('SELECT * FROM notes WHERE content LIKE ?', ('%' + query + '%',))
    notes = c.fetchall()
    conn.close()
    return notes

# Function to Read Notes Aloud
def read_note_aloud(content):
    engine.say(content)
    engine.runAndWait()

# Main Application Class
class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Notepad Application")
        self.root.geometry("600x400")

        self.category_filter = None

        self.create_widgets()

    def create_widgets(self):
        # Search Bar
        self.search_var = tk.StringVar()
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)
        search_label = tk.Label(search_frame, text="Search Notes:")
        search_label.pack(side=tk.LEFT, padx=5)
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(search_frame, text="Search", command=self.search_notes)
        search_button.pack(side=tk.LEFT)

        # Notes List
        self.notes_listbox = tk.Listbox(self.root, width=80, height=15)
        self.notes_listbox.pack(pady=20)
        self.notes_listbox.bind("<Double-1>", self.open_note)

        # New Note Button
        new_note_button = tk.Button(self.root, text="New Note", command=self.new_note)
        new_note_button.pack(pady=5)

        # Read Note Aloud Button
        read_button = tk.Button(self.root, text="Read Aloud", command=self.read_selected_note)
        read_button.pack(pady=5)

        # Show Notes
        self.show_notes()

    def show_notes(self):
        self.notes_listbox.delete(0, tk.END)
        notes = fetch_notes(self.category_filter)
        for note in notes:
            self.notes_listbox.insert(tk.END, note[1])  # Display title only

    def search_notes(self):
        query = self.search_var.get()
        notes = search_notes(query)
        self.notes_listbox.delete(0, tk.END)
        for note in notes:
            self.notes_listbox.insert(tk.END, note[1])  # Display title only

    def open_note(self, event):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            selected_note = fetch_notes()[selected_index[0]]
            note_title = selected_note[1]
            note_content = selected_note[2]
            note_category = selected_note[3]

            note_window = tk.Toplevel(self.root)
            note_window.title(note_title)

            # Note Title
            title_label = tk.Label(note_window, text="Title")
            title_label.pack()
            title_entry = tk.Entry(note_window)
            title_entry.insert(tk.END, note_title)
            title_entry.pack()

            # Note Content
            content_label = tk.Label(note_window, text="Content")
            content_label.pack()
            content_text = tk.Text(note_window, height=10, width=50)
            content_text.insert(tk.END, note_content)
            content_text.pack()

            # Note Category
            category_label = tk.Label(note_window, text="Category")
            category_label.pack()
            category_entry = tk.Entry(note_window)
            category_entry.insert(tk.END, note_category)
            category_entry.pack()

            # Save Button
            save_button = tk.Button(note_window, text="Save", command=lambda: self.save_edited_note(
                selected_note[0], title_entry.get(), content_text.get("1.0", tk.END), category_entry.get()))
            save_button.pack(pady=5)

    def save_edited_note(self, note_id, title, content, category):
        conn = sqlite3.connect('notepad.db')
        c = conn.cursor()
        c.execute('UPDATE notes SET title=?, content=?, category=? WHERE id=?', (title, content, category, note_id))
        conn.commit()
        conn.close()
        self.show_notes()

    def new_note(self):
        new_note_window = tk.Toplevel(self.root)
        new_note_window.title("New Note")

        # Note Title
        title_label = tk.Label(new_note_window, text="Title")
        title_label.pack()
        title_entry = tk.Entry(new_note_window)
        title_entry.pack()

        # Note Content
        content_label = tk.Label(new_note_window, text="Content")
        content_label.pack()
        content_text = tk.Text(new_note_window, height=10, width=50)
        content_text.pack()

        # Note Category
        category_label = tk.Label(new_note_window, text="Category")
        category_label.pack()
        category_entry = tk.Entry(new_note_window)
        category_entry.pack()

        # Save Button
        save_button = tk.Button(new_note_window, text="Save", command=lambda: self.save_new_note(
            title_entry.get(), content_text.get("1.0", tk.END), category_entry.get()))
        save_button.pack(pady=5)

    def save_new_note(self, title, content, category):
        save_note(title, content, category)
        self.show_notes()

    def read_selected_note(self):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            selected_note = fetch_notes()[selected_index[0]]
            note_content = selected_note[2]
            read_note_aloud(note_content)

# Main Loop
if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
