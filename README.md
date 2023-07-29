# Adventure Sports Website with Flask

This is a web application built with Flask that showcases various adventure sports offered by "WildRush Adventures". The website allows users to explore and get information about different adventure sports activities, request a quote, and learn more about the founding team behind the company.

## Features

- **Home Page**: The home page displays information about the company and the adventure sports activities offered by the company. The home page also displays a list of the founding team members.

- **Adventure Sports Page**: The adventure sports page displays information about the adventure sports activities offered by the company. The adventure sports page also displays a list of the founding team members.

- **Request a Quote Page**: The request a quote page displays a form for users to request a quote for an adventure sports activity. The form includes fields for the user's name, email address, phone number, and message.

- **Reviews Page**: The reviews page displays a list of reviews from customers who have used the company's services.

- **Contact Page**: The contact page displays a form for users to contact the company. The form includes fields for the user's name, email address and message.

- **Login Page**: The login page displays a form for users to log in to the website. The form includes fields for the user's email address and password.

- **Register Page**: The register page displays a form for users to create an account on the website. The form includes fields for the user's name, email address, password, and confirm password.

## Project Structure

```bash
- app/ # Main Flask application directory
- __init__.py # Initializes the Flask app
- routes.py # Defines the routes for the app
- models.py # Defines the database models
- static/ # Static files for the app
- css/ # CSS files
  - style.css # Defines the styles for the app
- js/ # JavaScript files
- templates/ # HTML templates for the app
- assets/ # Images and other assets
- run.py # Runs the Flask app
- requirements.txt # List of required Python packages
- README.md # Project documentation (you are here)
```

This project structure organizes the Flask app into distinct directories for better manageability and separation of concerns. The app directory contains the main Flask application files, while the static directory holds static assets like CSS and JavaScript. The templates directory houses the HTML templates used for rendering different pages, and the requirements.txt file ensures that the required Python packages are installed for the app to run smoothly.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (>=3.6)
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Bcrypt
- python-dotenv

You can install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone this repository to your local machine or download the ZIP file and extract it.

   ```bash
   git clone https://github.com/Saimadhav09/wildrush-adventures.git
   ```

2. Navigate to the project directory.

   ```bash
   cd wildrush-adventures
   ```

3. (Optional) Create and activate a virtual environment to isolate the project's dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the project dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

- **Database**: The application is configured to use SQLite as the database. You can change this by modifying the `SQLALCHEMY_DATABASE_URI` variable in the `.env` file.

- **Secret Key**: The application uses a secret key to sign cookies and protect against CSRF attacks. You can change this by modifying the `SECRET_KEY` variable in the `.env` file.

## Usage

1. Make sure you are in the project directory and have activated the virtual environment (if you created one).

   ```bash
   cd wildrush-adventures
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

1. Run the Flask application.

   ```bash
   python run.py
   ```

1. Open your web browser and go to `http://127.0.0.1:5000/` to access the landing page.

> **Note**: To stop the application, press `Ctrl+C` in the terminal.
