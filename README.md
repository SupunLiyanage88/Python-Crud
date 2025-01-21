# Flask CRUD Application

This is a simple CRUD application built with Flask, designed for developers to experiment with Python, Flask, and JavaScript integration. It includes basic functionality for creating, reading, updating, and deleting notes. This project is intended for **developer use only** and is not optimized for production environments.

---

## Features

### Backend:
- **Flask Web Framework**: Handles routing and logic.
- **SQLAlchemy**: Manages the SQLite database for storing user and note data.
- **Flask-Login**: Handles user authentication and session management.
- **SQLite Database**: Simple and lightweight database solution for managing users and notes.

### Frontend:
- **Jinja Templates**: Dynamically render user notes.
- **Tailwind CSS**: Provides a modern and responsive design.
- **Features Include**:
  - Form for creating new notes.
  - Editable note cards with save and cancel functionality.
  - "Delete Note" functionality with confirmation.
  - Dynamic display of the total number of notes.

### JavaScript Integration:
- **Fetch API**: Enables asynchronous operations for deleting, editing, and saving notes.
- Provides a smooth user experience with minimal page reloads.

### Interactive Features:
- Notes can be edited directly on the page.
- Notes are displayed in a responsive grid layout.
- Displays an empty state message if no notes exist.

---

## Installation

### Prerequisites:
- Python 3.7+
- Flask and required packages (see `requirements.txt`)

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-crud-notes.git
   ```
2. Navigate to the project directory:
   ```bash
   cd flask-crud-notes
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Flask application:
   ```bash
   flask run
   ```
6. Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Usage

- **Create a Note**: Use the form to add a new note.
- **Edit a Note**: Click the edit button on a note to modify it directly.
- **Delete a Note**: Click the delete button to remove a note (confirmation required).
- **View Notes**: Notes are displayed dynamically, with an empty state message if no notes exist.

---

## Example Screenshot

![Application Screenshot](https://github.com/SupunLiyanage88/Python-Crud/blob/fea29fcbc35874a966acbc53517d2ddca4d093d8/Screenshot%202025-01-21%20120115.png)
![Application Screenshot](https://github.com/SupunLiyanage88/Python-Crud/blob/5126210cf25a1eedbf250e8668362d6d92b39e8d/Screenshot%202025-01-21%20121240.png)


## Folder Structure

```
flask-crud-notes/
|-- instance/
|-- venv/
|-- website/
|   |-- __pycache__/
|   |-- instance/
|   |   |-- database.db
|   |-- static/
|   |   |-- index.js
|   |-- templates/
|   |   |-- base.html
|   |   |-- home.html
|   |   |-- login.html
|   |   |-- sign_up.html
|   |-- __init__.py
|   |-- auth.py
|   |-- models.py
|   |-- views.py
|-- main.py
```

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

---

## License

This project is licensed under the MIT License.

---

## Disclaimer

This project is for **developer use only** and is not suitable for production environments.

