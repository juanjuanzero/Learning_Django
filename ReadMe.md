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

If you run the server using the ```python manage.py runserver``` you can navigate to the ```http://127.0.0.1:8000/welcome.html``` and you should be greeted with a page with the text you outlined in the HttpResponse method that is returned by the welcome method. You actually got an error because there wasn't a resource in ```http://127.0.0.1:8000```. 

> When a web server is running. All it's doing is waiting for requests.

We'll add two other endpoints, a date and an about page by following the steps:
1. Go to the _views.py_ and add functions that take in a _request_ and return an HttpResponse
2. Go an update _urls.py_ to add url mappings (and import the view functions).

We'll also go ahead and change the mapping for the welcome page to an empty string '' so that requests to ```http://127.0.0.1:8000``` will lead there.  

views.py
```
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Hello there! Welcome to the Meeting Planner")

def date(request):
    return HttpResponse("This page was served at " + datetime.now)

def about(request):
    return HttpResponse("Hello, world. I am Juan")
```

urls.py
```
from django.contrib import admin
from django.urls import path

from website.views import welcome, datetime, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('date', date),
    path('about', about)
]
```
## Setting up a Data Model
Models and Migrations are core concepts to think about when dealing with the data model in Django.
* **Models** are python classes that maps to a database table. Each instance is an Entity.
* **Migrations** are an automated way to keep the structure of the db up to date with the model classes. It's not always automatic, as you'll need to write your own migrations if your project gets more complex.

So when you run the server in django you may have been getting a message like the following:
> You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

By default Django includes a slqlite3 db as part of your project, and the 18 migrations it is referring to are migrations for the default apps that come installed in Django. These apps are also listed in the INSTALLED_APPS array under _settings.py_. Its essentially saying: 
> "Hey your data model may not match what is in the db because there are unapplied migrations here".

We'll run the ```python manage.py showmigrations``` command to see our migrations. It will list out the migrations that have been created for each app that came with Django as default. Next we'll run ```python manage.py migrate``` to run all the currently pending migrations.

### Creating a Model Class
We now that we have our bearings, well go ahead and add another app into our project to contains all the meeting data for the meeting planner.

We'll run the ```python manage.py startapp meetings``` to create the meetings app. 

Once executed it will generate another app in your project. We'll create the models that this app will interact with in _models.py_. Don't forget to add it to _settings.py_! 

In _models.py_ we'll add a class called Meeting. The Meeting class will need to inherit from the Model class from Django so that it can be represented into the database. We'll also add a title and a date property. Both properties are defined by the methods called on the models module.

models.py
```
from django.db import models

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
```

Django will create the __init__ method for us in this Meeting class.

Next we'll need to create a migration so that the django can create the table for the Meeting entities. 

In the commandline:
```commandline
python manage.py makemigrations
```

The migration will find the meeting class and realize that its not in the sqllite db. A new file is added to the migrations folder of the meetings app folder. (If you don't see it right-click and select 'Reload from Disk'). 

The output of this is the _0001_initial.py_ file. If you inspect it there is a migration code that describes the creation of the Meetings table with the _title_ and _date_ fields in the database. There is also an id field that is created as the primary key of for each record in the db.

### Migrating our first migration
Next we'll go into creating a migration using the ```sqlmigrate <app> <migration_name>```.

In the commandline:
```commandline
python manage.py sqlmigrate meetings 0001
```
This generates the sql needed to be executed against the db. 

In order to run this migration against the db, we go back to the commandline and enter:
```commandline
python manage.py migrate
```
This runs all the _currently waiting_ migrations from all the INSTALLED_APPS in _settings.py_.

### Reviewing the Admin User Interface
With Django you get an admin interface that allows you to perform CRUD operations against your models in your project. For the app that we just created, we need to change the _admin.py_ file inside the meetings app folder.

meetings/admin.py
```python
from django.contrib import admin
from .models import Meeting

admin.site.register(Meeting)
```
We are importing the Meeting class into the admin.py and pass it into the admin.site.register method to get it setup for the admin screens. Once setup you  can add/edit/delete Meetings through the admin screen.

But you first need to log in as the admin. To do this you will need to create an admin account.

In the commandline:
```commandline
python manage.py createsuperuser
```
You will then be able to create a superuser account. Once you are ready, run the server, navigate to the ```http://127.0.0.1:8000/admin``` page, and log in. 

Once logged in add a few Meetings.

>THIS IS NOT YOUR SITE. THIS IS FOR ADMINS ONLY NOT USERS.

### Migration Workflow
Here is the workflow for future changes and when working with migrations.
1. Make sure the app is in INSTALLED_APPS
2. change the model code
3. Generate the migration script ```python manage.py makemigrations```
4. Review the migration script (VERY IMPORTANT)
5. Review other migrations by : ```python manage.py showmigrations```
6. Run the pending migrations by : ```python manage.py migrate```

### Adding more fields to Meetings
After reviewing the workflow we'll add two new fields to the Meetings model: _start time_ and _duration_. 

Here's a look at _meetings\models.py_
```python
from django.db import models
from datetime import time
# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
```
There are default parameters passed to define default values. If you were to migrate these changes without default values django will ask you for default values you can define at the time of migration.

Running through the workflow:
1. meetings app is already in INSTALLED_APPS
2. the model code has been changed
3. make the migrations, this created _meetings/migrations/0002_auto_20211017.py_
4. Reviewing looks like its adding the appropriate fields.
5. No other migrations are happening
6. Applying the migration.

### Other changes to models.
If you change the model's behavior by adding a method to it. Django will not detect any migrations (because there are any changes to make in the db).

Modifying _meetings\models.py_ to this does not create any new migrations
```python
from django.db import models
from datetime import time
# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} as {self.start_time} on {self.date}"
```

### Adding Another Model Class
We'll add a Room class inside the meetings app. The rooms will have a name, room # and what floor it is on. In _meetings\models.py_ 

We add the Room class:
```python
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} | Room {self.room_number} on {self.floor}"
```

We'll add a migration to so that the Room table can be added to the db.

We also want to reference a particular room in a meeting, We change the Meeting class to the following:
```python
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} as {self.start_time} on {self.date}"
```
The room property in the Meeting class will hold the room that the meeting will be held in. It's a ForeignKey to the Room a room object. 

There is an on_delete property here that tells django that if the room was deleted, that delete action will CASCADE into all meetings that reference it. It's basically saying:
>"Hey if i delete the room, then all the meetings that reference that room via this foreign key should also be deleted"

### A new db...
> You can only do this at the start of a project.
Create a migration for the room property on the Meeting class, when you migrate the migrations the django will ask you for default values in the Meeting class... if you dont want to do this, there is another way.

You can delete all the migration scrips in the meetings app folder and delete the slqlite db, then just start off from a fresh migration.

You'll need to create the superuser again.
