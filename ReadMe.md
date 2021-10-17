# Learning Django
Documented here are the items that i've learned by learning more about Django

## Getting Setup
Downloading Pycharm community edition i was able to get up and running pretty fast. Creating a project was easy.

### Window into my world.
I was using a Windows machine to get this going. Once i started a project in pycharm, the defaul terminal that I got was PowerShell. When i am running the commands to activate the virtual environment PowerShell would not show that I had the environment working. 

```C:> venv\Scripts\activate.bat```

Therefore, i had to change the settings to use the cmd.exe as my default terminal. Pycharm already activates the environment for you. Its nice but all you need to do is to run that _activate.bat_ file to start up your virtual env.

## Getting Started
Once you have your virtual env setup, you can now get started by installing the necessary dependencies for your project. Run the following to install Django into your project.

```C:> <inside your virtual env> python -m pip install django```

Here were we are running the python command the -m is the mod flag which calls the __pip__ module to call the __install__ command to install __django__. Since this was called inside our active virtual environment this installs django within that.

## Creating the Django Project
I am following a course put on by Reindert-Jan Ekker on Pluralsight and the project is essentially creating a basic meeting planner application. 

After installing Django into our env we can get started creating our project. Execute the following command in your virtual env:

```C:> <inside your virtual env> django-admin startproject meeting_planner```

This creates a meeting-planner folder inside your project folder. ```django-admin``` is for administrative tasks that is available to you as a command-line utility. For more information please [review the docs](https://docs.djangoproject.com/en/3.2/ref/django-admin/).

This creates a __meeting-planner__ folder inside your project directory. 

### Manage.py
Inside the meeting-planner folder you can see that there is a __manage.py__ file. This has a similar functionality to django-admin but it also sets the DJANGO_SETTINGS_MODULE env variable to point to the project's __settings.py__ file. The file __manage.py__ is saved in the folder that django created when we called _startproject_.

### Starting the Project
Once you called the _startproject_ django created a folder for you with that project name. In this guide it was called _meeting-planner_ we can nagvigate to where that manage.py file and pass in the _runserver_ command

```
C:> <venv> <your project root>cd meeting-planner
C:> <venv> <your project root>\meeting-planner python manage.py runserver
```

This will fire up the development server using the settings defined in the _settings.py_ file inside ```<root>\meeting-planner\meeeting-planner``` folder. The server will be available at ```http://127.0.0.1:8000/```. You will see that a db.sqlite3 file has been added to the parent meeting-planner folder. This is a result of running the server. You'll notice that there are there was another folder name similarly to the project name (meeting-planner). The child folder is the package that pretty much contains the web-app. The two files that we'll be working with throughout is _settings.py_ and _urls.py_.

### That one security warning
If you navigate to the settings.py file you can see that there is a SECRET_KEY variable storing a strange string of characters. Please be careful not to share any passwords or secrets out in the internet!

