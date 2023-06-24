week3_project
In an organization, an employee is given multiple devices to carry out his/her day-to-day operations. Created a DB structure and APIs to track the same. Details needed from the API:

1. Inserting the details of a new employee.
2. Inserting a new device.
3. List all the device types
4. Allocate a device to the user.
5. Deallocate the device to the user.
6. Get all the device information of a particular device type along with the user having it.
7. Switch the devices between two employees.
8. Updating, deleting the details of an employee or device.
9. Search a user or device with name(not exact match), device type, email address
10. Get the history of a particular device or employee.
Deployed GET, POST, PATCH and DELETE API's to handle all the cases required.

The first thing to do is to clone the repository:

    $ git clone https://github.com/shahank-attentive/week3_project.git
Create a virtual environment to install dependencies in and activate it:

     $ pip install virtualenv
     $ virtalenv env_name
     $ source path/bin/activate  like source /home/your_name/Environments/env_name/bin/activate
Then install the dependencies:

    (env)$ pip install -r requirements.txt
Once pip has finished downloading the dependencies:

    (env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000

Now you can see the link for Employee and Devices and perform CRUD operations
