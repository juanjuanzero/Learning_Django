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

## The Model, Template, View Pattern
This is also known as MVC. The components are:
* Models
* Templates
* View

First we'll change our welcome page...

### Convention for where templates fall.
We need to create own templates inside the app. For the website app folder, we'll add a templates folder to hold the templates for this app. Then we'll add another folder called website to prevent name clashes with other apps.

### Changing the Welcome Page
In our website\templates\website folder, we'll go ahead and add a html page and call it welcome. 

We add the following this welcome page looks like:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Learning Django</title>
</head>
<body>
<h1>Hello, world!</h1>
<p>This is my first Django app. This is on github at <a href="https://github.com/juanjuanzero/Learning_Django">my repo</a></p>
</body>
</html>
```
Next we update the welcome view function inside _views.py_ of the website app folder. The welcome function is updated to:

```python
def welcome(request):
    return render(request,"website/welcome.html")
```
This returns a render function that is imported by default in views.py. It takes in the request and the path to the html document. The render method here looks for a folder called _templates_ exactly.

### Adding Template variables
So now that we've seen that we can point to web pages (static sites) within the templates folder, the real power of this is passing in **template variables**. We'll make a few changes to the _welcome.html_ and _welcome view function_.

Updated welcome.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Learning Django</title>
</head>
<body>
<h1>Hello, world!</h1>
<p>This is my first Django app. This is on github at <a href="https://github.com/juanjuanzero/Learning_Django">my repo</a></p>
<span>{{message}}</span>
</body>
</html>
```
updated welcome view function
```python
def welcome(request):
    return render(request,"website/welcome.html", {"message": "hello world, this is a message from the view function!"})
```
When you run your server, you should see the ```hello world, this is a message from the view function!``` in the welcome page. It's not hard coded in the welcome page its being passed in as part of the render function that is returned from the view function. 

Btw, the passed in variable is called the **_context_**.

So you can see where this is going... you have a database, you have a way to show data, the next step is to just create a way to make changes to the data...

### Creating the Detail Page
So next we need to create a detail page, this will show the details of any meetings that we have. In the meetings app we'll add a view function called detail. 

First we'll create the templates\meeetings folder. Then add the detail page. Here is a look at the detail page:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Meeting: {{meeting.title}}</title>
</head>
<body>
<h1>{{meeting.title}}</h1>
<p>
    This meeting has been scheduled on {{meeting.date}}, at {{meeting.start_time}} in {{meeting.room}}
</p>
</body>
</html>
```

See how the properties of a meeting are accessed by the dot? Pretty cool!


meetigs\views.py
```python
from django.shortcuts import render
from .models import Meeting

# Create your views here.
def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request,"meetings/detail.html", {"meeting": meeting})
```
In the detail view function it accesses the objects collection in the Meeting objects and executes the get method to get the meeting with the matching id. Then that is passed into the render method to the detail page.

Next we update the url for the page in the meeting_planner app so that we can get to the detail page. This one will be a bit different since we'll want to have the ID to navigate to a meeting. Here is a look at the urlpatterns list in _urls.py_

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('date', date),
    path('about', about),
    path('meetings/<int:id>', detail)
]
```

#### What if there are invalid ids?
As you can see in the code for the detail view there's no way we handle invalid ids. Thankfully the django offers a good way to handle situations like this, we'll update the detail method to say the following

```python
from django.shortcuts import render, get_object_or_404

#.... other code

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request,"meetings/detail.html", {"meeting": meeting})
```

This is a built-in function that will return a 404 when a meeting id is no longer there.

## Building Urls, Listing Items
So now we have urls that we can navigate to but it would be nice to list them all. Django offers a way to iterate through a collection. We'll update the welcome screen to list out the meetings.

website\templates\website\welcome.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Learning Django</title>
</head>
<body>
<h1>Hello, world!</h1>
<p>This is my first Django app. This is on github at <a href="https://github.com/juanjuanzero/Learning_Django">my repo</a></p>
<ul>
    {% for meeting in meetings%}
    <li><a href="/meetings/{{meeting.id}}">{{meeting.title}}</a> on {{meeting.date}} {{meeting.start_time}} at {{meeting.room.name}}</li>
    {%endfor%}
</ul>
</body>
</html>
```

There is a ```{% for meeting in meetings%} ... {%endfor%}``` block of code here that will iterate through the meetings collection and render it on the page.

we'll also update the views.py of the website app for the welcome view function.

website\views.py
```python
def welcome(request):
    mtgs = Meeting.objects.all()
    return render(request,"website/welcome.html", {"meetings": mtgs})
```

### There is an anti-pattern here, enter Named Urls
You see how we hard coded the href tag in the welcome.html file? What if we needed to update the link to something else... and we had 100 pages that referenced that link? That would be bad. Thankfully, Django has Named Urls that we can use so that we'd only have to change it in one place.

We'll update the urls.py for the meeting detail page to pass in a name in the path method.

urls.py's urlpatterns
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('date', date),
    path('about', about),
    path('meetings/<int:id>', detail, name='detail')
]
```

Next we'll reference that in our welcome.html inside the href of the link:

```html
<ul>
    {% for meeting in meetings%}
    <li><a href="{% url 'detail' meeting.id %}">{{meeting.title}}</a> on {{meeting.date}} {{meeting.start_time}} at {{meeting.room.name}}</li>
    {%endfor%}
</ul>
```

Inside the href you see ```{% url 'detail' meeting.id %}``` this is a block that references an url with the name 'detail' and a parameter meeting.id is passed into the path. This is called a Named Url

I'll go ahead and add another page for good practice. I added the all rooms page. This has been added to the meetings app.

allRooms.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Learning Django</title>
</head>
<body>
<h1>All Rooms</h1>
<a href="{% url 'home' %}">Home</a>
<ul>
    {% for room in rooms %}
    <li>{{room.name}} | #{{room.room_number}} on {{room.floor}}</li>
    {% endfor %}
</ul>
</body>
</html>
```

urls.py's urlpatterns list
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='home'),
    path('date', date),
    path('about', about),
    path('meetings/<int:id>', detail, name='detail'),
    path('meetings/allRooms', allRooms, name='all_rooms')
]
```

Also added a view function in the meetings app.
```python
def allRooms(request):
    rms = Room.objects.all()
    return render(request, "meetings/allRooms.html", {"rooms": rms})
```

### There's another pattern emerging here.
When the application gets to be too large, it might be a better idea to have the urls scoped to the apps that way the project's urls.py's urlpatterns list won't be so large.

Django offers another way to keep things better organized. You can actually have a urls.py in your meetings app and then just reference them in the project's urls.py.

Here a look at the meetings\urls.py. Notice how it does not include the meetings\ prefix.
```python
from django.urls import path

from meetings.views import detail, allRooms

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('allRooms', allRooms, name='all_rooms')
]
```
In the project urls.py, we'll use the include method to reference the urls in the meetings.py. Here is the new project urls.py

```python
from django.contrib import admin
from django.urls import path, include

from website.views import welcome, date, about
from meetings.views import detail, allRooms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='home'),
    path('date', date),
    path('about', about),
    path('meetings/', include('meetings.urls'))
]
```
 So here, the last item on the list adds the meetings prefix to the urlpatterns list outlined in the meetings/urls.py file. So then we can keep all of our urls related to meetings in the same file.

## Stylin' all over the place
Django has a feature called **_Template Inheritance_** to apply the styles across your pages, so you only have to define your styling once.

We'll create a static file that will contain some of the styling for our page. We'll put this in the static folder of the website app.

website\static\website\first_style.css
```
body {
    font-family: sans-serif;
    color: cornflowerblue;
    background-color: floralwhite;
}
```

We'll create a base.html file that our website app will contain. We'll put this inside the templates folder of the app.

website\templates\base.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'website/first_style.css' %}">
</head>
<body>
{% block content %}
{% endblock %}
</body>
</html>
```
At the top you see the ```{%load static%}``` call and the link tag inside the head tag there uses the django templating to define the place where the styling is defined, which is inside the static folder of the website app.

You can see here that it has the django templating blocks. In the body tag you see the ```{% block content %}{% endblock %}```. This is where you will see the content in places that inherit from the _base.html_ file.

Next we'll modify the welcome page to inherit from the base.html file. Here is the changed welcome.html file.

website\welcome.html
```html
{% extends "base.html" %}

{% block title %} Welcome! {% endblock %}

{% block content %}
<h1>Hello, world!</h1>
<p>This is my first Django app. This is on github at <a href="https://github.com/juanjuanzero/Learning_Django">my repo</a></p>
<div><a href="{% url 'all_rooms' %}">All Rooms</a></div>
<ul>
    {% for meeting in meetings%}
    <li><a href="{% url 'detail' meeting.id %}">{{meeting.title}}</a> on {{meeting.date}} {{meeting.start_time}} at {{meeting.room.name}}</li>
    {%endfor%}
</ul>

{% endblock %}
```

At the very beginning of the file, there is a ```{% extends "base.html" %}```. This is what tells Django that this page, uses the base.html and extends it with what is inside the ```{% block content %}{% endblock %}``` of base.html. 

Here you can see that only the contents of the body tag remain in the welcome page. The contents are wrapped by ```{% block content %}{% endblock %}```. This is what tells Django what goes inside the block content.

All the other pages can extend base.html in their own way by defining what goes inside the content and title blocks. I'll go ahead and update the other pages.

## Is this even your final FORM?
A meeting application won't really be useful unless we are able to add more meetings in the future. Next we will add forms to our application so that we can add meetings.

This is a component feature of meetings so we will add it to our meetings app. We'll create a page that will hold the form, and call it new.html

templates\meetings\new.html
```html
{% extends "base.html" %}

{% block title %} Add a New Meeting {% endblock %}

{% block content %}
<h1>Add a New Meeting</h1>
<form>
    <table>
        {{ form }}
    </table>
</form>
{% endblock %}
```
Here inside the form and table tag, there is a form object being passed in. We'll talk more about that soon...

We'll add a new method to the view.py
```python
from django.forms import modelform_factory
#... more imports & methods
MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    form = MeetingForm()
    return render(request, "meetings/new.html", {"form":form})
```
Here we are importing a MeetingForm object that is a class that gets created from the modelform_factory class. In the new method, we instatiate the MeetingForm into a class and save it into a variable called _form_. That form is an object that gets passed into the view context which then renders input elements into the template.

We'll modify the urls.py in the meeetings app and add the url
```python
urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('allRooms', allRooms, name='all_rooms'),
    path('new', new, name='new')
]
```

Then we'll just add a link to the page from the welcome screen.

### Submitting the Form & Saving the Data
You'll need to add a submit button to the form because django does not add that for you. You'll also need to add the ```{% csrf_token %}``` which protects you from the cross site request forgery attacks into the form.

Here is the modified new template:
```html
{% extends "base.html" %}

{% block title %} Add a New Meeting {% endblock %}

{% block content %}
<h1>Add a New Meeting</h1>
<form method="post">
    <table>
        {{ form }}
    </table>
    {% csrf_token %}
    <button type="submit">Add Meeting</button>
</form>
{% endblock %}
```
Notice how the method in the form tag says post. This will submit the form to the same url where the form was created. We'll need to modify the new method to handle post requests when users submit the form.

new method in views.py
```python
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
```

Here we are processing requests as they are handled by the new method. 
* If the method is POST then we create a meeting form object from the request POST data and assign it to the form variable. If the form is valid, we save the data and redirect the user to the welcome page (using the named url)
* If the method is not POST, we create an empty meeting and store it in the form variable.

If it was not escaped during the submission. At the end we are taken to the new meeting page with the form variable.

## Adding a Delete Method
So now we are going to implement what we have learned so far and add a delete method, in case a meeting was created in error. All we'll do is add a way to delete a meeting in the detail page of the meeting. This will be a link that we click and once clicked we'll delete a meeting.

views.py
```python
def delete(request, id):
    meeting = Meeting.objects.get(pk=id)
    if meeting:
        meeting.delete()
    return redirect("home")
```

urls.py in the meetings app
```python
from django.urls import path
from meetings.views import detail, allRooms, new, delete

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('allRooms', allRooms, name='all_rooms'),
    path('new', new, name='new'),
    path('delete', delete, name='delete')
]
```

Here is a look at the detail page with delete meeting link:
```html
{% extends "base.html" %}

{% block title %} Detail {% endblock %}

{% block content %}
<h1>{{meeting.title}}</h1>
<a href="{% url 'home' %}">Home</a>
<p>
    This meeting has been scheduled on {{meeting.date}}, at {{meeting.start_time}} in {{meeting.room}}
</p>
<a href="{% url 'delete' meeting.id %}">Delete Meething</a>
{% endblock %}
```
## Adding an Edit method to modify the meeting
Next we'll go ahead and follow the same set of paths to modify a meeting. 

> We could use the new.html as it will be the mostly the same, but for the sake of simplicity we will just create another page for editing meetings

we'll create a editMeeting.html file in the meetings template app.

```html
{% extends "base.html" %}
{% block title %} Edit Meeting {% endblock %}
{% block content %}
<h1>Edit Meeting</h1>
<form method="post">
    <table>
        {{ form }}
    </table>
    {% csrf_token %}
    <button type="submit">Update Meeting</button>
</form>
{% endblock %}
```
You can see that it is very similar to the new.html with a few slight tweaks.

Next we'll add an edit method in the view.py
```python
def editMeeting(request, id):
    meeting = Meeting.objects.get(pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm(instance=meeting)
    return render(request, "meetings/editMeeting.html", {"form": form})
```
This method also looks a lot like the new method, the only difference here is in the else clause where we are trying to get a meeting to pass into the form when the request is a GET (not a POST). 

Here is a link to the [save method](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method) in the docs.

Next we'll add a url for in urls patterns list.
```python
from django.urls import path
from meetings.views import detail, allRooms, new, delete, editMeeting
urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('allRooms', allRooms, name='all_rooms'),
    path('new', new, name='new'),
    path('delete/<int:id>', delete, name='delete'),
    path('editMeeting/<int:id>', editMeeting, name='editMeeting')
]
```

And we'll add the link to edit the meeting in the detail page.
```html
{% extends "base.html" %}

{% block title %} Detail {% endblock %}

{% block content %}
<h1>{{meeting.title}}</h1>
<a href="{% url 'home' %}">Home</a>
<p>
    This meeting has been scheduled on {{meeting.date}}, at {{meeting.start_time}} in {{meeting.room}}
</p>
<div><a href="{% url 'delete' meeting.id %}">Delete Meething</a></div>
<div><a href="{% url 'editMeeting' meeting.id %}">Edit Meething</a></div>
{% endblock %}
```

And now we can add,edit,delete and see the details of our meetings. Nice Work!
