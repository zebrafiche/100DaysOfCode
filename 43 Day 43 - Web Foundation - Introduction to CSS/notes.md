[//]: # (368 Day 43 Goals_ what you will make by the end of the day)

In this lession we will learn the basics on the CSS design language
By the end of the day, we will be styling our CV website





[//]: # (369 Introduction to CSS)

So before CSS, styling of a website was basically limited to HTML
Changing the font with <font>
Centering the text with <center>
Using text beside the profile picture using the table etc. which is very cumbersome

To augment this, people started using something called teh Cascading Style Sheets
ITs purpose was just to support HTML with the styling
Alone it is not worth much
That is how CSS was created




[//]: # (370 Inline CSS)

We will be working with the same index.html file of our website in this project
Let's change the background color of the website
We will have to change it in the <body> section
So this - 
<body>
becomes this, with CSS - 
<body style="background-color: #FBBC05;">
remember - inside quotes, hyphen, closing with a semicolon

We can see that the background color has changed to yellow
The argument also takes color name or rgb codes

Visit colorhunt.co for beautiful color palettes

Now let's say we want to change the style of the horizontal rule
We have quite a few of them in total
To change the styling, by adding code in each of them, is a bit cumbersome
Also very error prone
Solution - we can use internal CSS in that case





[//]: # (371 Internal CSS)

Basically we will outline the styling elements at the top, and everytime we need to change something, we do at the top
At the top meaning at the <head> section
So remove the body styling from where it was before
And add it at the head section -

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <style>
        body {
            background-color: #FFF6DC
        }
    </style>
    <title>💼 Abdullah Al-Rafi</title>
</head>

Remember - 
closing tage, i.e. </style>
put the style in the <head> section

Now we want to change the horizontal rule
Same way
<style>
    body {
        background-color: #FFF6DC;
    }
    hr {
        background-color: white;
    }
</style>

Nothing heppens
Because some default styling is already applied to hr
A look into google says the default styling for hr is sth like this below - 

display: block;
margin-top: 0.5em;
margin-bottom: 0.5em;
margin-left: auto;
margin-right: auto;
border-style: inset;
border-width: 1px;

We can see there is something like 
border-style: inset;

Let's look it up on the documentation

CSS Demo: border-style
border-style: none;
border-style: dotted;
border-style: inset;
border-style: dashed solid;
border-style: dashed double none;
border-style: dashed groove none dotted;

There is a whole bunch of border styles that we can change
Let's change the border style to none
    
<style>
    body {
        background-color: #FFF6DC;
    }
    hr {
        background-color: white;
        border-style: none;
    }
</style>

THE HORIZONTAL RULES DISAPPEAR

This is because initially the hr was 0 pixels high, with a border
Now it is 0 pixels high with no border
No wonder it does not show

In the style section, change the hr pixels to 2 px

<style>
    body {
        background-color: #FFF6DC;
    }
    hr {
        background-color: white;
        border-style: none;
        height: 5px;
    }
</style>

Now, we can see the horizontal rule, white

Like this, you can change the height of most other elements

Change the width of the horizontal rule to 100px
Well, not 100px
Change it to a percentage
The percentage denotes the portion of the screen the website is viewed on

<style>
    body {
        background-color: #FFF6DC;
    }
    hr {
        background-color: white;
        border-style: none;
        height: 5px;
        width: 60%;
    }
</style>

We can see that if we change the screen size by dragging the width of the hr adjusts accordingly

Timestamp - 13:59


Challenge - change the border style to dotted, placing the hr in the center

<style>
    body {
        background-color: #FFF6DC;
    }
    hr {
        background-color: #FFF6DC; to set the border color same as the page background, otherwise border bg stays white
        border-style: dotted none none; border style can be set in this order - top, side, bottom, so dotted none none, because I want dotted top only
        border-width: 10px; now that I have dotted top, I set the thickness of that dotted top
        border-color: lightgrey; 
        height: 50px; doesn't matter what you set, won't show, becauze the bg is same as page bg, and border sides and bottom have been set to none
        width: 10%;
    }
</style>


From the MDN documentation - 

The border-style property may be specified using one, two, three, or four values.

When one value is specified, it applies the same style to all four sides.
When two values are specified, the first style applies to the top and bottom, the second to the left and right.
When three values are specified, the first style applies to the top, the second to the left and right, the third to the bottom.
When four values are specified, the styles apply to the top, right, bottom, and left in that order (clockwise).

Now,

These changes we have done using CSS, these changes are only getting reflected in the home page
Not in the other pages, like Work Experience, Contacts
What we can do here is copy the style section into the head of those other pages too
But in this case it is simple as that
What if our website contained 50 pages? 100 pages?
That is where external CSS comes in




[//]: # (372 External CSS)

So far we have worked with internal CSS
Putting the style aspects into the html code itself
Now we are going to do external CSS
Think of OOP, it is kinda like that
The CSS now is going to be an external module


In the project directory, create a new folder named css
Inside that folder, create a file named styles.css

So move all the contents you have written under the <style> section so far into the styles.css
And then link the styles.css in the html, in the head section, same spot, like so - 

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>💼 Abdullah Al-Rafi</title>
    <link rel="stylesheet" href="css/styles.css">
</head>

do the same for the education, experience and contacts page too

Education - 
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Education - Abdullah Al-Rafi</title>
    <link rel="stylesheet" href="css/styles.css">
</head>

Experience - 
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Professional Experiences - Abdullah Al-Rafi</title>
    <link rel="stylesheet" href="css/styles.css">
</head>

Contacts - 
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Contact Details - Abdullah Al-Rafi</title>
    <link rel="stylesheet" href="css/styles.css">
</head>


This is called external CSS

Challenge -
Change the h1 tag - Abdullah Al Rafi
and the h2 tag - Business Consultancy | SME Banking | Credit Risk Management

Into a different color that goes with the color palette

h1 {
    color: #322653;
}

h2 {
    color: #322653;

While you are at it, change the <a> too (links)

a {
    color: #322653;
}

Also changing the table structure, so that now the table contains three columns
1st column - Pic, adjusting the cell width too, to fit smaller screens
2nd column - Name and Deets, adjusting the cell width too, to fit smaller screens
3rd column - Links to other pages, adjusting the cell width too, to fit smaller screens
used margin-left for the second two links (Education and Contact) to space out the links some
Also moving the skills section to education, since that page is almost empty
Finally, removed the links at the bottom(commented out), since all of them are now at the top

Timestamp - 05:23





[//]: # (373 How to Debug CSS Code)

So in the video, Angela says to copy all the contents of the file "Debugging Problem 1"
And paste it in the index file (keep a copy of our contens prior)
We should see that all our styling has disappeared
But, does not happen in this side
Probably because I did not follow Angela's instructions to the letter
And added my own elements here and there too

So we are gonna go ahead with the video nonetheless

So in the video the index file (the one with the flawed html code) was loaded on chrome
Then chrome developer tools was opened
The console tab showed that a file could not be accessed 'styles.css'

Now time to load up the second one - Debugging Problem 2
In this one, the background color, as set by the css file, was not applying
So a close look revealed that despite the styles.css, the body contained style="background-color: white"
So, removed that and everything was a okay

So what is the order of importance?
The inline CSS comes first, meaning the code looks at the inline styling first
Then comes the internal CSS, meaning if no inline CSS is present, then internal CSS is applied
Lastly, the one we have, ie external CSS




[//]: # (374 The Anatomy of CSS Syntax)

CSS syntax looks like this - 

selector{property: value;}
who{what: how;}

Challenge - Bacon Website
Get the Bacon Fansite folder from the course resources
Inside the folder, you will get a CSS file
Create a style.css file inside this folder and link it with the index file, using external CSS

change the background color
also,
the picture was not loading because the picture link was broken
so I went ahead and got a transparent bg pic from bing, and used its link
I also set the width and height to 20% so it fits the website better

<body>
  <h1>I Love Bacon</h1>
</body>

Change this h1 tag to red
also, change the font size

h1 {
    color: red;
    font-size: 300%;
}

Now, imagine that you have a lot of properties here
So this list will be loong
When it is time to debug, you will have trouble finding the right property
Thus, as a convention, it is best practice to list all the properties in alphabetical order

Timestamp - 10:01

Challenge - change the background of the picture to red as well

Simple, add this to CSS - 
img {
    background-color: red;
}

So magine you want to change something in the CSS sheet
The element or the who part is easy,
How do you figure out the correct syntax to affect the who/what part?

This is where you google and use the documentation
Especially, the CSS reference page in MDN web docs
If you click on each of the properties listed there, it takes you to another page detailing how you can change





[//]: # (375 CSS Selectors)

So far, we have only learnt how to change the elements using the tags, i.e. h1, h1, img etc.
What if I wanted to change specific elements?
Maybe one particular image?

Enter class

Let's put another image beside the image of bacon
Now, let's say that I want to change the background color of the bacon to green and that of the brocolli to red

What we do is, we assign specific classes to each of the image
And then, in CSS, we change the class property

So,
in index.html - 
<body>
  <h1>I Love Bacon</h1>
  <p>bacon, bacon, bacon, bacon, bacon, bacon</p>
  <p>bacon, bacon, bacon, bacon, bacon, bacon</p>
  <p>bacon, bacon, bacon, bacon, bacon, bacon</p>
  <img class="bacon" src="https://clipartcraft.com/images/bacon-clipart-simple.png" width="20%" height="20%" alt="bacon-img ">
  <img class="brocolli" src="https://w7.pngwing.com/pngs/18/601/png-transparent-broccoli-vegetable-cartoon-celery-food-leaf-cooking.png" width="30%" height="30%" alt="bacon-img ">
</body>
notice that the img elements now have classes


in the style.css file - 
note - when you refer to class selectors in css, you preceed with a dot

.bacon {
    background-color: green
}

.brocolli {
    background-color: red
}

So let's say there are multiple tags that should have the same theme, some h1, some h3 etc.
Assign the same class to them, and then change the class property in CSS





[//]: # (376 Classes vs. Ids)

Just like classes, we can also assign id to our tags
in the html file, add an id to the h1 - 
<h1 id="header">I Love Bacon</h1>
change its color in the CSS

So CSS syntax for id selectors start with #
#header {
    color: purple
}

So even though we have specifiec color for h1 as a tag selector at the top of the CSS file
The id selector takes precedence
And this is the same for class selectors too

If you go to the chrome developer tool > inspect > select the header you will see that the tag selector color has been crossed out
Because an id selector is there, that gets priority

So that is the similarity between class and id selectors
Uncomment the tag selector for the image and check, the class selectors for the image with take precedence

Differences between id and class - 
Diff#1
You can only use one instance of id in your page
example - now that you have used header id in the h1 tag, you cannot use header id anywhere else
let's say all h1 will have to conform to a certain style except one, you can use id for that

classes can have multiple instances
we have used classes in two instances in our page, for two images
works well when we want a certain number of h2 elements in a specific style, we can group them using class
for example, we could assign bacon class to multiple elements html, and change them in css

Another example,
imagine you are an element, then your class would be your name, there can be other classes by the same name
but your id is your passport number, only one unique passport number exists for you

Again, any of the class or id selectors will override any of the tag selectors

Another thing, the tags have some predefined styles from the browser end
You can see them at developer tools > user agent stylesheet
Those can be overridden using tag selectors, which can be overridden using id or class selectors

Diff#2
Any html element can have multiple classes but cannot have multiple ids
for example, in html i can add another class to the existing brocolli class, shape
<img class="brocolli shape" src="https://i.pinimg.com/originals/a5/65/01/a565019e605018a27ca99e0253ac5efc.png" width="10%" height="10%" alt="bacon-img ">
and then change the style of the class in the css sheet
.shape {
    border-radius: 50%;
}
However, you can only have one id

Last thing, 
There can also be pseudo classes
For these, nothing needs to be added to the html, only in the css
let's add in the tag selector - 
img:hover {
    background-color: yellow;
}
you can add these in any selectors, tags, classes, ids
this :hover pseudo class means the styling will change when mouse is hovered over that element

let's change some things in the personal website
I want the element color to change when mouse hovers over work, ed and contact
and the underline to disappear

from google - 
To remove the underline of a link, 
you can use CSS (Cascading Style Sheets) property text-decoration and set it to none.

Therefore - 
a:hover {
    color: #61677A;
    text-decoration: none;
}

Yep, works