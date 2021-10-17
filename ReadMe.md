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

## Creating a Simple Web Page
Here is a summary that we'll do next:
* Create a Django app
* Add a view function
* Assign a URL to the view function
* Run and view the page

Question: 
* How does Django serve the page?
* What are some problems and pitfalls to know?

### Creating a Django App
The pattern here is to group things via _apps_. _Apps_ are a concept in Django that groups functionality. Here we are going to create an app that represents the website (or frontend). 

We'll run the following code on our Django Project (meeting-planner):

```python manage.py startapp website```

This will add a _website_ folder inside the meeting-planner project (the parent, from now on will be called the project folder). Inside this folder you see a few py files. For this guide, well just focus on the _views.py_ file. Everything else can be deleted.

The views.py (meeting-planner/website/views.py) file is where we will create our views for this project. But before we have to configure the settings so that Django knows about it in _settings.py's_ INSTALLED_APPS setting. We'll add the app name to the INSTALLED_APPS list. It should look like so:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
```

### Adding the view
A view is a django component that responds to requests for a webpage. In views.py we'll create welcome function that just returns an HttpResponse with some text like so:

```
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Hello there! Welcome to the Meeting Planner")
```

Here we are importing the HttpResponse class from django so that it can be used.

### Adding the url
So there has to be a way we get to the view, we'll need to configure the _urls.py_ so that the resource we created (the welcome function in _veiws.py_) can be visited. We'll go into the _urls.py_ file and add a path in the urlpatterns array. The code should look like so:

```
from django.contrib import admin
from django.urls import path

from website.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome.html', welcome)
]
```

You see that we are importing the _welcome_ function that is in _website/views.py_. The path method takes in a string function for the pattern and the welcome method.

> If you get red lines with a reference warning beneath welcome this likely means that pycharm doesn't know which is your root project. You can right-click on the meeting-planner project folder (not the app) and mark it as Source root.

If you run the server using the ```python manage.py runserver``` you can navigate to the ```http://127.0.0.1:8000/welcome.html``` and you should be greeted with a page with the text you outlined in the HttpResponse method that is returned by the welcome method.