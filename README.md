# Flask Student Database App

This is a simple Flask web application that allows users to submit student information through a form and saves it to a database. The submitted data is then displayed on the webpage.

## Features

- Submit student information including name, college, roll no. and branch through a form.
- Save the submitted data to a database.
- Display the submitted data on the webpage.

## Technologies Used

- Python
- Flask
- SQLAlchemy (for interacting with the database)
- HTML/CSS (for the form and webpage layout)

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt`
   ```
3. Set up the database:
   - Now, you need to create the database and the student table. You can do this by running the following commands in your terminal or command prompt:
     ```bash
     python
     ```
     ```python
      from app import db
      db.create_all()
      exit()
     ```
4. Start the Flask development server:
   ```bash
   python app.py
   ```
5. Open a web browser and navigate to [http://localhost:5000](http://localhost:5000) to access the application. <br>
   Preview: <br>
   ![image](staic/images/preview.png)
   
