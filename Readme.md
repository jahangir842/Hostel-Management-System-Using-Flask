# Hostel Management System

This is a Flask-based web application for managing a hostel. It includes functionalities for enrolling students, managing rooms, tracking expenses, and more.

## Features

- Enroll students with details including name, fee, room number, and picture.
- Manage rooms and see which students are assigned to which rooms.
- Track monthly expenses by adding items and their prices.
- View a list of all students and rooms.
- Responsive design using Bootstrap.

## Technologies Used

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/)
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [SQLite](https://www.sqlite.org/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [ReportLab](https://www.reportlab.com/)
- [Pandas](https://pandas.pydata.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/)

## Recommended Dev Tools

- [VS Code](https://code.visualstudio.com/download)
- [Black Formatter](https://code.visualstudio.com/docs/python/formatting)

## Setup and Installation

### Option 1: Using Pipenv (Recommended)

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Hostel-Management-System-Using-Flask.git
   cd Hostel-Management-System-Using-Flask
   ```

2. Install `pipenv` if you don't have it:

   ```bash
   pip install pipenv
   ```

3. Install dependencies and create a virtual environment:

   ```bash
   pipenv install
   ```

4. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

5. Initialize the database:

   ```bash
   flask db init
   flask db upgrade
   ```

6. Run the application:

   ```bash
   flask run
   ```

7. Open your browser and navigate to `http://127.0.0.1:5000`.

### Option 2: Using venv and pip

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Hostel-Management-System-Using-Flask.git
   cd Hostel-Management-System-Using-Flask
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install all the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If you encounter any missing module errors, install them individually:
   
   ```bash
   pip install reportlab flask-migrate flask-sqlalchemy flask-wtf flask-login flask-bcrypt pandas openpyxl
   ```

4. Initialize the database:

   ```bash
   flask db init
   flask db upgrade
   ```

5. Run the application:

   ```bash
   flask run
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000`.

## Deployment

This application can be deployed to Vercel using GitHub Actions for continuous deployment. For detailed instructions, see the [DEPLOYMENT.md](DEPLOYMENT.md) file.

### Quick Deployment Steps:

1. Fork this repository
2. Set up a Vercel account and get your API tokens
3. Add your Vercel tokens as GitHub secrets
4. Push to your main branch to trigger automatic deployment

## Troubleshooting

If you encounter errors like "No module named 'reportlab'" or "No such command 'db'", make sure you have installed all required dependencies as shown in step 3 of Option 2.

## Application Structure

- `app.py`: Main application file containing routes and logic.
- `models.py`: Database models for Student, Room, and Expense.
- `forms.py`: Forms for enrolling students and adding expenses.
- `templates/`: HTML templates for the application pages.
- `static/`: Static files including CSS and images.
- `migrations/`: Database migration files.

## Routes

- `/`: Home page with links to enroll, view students, view rooms, and manage expenses.
- `/enroll`: Form to enroll a new student.
- `/students`: List of all enrolled students.
- `/rooms`: List of all rooms and their assigned students.
- `/expenses`: Form to add expenses and view total monthly expenses.

## Images 
![Admin Dashboard]](<Screenshot from 2025-04-20 16-15-48.png>)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or suggestions, please contact [najamabass2020@gmail.com](mailto:your-email@example.com).
