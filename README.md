# SmartSearch

SmartSearch is a Django web application that allows users to manage Points of Interest (POIs) and search for them based on various criteria.

## Getting Started

Follow these steps to set up and run the SmartSearch application locally.

### Prerequisites

- Python (3.8 or higher)
- pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your_username/smartSearch.git
Navigate to the project directory:

bash
Copy code
cd smartSearch
Create a virtual environment (optional but recommended):

bash
Copy code
virtualenv venv
Activate the virtual environment:

Windows:
bash
Copy code
venv\Scripts\activate
Linux/macOS:
bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Database Setup
Migrate the database:
bash
Copy code
python manage.py migrate
Importing Data
To import data into the database, you can use the following command:

bash
Copy code
python manage.py import_poi_data <path_to_data_file>
Replace <path_to_data_file> with the path to your data file (JSON/XML).

Running the Application
Start the development server:

bash
Copy code
python manage.py runserver
Access the application in your web browser at http://localhost:8000.

Accessing Django Admin
Create a superuser account:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to provide a username, email, and password.

Access the Django admin panel in your web browser at http://localhost:8000/admin.

Usage
Use the web interface to search for Points of Interest based on categories, IDs, etc.
Log in to the Django admin panel to manage POIs, users, etc.
Contributing
Contributions are welcome! Please follow the contribution guidelines.

License
This project is licensed under the MIT License - see the LICENSE file for details.