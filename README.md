# teachersDirectory

Prerequisites
--------------
1. Python3.6.1
2. Pip3

Database used: SQLite

Flow
-----
1. git clone git@github.com:ShamlaHameed123/teachersDirectory.git
2. Run pip3 install -r requirements.txt
3. cd teachers
4. python3 manage.py makemigrations
5. python3 manage.py migrate
6. Run python3 manage.py runserver // Runs the backend server at port 8000 by default

Import csv to populate database
-------------------------------
After running the server, open http://localhost:8000/teachers/home and click on populate feed once so to populate the database. The database will get populated by the teachers whose number of subjects taught is less than or equal to 5 only.

1. Teacher's directory opens at http://localhost:8000/teachers/home.
2. Click on the teacher to open up the profile page at http://localhost:8000/teachers/profile/{teacher-id}
3. For the teacher whose profile image is not available, default_teacher.png image will be displayed.
4. The teachers' directory can be imported by clicking on Export as csv, where csv will be downloaded only by authenticated user, hence prompting to login.
5. The teacher can be filtered by firstname or the subjects taught by searching through Search bar.




