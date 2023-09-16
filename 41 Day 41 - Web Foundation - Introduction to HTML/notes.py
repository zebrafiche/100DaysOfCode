# 347 Day 41 Goals_ what you will make by the end of the day

# Over the next few sessions, we will learn how to create and scrape websites
# Using beautiful soup and selenium

# We have to have a good foundation on how to construct and website
# For that, we need HTML and CSS, the building blocks of any website

# For this, we will study the first four modules of Angela Wu's web development bootcamp

# HTML and CSS are two additional programming languages
# But fret not, the guide is here to make it as simple and easy for us as possible

# We are gonna be building a CV website

# Angela will be using Atom, a code editor for this project
# You can use PyCharm, it is all the same.

# Creating new HTML and CSS files
# Nothing complicated, just go to the sidebar > Project > (right click) New > index.html(type the extension, like .py)


# 348 How Does the Internet Actually Work_

# Think of a giant wire, that connects all the computer in the world
# So if a computer in Seattle wants to share some data with you, your PC can access it via the internet
# Some of these PCs need to be on 24/7 to feed data and files to computers around the world
# These are called servers and the PCs that get the data are called clients

# Imagine a giant library that is open 24/7, that's a seb server
# Now you can imagine if there's a library that's big enough to house all of these websites,
# then it's going to be pretty difficult to quickly locate the thing that you want out of this giant library, right?
# So how is this problem solved on the internet?

# Well, let's say that you're sitting at home on your computer and you type in google.com because
# you want to head over to the main Google homepage.
# What happens behind the scenes is that your browser will send a message to your internet service provider.
#
# So these are the people who you pay to be able to access the internet.
# And if you're in the US that's a company like AT&T or Comcast,
# and if you're in the UK, then that would be something like BT or Talk Talk.
#
# Now the message that you're sending the ISP is I want to see google.com and the
# ISP will then relay that message to something called a DNS server, a domain name system server.
#
# And a DNS server is essentially just a souped up phonebook.
# And what happens when you make that request through your browser is the DNS
# server will look up in its database as to what is the exact IP address of that website that you are trying to access.
#
# And every single computer that's connected to the internet has an IP address.
# This is like a postal for your computer so that when people need to send and receive files on the internet
# each computer can be located by their unique IP address. And once the DNS server finds the IP address,
# it sends that back to your browser. So now, you know the exact address where you can find the Google homepage.
#
# The next thing that happens is you will send a direct request to that address through your internet service provider.
#
# And this message will be delivered via what's called the internet backbone.
# Now the internet backbone isn't some sort of analogy for some clever Programming.
#
# It's literally the backbone of the internet.
# And if you head over the submarinecablemap.com, you can view all of the
# underwater cables that power the internet. And the internet is made up of these huge sprawling masses of wires
# connecting all of the world's internet users. As you can imagine,
# it's a pretty complex world out there. Now, if I'm sitting in London and I want to see a website that's hosted in the
# United States, then my browser would have to make a request that goes through one of these
# cables under the Atlantic ocean in order to reach the United States. And once that computer has received my request,
# they'll send back all of the relevant data, again,
# through these giant cables. And to navigate all of this crazy underwater and
# above water wires, all I have is an IP address.


# 349 How Do Websites Actually Work_


# Now, in order to access a webpage, we all know that you need a browser, right? And that can be Chrome,
# Safari, Firefox, whatever is your favorite one.
# These are all pieces of software that allow you to look up the IP address of
# your website and be able to receive data that it can render into this beautiful websites that we see.


# The data that you receive from the server usually consists of three types of files - HTML, CSS and Javascript
# The HTML code file is responsible for the structure of your web files
# You can use HTML to add an image/button/text box

# Then there are CSS files, these files are responsible for styling your website
# For example, the buttons defined in the HTML is given a color in CSS

# Lastly, the JavaScript(JS) code allows the websites to have specific behavior
# The button was constructed using HTML
# It was stylized by CSS
# Now it will get a function via JS

# So if we take the Google website as an example again, once we receive these files from Google server,
# when our browser loads up the HTML files, we'll get to see the structure
# of the website, namely, there's one image which has their logo, there's two buttons,
# and there's a text box where we can enter our search. Now, when we receive the CSS files,
# then that will modify the appearance of all of those components.
#
# We don't have any more buttons or any more images, but the now look the way that Google wanted it to. And finally,
# when we incorporate the JavaScript files, then our website actually starts having behavior. It has functionality
# and it's actually able to do something rather than just display some images and texts to us.


# 350 Optional_ Install the Atom Text Editor used in the Video Lessons (skipped, will use PyCharm)
# 351 Introduction to HTML


# So no matter what you use as your browser, it could be Chrome, it could be Safari or Firefox.

# They all have a single purpose and that's to interpret your files, such as your HTML files,
# CSS files, your JavaScript files into a website that should be displayed.

# HTML is the foundation for all websites
# You cannot create a website using only CSS or JS, but you can create a website using just HTML
# HTML - HyperText Markup Language
# The important word here it markup
# Because there's many markup languages. For example,
# you might have heard of things such as XML, extensible markup language,
# or GML, generalized markup language.

# And all of these languages share a common history. They're based off the markup
# that used to be put into manuscripts where editors would mock up the manuscript
# and either specify changes to the author or specify structure and layout to the publishers. So for example,
# you might have the squiggly line that shows the publishers that this part should be printed in bold,
# or this part should be printed in italics. And HTML works in much the same way.

# Go to codepen.io to play with real life HTML
# So you don't have to sign up, just head over to codepen.io and then hit create new pen.
# And then we're going to change the view to a format like this (vertical).
# So this is the live version of our website, and these are the places where we're going to put our code.
# So as you can see codepen lets you put in HTML, CSS, and JavaScript,
# which will together get interpreted and get shown on the left as your website.

# Now let's code some HTML
# Go to project gutenberg and find The Adventures of Sherlock Holmes book
# Open in plain text in one tab and HTML in another tab
# You can see that plain text is very, well, plainly structured, and the HTML has a bit more structure to it

# We will try to replicate the HTML version, by copy/pasting the plain texts in the codepen.io console

# In codepen, in the HTML editor - type -
# The Adventures of Sherlock Holmes
# by Arthur Conan Doyle

# It gets generated in the bland plaintext manner
# To get it to become the heading -

<h1>The Adventures of Sherlock Holmes
by Arthur Conan Doyle

# The <h1> changes it to heading text

# Timestamp 04:43

# So basically the syntax is like this - <type of element>
# It is really important to close the heading as well, <h1> denotes the start of the heading
# </h1> denotes the end
# Otherwise the editor thinks the entire text is in heading

<h1>The Adventures of Sherlock Holmes</h1>
by Arthur Conan Doyle

# Now, 'by' is a bit smaller than 'Arthur Conan Doyle', (both are smaller than the main heading)
# So,
<h1>The Adventures of Sherlock Holmes</h1>
<h3>by</h3> (smallest)
<h2>Arthur Conan Doyle</h2> (smaller)

# So you can decrement the heading element all the way upto h6, making it smaller with each iteration

# ACCESSING DOCUMENTATION
# Getting good at developing comes a lot to how much you can help yourself
# So, familiarize yourself with the documentation
# The preferred HTML documentation Angela uses is the MDN documentation (Mozilla Development Network)
# Also w3schools, and devdocs.io (which has docs for other languages too)

# Add spaces between the lines
Currently, the output has no spaces between the lines
<h1>The Adventures of Sherlock Holmes</h1>
<h3>by</h3>
<h2>Arthur Conan Doyle</h2>

to add spaces between the lines, add line breaks -

<h1>The Adventures of Sherlock Holmes</h1>
<br>
<h3>by</h3>
<br>
<h2>Arthur Conan Doyle</h2>


# 352 The Anatomy of an HTML Tag


# Now when you are constructing a website, you work with various tags - headings, breaks etc.
# Some of these require an open and close tag, i.e. <h2> & </h2>
# Some of these do not, <br>
# How do you figure if a tag requires closing or not?
# Documentation - devdocs.io
# In devvdocs.io, there is a section called "Tag omission" which clearlt states if the element requires closing or not

# Using the docs, insert horizontal lines above and below the portion of text
Currently -
<h1>The Adventures of Sherlock Holmes</h1>
<br>
<h3>by</h3>
<br>
<h2>Arthur Conan Doyle</h2>

# Add lines above and below using <hr> (Tag omission - does not require closing)

<hr>
<h1>The Adventures of Sherlock Holmes</h1>
<br>
<h3>by</h3>
<br>
<h2>Arthur Conan Doyle</h2>
<hr>

# Now we are trying to imitate the HTML page of the book in project gutenberg
# Their lines are a bit thicker than our lines, what have they done extra?
# In their website, hover your cursor above the line > right click > inspect
# We can see that their line is like this - <hr size="3" noshade>
# Read more at devdocs.io > HTML > attributes

# Now, align the entire text in the center -

<center>
<hr size="3" noshade>
<h1>The Adventures of Sherlock Holmes</h1>
<br>
<h3>by</h3>
<br>
<h2>Arthur Conan Doyle</h2>
<hr size="3" noshade>
</center>

# Adding comments inside the HTML code -
# just like in python, in HTML too you can add comments for other fellow programmers
# Instead of # use <!-- to open and --> to close
# <!--anything written here is the comment-->


# 353 What we're building - HTML Personal Site

# By the end of the day, we are going to be building a simple HTML personal website


# 354 What is The HTML Boilerplate_

# create a new html file, name it personal_website.html

# timestamp 07:26

# Structure of the boilerplate code
# <!doctype html> this specifies the type of the doc
# <html lang="en"> html open
# <head> head open
#     <meta charset="UTF-8">
#     <meta name="viewport"
#           content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title>Document</title>
# </head> head close
# the head holds information about the webpage and tells the browser how it should handle the page
# <body> body open
#
# </body> body close
# </html> html close
#
# The HTML code usually contains a head portion and a body portion
# Inside the head portion, there is a title section, where you set the title
# Let's change the title of the webpage to Abdullah Al Rafi
# The head portion also contains this line -
# <meta charset="UTF-8">
# It means that all the text in the webpage will be encoded in the UTF-8 system
#
# There are separate encodings for separate languages
# To render the characters in the languages correctly
# Sometimes when the encoding and the language characters do not match, they are jumbled up together
# This is called Mojibake
#
# Now UTF-8 includes all of those international symbols
#
# Now all these unicode symbols from various languages can be found at unicode-table.com
# Take a symbol from there, copy it, and paste it alongside your title (Abdullah Al Rafi)
# It gets generated when you load up the page again
#
# Read this article to learn the bare minimum unicode you should know as a software developer
# https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
#
# <meta charset="UTF-8"> means that it is the charset attribute of the meta element
#
# Go to a website and right click > inspect > search for description
# Toggle through different search results, one of them will contain the site description that you see when you google it
# And this is what search engines do, they crawl the HTML of your website and find what your website is all about to
# display it in the search result
#
# So to find out what different attributes meta can have, go to MDN webdocs, search for meta
#


# 355 How to Structure Text in HTML

# Go to John Kleinberg's personal website
# Let's follow that structure
# Add a h1 level heading, your name
# Indent it inside the body section, so we know that the heading is a child of the body
# Now add your profile/description, add it using a p tag
# From MDN Webdocs -
# <p>: The Paragraph element
# The <p> element represents a paragraph.
# Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank
# lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content,
# such as images or form fields.

# How to stylize the text
# Go to google for this
# for example,
# To change font, change this -
# <h1>Abdullah Al-Rafi</h1>
# to this -
# <h1 style="font-family:courier;">Abdullah Al-Rafi</h1>

# For example, in <p>, I want to change the text as well as the font size
# <p style="font-family:courier; font-size:90%;">Business Consultancy | SME Banking | Credit Risk Management</p>

# Italicize/Bold Text
# Just al <b></b> for bold and <em></em> for italicized
# Now there was also <i></i> that we could have used for italics
# But <em></em> tells the browser to put emphasis on the text in addition to italicizing
# Similarly there is the <strong></strong> tag that bolds and puts emphasis on the text
# As a thumb rule, it is better to use strong/em instead of b/i because strong/em actually assigns emphasis on the text,
# not just make it visually darker

# Using google, add image -
# just add this inside body element
# <img src="DSC_1667_2.jpg" alt="Photo" width="200" height="240">
# note - the image should be placed in the project folder first and the width and height adjusted to make it look good

# timestamp - 07:50

# Now add a profile
# Using the same method as before, i.e. <p></p>. Also add italic and bold wherever appropriate

# Add a horizontal line after the profile section
<hr size="3" noshade>

# After the horizontal line, insert another section titled professional experience
# Use a level three heading for the section header


# 356 HTML Lists
# HTML lists allow web developers to group a set of related items in lists.
# Unordered HTML List
# An unordered list starts with the <ul> tag. Each list item starts with the <li> tag.
# The list items will be marked with bullets (small black circles) by default:
# < ul >
#     < li > Coffee < / li >
#     < li > Tea < / li >
#     < li > Milk < / li >
# < / ul >

# Coffee
# Tea
# Milk

# Ordered HTML List
#
# An ordered list starts with the <ol> tag. Each list item starts with the <li> tag.
# The list items will be marked with numbers by default:
#
# < ol >
#     < li > Coffee < / li >
#     < li > Tea < / li >
#     < li > Milk < / li >
# < / ol >

# 1. Coffee
# 2. Tea
# 3. Milk


# 357 HTML Image Elements

<img src="DSC_1667_2.jpg" alt="Photo" width="200" height="240">
# The source can contain an online image link or a local path to an image
# The image must be stored at the project folder, where the html is
# alt is the alternative text that the website shows in case it fails to load the image
# If you are interested in SEO, you should properly name the image, don't just write "photo", but provide a clear description
# If you do not have any image of yourself online, you can upload one in PhotoBucket

# Tip - You can circle-crop your image, save it in the folder and use that path to get a circular image, right


# 358 HTML Links and Anchor Tags

# We already know how to add hyperlinks in the html
# What if I want to create a separate page for the Experiences section and hyperlink to that?
# Just like OOP
# Create a separate html file called Experiences
# Put all the experiences there
# Then create hyperlink on the main html, provide the name of the experiences html in the link section

# Also if you want to hyperlink your email address
# Just use the same method of adding hyperlinks, link - mailto: email address, text: email address

# THIS WILL CONTINUE ON THE NEXT DAY, DAY 42