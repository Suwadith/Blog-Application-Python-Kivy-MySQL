Software requirements
    1. Python 3.9.x
    2. Latest pip version 22.0.x


Setting up the MySQL DB
    1. create a user on the db with username='admin' and password='admin' with all the admin/root privileges
    2. create a database named 'blog'
    3. import the Assets/blog.sql file on to the database
    4. make sure the server is up and running and using the default port


Setting up the virtual environment and executing the program
    1. execute the following command on the root directory(basically inside the code repository) to set up the virtual environment
        $ python3 -m venv venv
    2. execute the below command on the same directory to use or activate the virtual environment
        1. Windows
            $ venv\Scripts\activate
        2. Linux
            $ source venv/bin/activate
    3. install the dependencies using the following command using the virtual environment
        $ pip install -r requirements.txt
    4. run the following command to start the kivy app using the virtual environment
        $ python Main.py


Screens - Left to Right (Can be navigated using different icons provided in the top toolbar)
    1. Public Screen (Home Icon)
        Used to view posts that are not restricted. Anyone can view without logging in
    2. Members Screen (Group of people Icon)
        Used to view posts that are member restricted. only logged in registered users can view posts in this section.
    3. Private Screen (Lock Icon)
        Used to display all the posts made by the current logged-in user and gives them teh ability to edit and delete posts their posts.
    4. Create Post Screen (Plus Icon)
        logged-in member will be able to create a blog post. They can choose between public view and member only view.
    5. Admin Screen (Head Icon)
        If the logged-in user is the admin then he'll be able to view all the activity related log entries on a list
    6. Login/Registration Screen (Power Icon)
        Can log in as a normal member or an admin. Or you can register as a non-admin user.


Pre created users
    1. Admin user
        username: admin
        password: Admin$123
    2. Member user
        username: charles
        password: Charles$123




