Clone the Repository:

Bash
git clone https://github.com/your_username/smartSearch.git
Use code with caution.
Navigate to the Project:

Bash
cd smartSearch
Use code with caution.
Install Dependencies:

Bash
pipenv install
Use code with caution.
Database Setup:

Bash
pipenv run python manage.py migrate
Use code with caution.
Import Data (Optional):

To populate your database with POIs, run:

Bash
pipenv run python manage.py import_poi_data <path_to_data_file>
Use code with caution.
Replace <path_to_data_file> with the actual path to your data file (JSON or XML).

Run the Application:

Bash
pipenv run python manage.py runserver
Use code with caution.
Access SmartSearch in your web browser at http://localhost:8000.

Django Admin:

Create a superuser account for administrative tasks:

Bash
pipenv run python manage.py createsuperuser
Use code with caution.
Log in to the admin panel at http://localhost:8000/admin using your credentials.

Usage
SmartSearch's intuitive web interface lets you:

Search for POIs: Narrow down your search using categories, IDs, and other criteria to find exactly what you're looking for.
Manage POIs (Optional): Log in to the Django admin panel to add, edit, delete, and organize your POIs with ease.
Contributing
We welcome contributions to SmartSearch! 

