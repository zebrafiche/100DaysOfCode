### 444 Understanding Backend Web Development with Python

How is it different from the generic web development with HTML and CSS?

Well that is a simple website.

A simple website only has a frontend.

But if you are building a website with some functionality, for example a web app.
Then there has to be a backend.
This is where complex calculations get carried out.

Full stack web development means front end plus back end.

There are different languages for different ends.
The front end mostly uses HTML, CSS and Javascript, whereas the backend uses Python, JS, Ruby, Java etc.

There are also different frameworks that you can use for the front and back end.

Frontend - Angular, React
Backend - Nodes, Flask, Django

These are basically tools that come with a lot of codes prebuilt for a lot of common functionalities.

When we are considering python backend, there is a whole myriad of frameworks that we can choose from.
These are Flask, Django, Bottle, Cherrypie etc.

The most popular ones are Flask and Django.
Flask is better suited for beginners.

There are three components to the backend - the client, the server and the database.

The client is the user and the frontend.
The server is basically a souped up computer that interacts with the requests sent by the client.
The database is a souped up spreadsheet that holds all the MIS in case the website deals with a lot of user data.

### 445 Create your First Web Server with Flask

Let's create the server using Flask.
Now flask is one of the most popular web development frameworks.

What is the difference between a library and a framework?

![Difference - Library and Framework](https://miro.medium.com/v2/resize:fit:550/0*6FmXM3_cFkEzhafa)

A good way to understand any new tech is to go through the doc.
Let's go to the flask documentation.

Create a new file called hello.py

A minimal flask application looks something like this - 
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
```
Process finished with exit code 0
```
So what did that code do?

    1. First we imported the Flask class. An instance of this class will be our WSGI application.

    2. Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

    3. We then use the route() decorator to tell Flask what URL should trigger our function.

    4. The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.


Where is my website?

To run the app, you need to let os know that this is your flask app, meaning you need to set up an environment variable.

In the terminal -
```
 set FLASK_APP=hello
 flask run
```

```
Error: Could not locate a Flask application. Use the 'flask --app' option, 'FLASK_APP' environment variable, 
or a 'wsgi.py' or 'app.py' file in the current directory.
```

So changed the name of hello.py to app.py. Now,
```
set FLASK_APP=app.py
flask run
```
```commandline
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Click on that ip address to go to the web server created using Flask.

When we go on and inspect the "Hello World" text, we can see that a full-blown HTML has been created.

We did not have to write the full HTML of the website, we just told with flask what we wanted to be printed onto the site.

So this is how flask works. You can send codes in flask and it will convert it into a website.

Until you press CTRL+C, this flask app is going to keep on running.
You cannot launch another flask app simultaneously.
So press CTRL+C to quit this app.


### 446 Understand the Command Line on Windows and Mac

The command line or the terminal is a very powerful tool.
It is a way of controlling the computer one line at a time.

This command line is also known as the shell.

So what is the shell?
Imagine your computer is a pistachio nut. The kernel inside is actually the meat of the computer.
It refers to the hardware of the computer. The outer shell is the medium through which you can interact with the shell.

There are two types of shells. There are the Graphical User Interface shells.
For example, the search function in the PC.
Then there are Command Line Interface shells.

This is an alternative way of interacting with the computer.

On Mac, there is a separate app called terminal to interact with the command line.
On PC, there is the Windows Powershell.

Below are some common commands you can run on the Powershell.

1. Print Working Directory
```commandline
pwd
```
```commandline
Path
----
C:\Users\DELL
```

2. List the files/folders in the working directory
```commandline
ls
```
```commandline
    Directory: C:\Users\DELL


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         12/5/2022   4:50 AM                .cache
d-----        12/18/2022   6:37 AM                .idlerc
d-----         1/29/2023   5:24 AM                .ipython
d-----          8/3/2023   6:43 AM                .keras
d-----          8/3/2023   6:36 AM                .matplotlib
d-----         6/30/2022   1:07 PM                .ms-ad
d-----         6/19/2023   4:25 AM                .vscode
d-----         4/17/2022   9:25 AM                .wdc
d-----         9/17/2023   5:06 AM                .wdm
d-r---          4/2/2022   3:09 PM                3D Objects
d-r---         5/18/2023   6:23 AM                Contacts
d-r---        10/21/2023   6:28 PM                Desktop
d-r---          7/5/2023   4:52 PM                Documents
d-r---        10/29/2023   5:46 PM                Downloads
d-r---         5/18/2023   6:23 AM                Favorites
d-r---         5/18/2023   6:23 AM                Links
d-r---         5/18/2023   6:23 AM                Music
dar--l        10/29/2023   5:52 AM                OneDrive
d-r---         7/22/2023  11:17 AM                Pictures
d-r---         5/18/2023   6:23 AM                Saved Games
d-r---         5/18/2023   6:23 AM                Searches
d-r---         5/18/2023   6:23 AM                Videos
-a----         6/26/2023   6:20 AM            103 .bash_history
-a----         6/26/2023   6:20 AM             64 .gitconfig
-a----        11/21/2022  11:46 AM             43 mapit.bat
-a----        11/21/2022  11:43 AM           2907 mapit.py
```

3. Change Directory

```commandline
cd .\Downloads\
```
You can type in partially and hit tab. That will autofill the possible choices.

```commandline
pwd
```
```commandline
Path
----
C:\Users\DELL\Downloads
```

4. Make a new folder called TEst.

mkdir - Make Directory
```commandline
mkdir TEst
```

```commandline
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        10/30/2023   6:28 AM                TEst
```

Change your current working directory to this new folder.

```commandline
 cd .\TEst\
 pwd
```

```commandline
Path
----
C:\Users\DELL\Downloads\TEst
```

5. Create a new file called main.oy inside TEst

```commandline
New-Item main.py
```
```commandline
Directory: C:\Users\DELL\Downloads\TEst


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        10/30/2023   6:38 AM              0 main.py
```

6. Delete a file

```commandline
rm main.py
```

7. Delete a folder

We are going to delete the TEst folder. We are inside the TEst folder now so need to move one folder up.

```commandline
Remove-Item TEst
```

Remember when you are inside the C:// drive, mess around with the PowerShell very, very cautiously.
There are lots of instances where people mistakenly deleted their entire computer data by being in the wrong directory.

There are lots of other useful command prompts. Google for them.


### 447 __name__ and __main__ _ Special Attributes built into Python

Let's understand what __name__ does.

```python
from flask import Flask
import random

print(random.__name__)
print(__name__)

print(Flask.__name__)
print(__name__)

#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
```
```
random
__main__
Flask
__main__

Process finished with exit code 0
```

We create codes or scripts for to purposes - 
1. To be imported as modules, to be used as a component in some other piece of code.
2. To be run directly

Whenever the Python interpreter reads a source file, it does two things:

    1. it sets a few special variables like __name__, and then
    2. it executes all of the code found in the file.

When Your Module Is the Main Program (for example, foo.py) -
If you are running your module (the source file) as the main program, 
the interpreter will assign the hard-coded string "__main__" to the __name__ variable, i.e.

```python
# It's as if the interpreter inserts this at the top
# of your module when run as the main program.
__name__ = "__main__"
```

When Your Module Is Imported By Another

On the other hand, suppose some other module is the main program and it imports your module. 
This means there's a statement like this in the main program, or in some other module the main program imports:

```python
# Suppose this is in some other main program.
import foo
```

The interpreter will search for your foo.py file (along with searching for a few other variants), 
and prior to executing that module, it will assign the name "foo" from the import statement to the __name__ variable, i.e.

```python
# It's as if the interpreter inserts this at the top
# of your module when it's imported from another module.
__name__ = "foo"
```

For a more detailed explanation, visit [this Stack Overflow explanation](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

### 448 Python Functions as First Class Objects_ Passing & Nesting Functions

The next thing we are going to delve into is the @ sign.
You might remember this line was in the module app.py

```python
@app.route("/")
```

What is this?
Well the forward slash is telling the code to go to the homepage (or in this case, declaring the home page).
Any web address that has the forward slash after it denotes to the homepage.

So that's the forward slash.

Now the "@" sign, in python, is called a decorator.

**What is a decorator?**
A decorator is a function that is used to insert additional functionalities to an already existing function.
You might have a number of functions in your class or module, and you need to add a certain functionality to each.
You can use the decorator function to do that.

Let's revisit functions, that will help us to better understand this.

```python
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
```

Now, what if we wanted to get a little bit fancier? 
Well, one of the things about Python functions is that they are known as first-class objects,
which basically means that you can pass a function around as an argument,
just like what you could do with an integer, a string or a float, it's treated identically.

_That means we can take these functions above, and we can build another function that uses these functions._

```python
##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)
```

Now, the next concept which you might've come across but haven't really used a lot is the concept of _nested functions_.
Functions can also be nested inside other functions.

```python
##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()
```

```
I'm outer
I'm inner
```

And now we have the problem of trying to call this function. 
Now, because this function was declared inside this function, its scope means that it's only accessible inside the confines of this function.

So if we were to go out of the function, so by indenting back to the beginning and try to call this nested function,
then it's actually not going to work. We're going to get a name error. It's not defined.


Now, one of the other things you could do is you can actually return a function from another function.
Functions can actually be returned from other functions.

```python
## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

outer_function()
```
```
I'm outer
```

The "I'm outer" got printed at the 2nd line of the code.

Now if we do this - 

```python
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


# outer_function()

inner_function = outer_function()
inner_function()
```

So now when I call this outer_function, the output that this line is going to evaluate to is going to become the nested_function. 
So you could almost store it inside a variable.

So let's say I create a variable called inner_function which is equal to the output of the outer_function,
which is basically this nested_function that's being returned.

**_Well then, not only can I trigger the outer_function which is just going to give me I'm outer,
I can also trigger the inner_function separately by calling it and then adding the activator which is the parentheses._**

```
I'm outer
I'm inner
```


### 449 Understanding Python Decorator Functions and the @ Syntax

So we've seen that functions can have functionality, inputs, outputs.
Functions are first-class objects and can be passed around as arguments.
Functions can be nested in other functions, and finally, functions can be returned as the output from another function.

We're finally ready to tackle the Python decorator.

So what the decorator does is it adds additional functionality(ies) to already existing function(s).

Let's say I have the functions below - 

```python
def say_hello():
    print("Hello")

def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")
```
Let's call say_hello()

```python
say_hello()
```
```
Hello
```

What if I want to delay the printing by two seconds, on all the functions?
Well I could do this -

```python
import time

def say_hello():
    time.sleep(2.0)
    print("Hello")

def say_bye():
    time.sleep(2.0)
    print("Bye")

def say_greeting():
    time.sleep(2.0)
    print("How are you?")
```

Or, I can use a decorator function to do do this efficiently - 

```python
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

say_hello()
say_bye()
```

In the decorator I have added multiple commands, delay the printing by two seconds and print twice.
So when there are multiple commands/functionalities that need to be added - decorators are a charm.

```
Hello
Hello
Bye
Bye
```

**Timestamp - 05:09**

This is what we saw when we were creating our Flask app.

**This @ sign is also known as syntactic sugar.**
**It refers to some syntax that you can write to make it easier to write an alternative piece of code.**

Currently, we are adding the code **@delay_decorator** before declaring the function, and then call the function itself.

But we could also do it like this - 

```python
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)
# delay_decorator(say_greeting) will return the modified function w/o the activator, we wiil just save it and activate it.
decorated_function()
```

So there are two ways of decorating a function - 
1. With the syntactic sugar
2. Without the syntactic sugar

```python
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()
```

Now using what we have learned so far, let's break down the code of the Flask app (app.py) - 

```python
# import
from flask import Flask

app = Flask(__name__)
# this becomes Flask(__main__), __main__ referring to this module here
# so Flask(this module), kinda like OOP

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
# @app.route is the decorator function, put before declaring hello_world() as a syntactic sugar
# app.route('/') means if the user visits the homepage

# don't always want to run the app using the terminal, use this -
# if this script is the main module, run the app
if __name__ == "__main__":
    app.run()
```
Let's add another decorator -

```python
@app.route("/bye")
def say_bye():
    return "Bye"
```

This means that if someone goes to the 'https://_______/bye' then return "Bye" on the homepage.
Now run the app.

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
```

When you run the app, it gives you a server address that takes you to the homepage.
When you modify the address to add "/bye" it takes you to another page that says 'Bye'.

### 450 [Interactive Coding Exercise] Create Your Own Python Decorator

Starting code - 

```python
import time
current_time = time.time()
print(current_time)

def speed_calc_decorator():
    pass

def fast_function():
    for i in range(10000000):
        i * i
        
def slow_function():
    for i in range(100000000):
        i * i
```

**Instructions**

time.time() will return the current time in seconds since January 1, 1970, 00:00:00

Try running the starting code to see the current time printed.

If you run the code after a while, you'll see a new time printed.

e.g. first run:

1598524371.736911

second run:

1598524436.357875

The time difference = second run - first run

64.62096405029297

(approx 1 minute)

Given the above information, complete the code exercise by printing out the speed it takes to run the fast_function() vs the slow_function(). You will need to complete the speed_calc_decorator() function.

HINT: You can use function.__name__ to get the name of the function,

Solution(mine) - 

```python
import time

# current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        print(function.__name__)
        time_before = time.time()
        function()
        time_after = time.time()
        print(time_after-time_before)
    return wrapper_function


# with syntactic sugar
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


# w/o synctactic sugar
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_func_time = speed_calc_decorator(slow_function)
slow_func_time()
```
```
fast_function
0.33091044425964355
slow_function
3.3168418407440186
```

