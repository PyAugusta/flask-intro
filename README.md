# Introduction to Flask - Web Development with Python #

## Presented by PyAugusta #

Welcome to PyAugusta - The CSRA's Python User Group. 

For this session, we'll be learning the basics of Flask - one of the most popular web development frameworks for Python. If you'd like to follow along, open up a command prompt and your favorite text editor and get ready to type. Or, if you're familiar with Git, clone this repository and examine the code.

## Outline #

1. Getting Setup with venv

2. A Basic Flask App

3. The Flask Project Structure

4. Static Files

5. Jinja Templates

6. Putting It All Together

7. Conclusion

## Getting Setup with venv #

When starting a new Python project, it's often a good idea to do so using a *virtual environment* - one that is separate from your system's base Python installation. Doing so will ensure that any additional libraries that our project needs stay isolated and will keep our system and other projects "clean".

One way to do so is using the **virtualenv**, or **venv**. First, let's make sure we have venv installed using the command line.

```bash
$ pip install virtualenv
```

Now that venv is installed, let's create a new environment. First, we'll create a folder just to house our separate environments.

```bash
$ mkdir pyvenvs
```

Next, we'll navigate into that folder, and create a virtual environment just for our Flask application.

```bash
$ cd pyvenvs
$ python -m venv flaskapp
```

Once the virtual environment is created, we can start it by running the activate script.

**Windows**

```bash
$ flaskapp\Scripts\activate.bat
```

**Linux & Mac (maybe?)**

```bash
$ source flaskapp\bin\activate
```

Once activated, you're command prompt will start with the environment name like this: ```(flaskapp) $```. Now that we're in our new environment, lets install Flask.

```bash
(flaskapp) $ pip install flask
```

From now on, anytime we work on our project, we should ensure that commands are run from the activated ```flaskapp``` virtual environment.

## A Basic Flask App ##

Let's start by creating a project folder - we'll call our application **myapp**.

```bash
(flaskapp) $ cd ~
(flaskapp) $ mkdir myapp
```

Using your favorite editor, open a new file in the myapp directory called **myapp.py**. Put this code in it.

*myapp.py*

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to My Application</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```

So, what's all this doing? Well, after importing the *Flask* object, we initialized it into the *app* variable, using the *__name__* atrribute. We then defined a function that returns the text we'll see on our application at the **/** route. The **if __name__ == '__main__'** block sets our code up to be runnable from the command line. So, let's try it out.

```bash
(flaskapp) $ cd myapp
(flaskapp) $ python myapp.py
```

If everything is right, you should be able to open up any browser and navigate to *http://localhost:5000/* and see the welcome message. Use Ctrl+c in the command prompt to stop the application.

## The Flask Project Structure #

Now, let's structure our application according to the standard Flask implementation. To keep everything neat, we need folders for static files, as well as any templates we'll be needing. From inside your myapp directory, run the following commands:

```bash
(flaskapp) $ mkdir static
(flaskapp) $ mkdir static/css
(flaskapp) $ mkdir static/img
(flaskapp) $ mkdir static/js
(flaskapp) $ mkdir templates
```

Your project structure should now look like this:

```
myapp/
  static/
     css/
     img/
     js/
  templates/
  myapp.py
```

## Static Files #

Our static directory is where we keep files that our application needs for front-end functionality and styling. Often times, these files can be excluded and instead of storing the data locally, our application can retrieve them from the internet. Since this session is focused on Flask, and not Javascript or CSS, we'll opt for the second option. Just remeber, that when it comes time to create custom functionality, your files should be stored here.

For our CSS and Javascript, we'll use Twitter's Bootstrap libraries. To do so, we'll need these links later on:

- https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css

- https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js

## Jinja Templates #

Now, you may want your application to deliver more than just simple welcome messages, and we certainly wouldn't want to type out huge strings of HTML in our Python code. Luckily, Flask supports Jinja templates, which is a way to generate and deliver reusable HTML files. The Jinja templating language is full of awesome functionality, but we'll stick to the basics.

Let's start by creating a file in the templates folder called layout.html. Put the following Jinja/HTML into the file.

*templates/layout.html*

```html
<!DOCTYPE html>
	<head>
		<title>My Flask Application</title>
    	{% include "resources.html" %}
	</head>
	<body>
		{% include "navbar.html" %}
		{% block content %}
		{% endblock %}
	</body>
</html>
```

If you've seen HTML before, much of this should look familiar to you. The Jinja (stuff inside the **{% %}** blocks) may be new to you though. The easiest way to explain it is to show you. We see that in the head of the document, we use **include "resources.html"**. So, let's create a new file called resources.html.

*templates/resources.html*

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" />
<script type="text/javascript" src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
```

Here, we simply define the appropriate tags to get our CSS and Javascript from the Bootstrap CDN. By keeping it separate, we can easily locate and change it in the future if we wanted to.

We also **include "navbar.html"**.

*templates/navbar.html*

```html
<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <a class="navbar-brand" href="#">My Application</a>
    <div class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <a class="nav-link" href="{{ url_for('home') }}">Home <span class="sr-only">(current)</span></a>
            </li>
        </ul>
    </div>
</nav>
```

In this template, you'll see that we use the **url_for** function, which is contained in **{{ }}** brackets. That will help us keep track of internal links. The arguments should match the names of the routing functions in myapp.py.

There's another bit of Jinja in the layout.html file that says **{% block content %}** and **{% endblock %}**. This is telling our layout that the content of the page will be put there. So, let's go ahead and make our content. Create a file called home.html.

*templates/home.html*

```html
{% extends "layout.html" %}
{% block content %}

<div class="jumbotron">
	<div class="container">
    	<h1 class="display-3">Welcome to my Application</h1>
        <p>This application is powered by Flask and uses Bootstrap 4 for styling.</p>
        <p><a class="btn btn-primary btn-lg" target="_blank" href="https://github.com/PyAugusta/flask-intro" role="button">Learn more &raquo;</a></p>
    </div>
</div>

{% endblock %}
```

## Putting It All Together #

Now that we have our templates written, let's make some simple updates to myapp.py.

*myapp.py*

```python
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
```

Now, instead of using our home function to return HTML, we'll use the render_template function to have it return our Jinja templates. When a user visits the **/** path (the home page), Flask will assemble all the files into a single HTML page. 

Just like before, start your application from the command line.

```bash
(flaskapp) $ python myapp.py
```

And visit http://localhost:5000/ to see your new site.

## Conclusion #

I hope you enjoyed this tutorial and are excited enough to learn more about Flask and Jinja. If you'd like, take the time now to use what you've learned to start adding more pages to your application. The code in this repository's myapp.py contains some comments to help you out.

Thanks!