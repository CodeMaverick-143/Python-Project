---

# **Desktop Notepad Application**

This is a simple notepad application built with Python, using `Tkinter` for the GUI, `pyttsx3` for text-to-speech functionality, and `sqlite3` for data persistence. This project allows you to create, edit, save, and categorize notes. You can also search through your notes and read them aloud using text-to-speech.

---

## **Features**
- **Create, Save, Edit, and Delete Notes**: Allows users to manage notes.
- **Search Notes**: Search for notes based on their content.
- **Categorize Notes**: Organize notes into categories for better management.
- **Read Notes Aloud**: Integrated with text-to-speech functionality using `pyttsx3`.
- **Persistence**: Notes are saved and retrieved from an SQLite database, ensuring that they persist across app sessions.

---

## **Prerequisites**
Before you start, make sure you have the following installed:

- **Python 3.x** (You can download it from [Python's official website](https://www.python.org/)).
- **Tkinter** (For the GUI – it's usually bundled with Python, but if not, install it using your package manager).
- **pyttsx3** (For text-to-speech functionality).
- **sqlite3** (For storing notes in a local database).

---

## **Installation**

### Option 1: Using a Virtual Environment (Recommended)

1. **Install Python** (If not already installed):
   - Download and install Python from [Python's official website](https://www.python.org/).

2. **Create a Virtual Environment**:
   - Open your terminal/command prompt and run the following command:
     ```bash
     python3 -m venv notepad-env
     ```

3. **Activate the Virtual Environment**:
   - For **Linux/macOS**:
     ```bash
     source notepad-env/bin/activate
     ```
   - For **Windows**:
     ```bash
     notepad-env\Scripts\activate
     ```

4. **Install the Required Libraries**:
   With the virtual environment activated, install the necessary dependencies:
   ```bash
   pip install pyttsx3
   ```

5. **Clone the Project or Download the Code**:
   Clone the repository or download the Python script from the project folder:
   ```bash
   git clone <repository-url>
   ```

6. **Run the Application**:
   - Navigate to the project directory and run the Python script:
     ```bash
     python notepad_app.py
     ```

---

### Option 2: Installing Globally (Not Recommended)

If you don't want to use a virtual environment, you can install the required packages globally (not recommended due to potential conflicts):

1. **Install `pyttsx3`**:
   ```bash
   pip install pyttsx3
   ```

2. **Clone or Download the Project**:
   Clone or download the Python script and navigate to the project directory:
   ```bash
   git clone <repository-url>
   ```

3. **Run the Application**:
   Run the Python script:
   ```bash
   python notepad_app.py
   ```

---

## **Usage**

Once the application is running, you will see the following options in the GUI:

1. **New Note**:
   - Click the "New Note" button to create a new note. You can give it a title, add content, and categorize it.
   
2. **Search**:
   - Use the search bar to search for notes by content. The results will appear in the list below.
   
3. **Edit Note**:
   - Double-click any note in the list to open and edit it. You can update the title, content, and category of the note.

4. **Read Aloud**:
   - Select a note and click the "Read Aloud" button to have the content of the note read aloud using text-to-speech.

5. **Save and Delete Notes**:
   - When editing a note, click "Save" to update the changes.
   - To delete a note, delete its content and save it. (You can also directly delete from the database if needed.)

---

## **SQLite Database**

The notes are stored in an SQLite database (`notepad.db`) in the same directory as the application. You don’t need to interact with the database manually, as the application handles all database operations (creating, saving, updating, deleting) automatically.

---

## **Contributing**

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Make sure to adhere to the following guidelines:

- **Follow PEP-8**: Ensure that the code follows Python’s PEP-8 guidelines for style and readability.
- **Test**: Test your changes before submitting.
- **Document**: Add comments and document your changes where necessary.

---

## **Troubleshooting**

### 1. **Missing `pyttsx3` Library**

If you encounter errors related to the `pyttsx3` library, make sure it's installed in your environment:
```bash
pip install pyttsx3
```

### 2. **Database Issues**

If the application fails to load or save notes, ensure that the SQLite database (`notepad.db`) has been created successfully. If it's missing, it should be created automatically when you first run the application.

### 3. **GUI Issues on Linux**

If you’re running the app on Linux and experiencing GUI issues with Tkinter, you may need to install Tkinter manually:
```bash
sudo apt-get install python3-tk
```

---

## **License**

This project is open source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Contact**

If you have any issues, suggestions, or questions about the project, feel free to reach out via email or open an issue on the repository.

---

This `USE.md` should help users set up the project on their systems, providing detailed steps for installation, usage, and troubleshooting. Feel free to adjust or add additional instructions based on any specific requirements you might have for your project!
