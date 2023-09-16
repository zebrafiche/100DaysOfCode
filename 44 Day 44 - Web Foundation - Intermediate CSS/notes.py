# 377 Day 44 Goals_ what you will make by the end of the day

# By the end of the day, we will be finishing off our personal webpage

# 378 What We'll Make - Stylised Personal Site

# Challenge -
# Create a new folder called CSS - Mysite
# An a new index html file
# Create a css folder and a css file inside
# Connect the css file with the html file

# In the new html file -
# Add the boilerplate (!#html + tab)
# Then add the link to the stylesheet -
<head>
    #Boilerplate code
    <title>Abdullah Al-Rafi</title>
    <link rel="stylesheet" href="CSS_Mysite/styles.css">
</head>

# In the new css file -
body {
    background-color: #FFF6DC;
}

# Note: the html was not linking with the css, adding a "/" before the link resolved the issue


# 379 What Are Favicons_
# Now your site shows no icon at the tab
# But Sean Halpin's does
# You can get/create similar icons from favicon.cc/favicon.io

# Went to a free website and downloaded a random icon in .ico file
# To add the file, just link it with the index file just like css -
< head >
< link rel = "stylesheet" href = "/CSS_MySite/style.css" >
< link rel = "icon" href = "/CSS_Mysite/math_format_professional_regular_icon_205169.ico" >
< / head >

# In Sean's site, there are blocks that viewers can scroll through and see
# How do we do that?
# Next Lesson


# 380 HTML Divs
# reset the css, delete the awful color you set for the body
# Insert Hi, as h1
# Insert your name, as p

# Now these are presented as separate elements in my website
# And not centered
# And not together

# Enter div
# Timestamp - 05:25

# Add div to the html, ignore the class for now
<body>
    <div class="">

    </div>
</body>
# Open the website in Chrome
# Go to chrome developer tools, find the div in the Elements tab
# You can see that it is 0 pixels high
# So div, this block, is currently invisible and has no effect on the overall website look
# In order for it to do something, we have to use CSS

# In the developer tools, go to styles
# Here you can temporarily change attributes to see what kind of change takes effect
# Added these two lines, while having the div selected in Elements tab
background - color: black;
height: 20px;
# Just to give div a height and maybe see it in action
# Yes a black block can be seen

# So the div is only there for you to structure and divide up your content

# The developer tools is just for testing basically
# If you refresh the site, everything that you have entered in the styles section disappears

# For lasting effect, you have to make the changes in the html

# Now divs are there so you can group all the paragraphs together
# Remember group/ungroup in powerpoint
# When you group, the resulting box that contains all the elements is just enough high to contain them all
# The div is just like that

# In the html, move the h1 and the p inside the div
# We can see in the chrome developer tools that the div now has a height, just enough to contain the h1 and the p

# Think of it like this, this is a shape in powerpoint that contains some desired text
# Now let's change the color of this shape
# go to css and change the background color of the div

div{
    background-color: #C8E4B2
}

# Now you will see that the div block contains a margin of sort, the texts do not start from the absolute edge
# There is a gap
# This is where User Agenet Stylesheets come into play
# user agent stylesheet is some default css set by the browser, to render a default view
# Again, open chrome developer tools
# select body
# you will see, in the style section, a "user agent stylesheet" section with some default styling values
# and below a visual representation of what it looks like

# you can edit the values too, temporarily of course
# select the visual representation, and modify the margin to 0

# You will see that the text inside our div block is now at the edge of the screen

# But there is a margin at the top still
# Go to the developer tools and select the element
# You can see that when you select h1, the user agent stylesheet shows a bunch of values
# Meaning they have default styling in case no specifics are provided at the html file
#
# TIP: Make the temporary changes in the developer tools, via the styles tab and the visual representation
#      the changes will reflect on the elments tab which will contain your html
#      you will be able to see what the changes in the visual entail in the html
#      and then you can edit the html yourself


# Challenge - change the html so that the text has no margins at the top, left and bottom

h1 {
    font-family: MV Boli;
    font-size: 400%;
    margin-top: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
}

body {
    margin-top: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
}

# In the lesson video however, Angela only added margin: 0px; so that all the margins get deletec together


# 381 The Box Model of Website Styling

# All the elements in an html are essentially boxes, with specific styling, i.e height and width
# This is how we specify the layout of our website
# Let's say we have an image and we set the css rule to 50%
# This essentially alters the box element that contains the image and thus the image size as well
#
# This principle is called the box model
# eg suppose a box has a width of 300 and a height of 300
# change the dimensions to 600x600
# this means that the box will now push other elements aside to expand itself
# These alterations can be done by specifying the px or the %
#
# We can also sepcify borders for these boxes
# When not specified, the borders are or width 3px
# they do not encroach on the box dimension, meaning no matter how you change this width, they will not bleed into the box
# But the changed element will have a bigger dimension
#
# change one border width
# border-top 0px
# change multiple
# border-width 0px 10px 20px 30px
#
# The box
# Itself, by default, the boxes do not have any dimensions
# They assume the dimensions to fit in the content
#
# Padding
# increase the size of the box
# creates distance between contents and the box inner edge
#
# Margin
# buffer zone between boxes

# Timestamp - 05:35

# Challenge -
# 2 divs
# called middle container and botton container
# Give the first div a class of top container
# 200x200px squares
# Each with diff background colors

# So, in the html -

<div class="top-container">
    <h1>
        Hi
    </h1>
    <p>
        I'm Rafi
    </p>
</div>
<div class="mid-container">

</div>
<div class="bottom-container">

</div>

# In the style.css, create a section called class selectors -

.top-container{
    background-color: #C8E4B2;
}

.mid-container{
    height: 200px;
    width: 200px;
    background-color: red;
}

.bottom-container{
    height: 200px;
    width: 200px;
    background-color: blue;
}

# id could have worked too, since there are only one of each type
# Although all the divs are set with a bg color of red in the tag selectors section, the class selectors get preference

# Challenge -
# 3 boxes 200x200px
# 1st box - 10px border and 20px padding
# 2nd box - 20px border
# 3rd box - 10px border

.top-container{
    background-color: #C8E4B2;
    height: 200px;
    width: 200px;
    border: 10px;
    border-style: solid;
    border-color: black;
    padding: 10px;
}

.mid-container{
    height: 200px;
    width: 200px;
    background-color: red;
    border: 20px;
    border-style: solid;
    border-color: black;
    margin-left: 240px;
}

.bottom-container{
    height: 200px;
    width: 200px;
    background-color: blue;
    border: 10px;
    border-style: solid;
    border-color: black;
    margin-left: 480px;
}

# Notes -
# 1. if you do not specify the border style to solid, you cannot see it
# 2. mid container accounted for the padding and margin of the top container
# 3. bottom container accounted for the padding and margin of both
# 4. adjusting the left marging shifts the elements to the left


# 382 CSS Display Property

# get some images and add them to the first div
# get rid of the margins done for the last challenge

# downloaded some images
# put the image of the sun right before the h1
        <img src="/CSS_Mysite/images/sun.png" width="50" height="50">
        <h1>
            Hi
        </h1>
# but the sun's image gets positioned right at the top of the "Hi"
# not beside it
# enter css display properties
# there are four types of css display properties -
# 1. Block
# 2. Inline
# 3. Inline-Block
# 4. None
# when you select the img in the chrome dev tool, you will see that it has a width equal to the image's width
# when you select the h1 in chrome dev tool, you will see that the h1 element takes up the entire width of the screen
# So the h1 element falls under the Block property of css display, they takw up the whole width of the screen
# essentially blocking other elements from sitting next to them

# Common Block Elements -
# Paragraphs
# Headers
# Divisions
# List and List items
# Forms

# How to insert the sun right to the left of "Hi"?
# Use an inline display element, i.e. span
# Think of insert, how it inserts things in between texts
# Span works like that
# You can use span to modify parts of a text as well
# Let's say I want to highlight the Rafi in I'm Rafi
# I can do it like this -
        <p>
            I'm <span id="rafi">Rafi</span>
        </p>
# Put that part inside span
# Give the span an id
# change the id styling in css
#rafi{
    background-color: yellow;
}

# Similarly, I can add the sun beside the text as well
        <h1>
            <span><img src="/CSS_Mysite/images/sun.png" width="50" height="50"></span>Hi
        </h1>

# Timestamp - 06:42

# Spans, like divs, do not do very much unless they are used in conjunction with css
# Inline elements take as much space as needed, not more like Block elements
# Common inline elements
# Spans
# Images
# Anchors(Links)

# Remember the links you put in your cv website? By default they occur in line with each other
# You can also have spans as standalones
    <div class="mid-container">
        <span>This</span>
        <span>is</span>
        <span>span</span>
    </div>
# You can see that the mid container now contains the line "This is span"
# And the width of each sppan is exactly the width of the word itself

# Then why don't we always use spans?
# You cannot change the width
# There is no width:{} function in css for span
# For Blocks there is

# But if you really want Blocks to be placed side be side, you can change the display property in the css
# In the html -
    <div class="bottom-container">
        <h3>
            This is here to demonstrate display properties
        </h3>
        <h3>
            Change the display property to inline
        </h3>
    </div>
# and in the css -
h3 {
    display: inline;
}

# You can see that the two h3 gets placed side by side

# Similarly you can set the display of your inline elements (eg span) to block elements
# display: block

# So Block elements let's you change their width, but do not let you place them side by side
# Change them to inline elements, you can place them side by side but you cannot change their widths

# What to do if you want to place elements side by side as well be able to change their widths at the same time?

# Enter Inline-block elements
# Let's say they are a subset of inline elements
# In the html -
    <div class="bottom-container">
        <h3>
            Display
        </h3>
        <h3>
            Property
        </h3>
    </div>
# and in the css -
h3 {
    display: inline;
    width: 80px;
}

# So we have covered three of the four display properties

# Let's talk about None
# When you set the display property of any element to none, it just simply does not show

# in the css id selector, change rafi's display property to none -
#rafi{
    background-color: yellow;
    display: none
}
# so rafi was the id given to the name Rafi
# now that the id display property has been changed to none, the name will not show

# there is another alternative to this none display property
# visibility: hidden;

# in the html -
        <p>
            I'm <span id="rafi">Rafi</span>here <span id="testing">to</span> serve
        </p>
# in the css -
#rafi{
    background-color: yellow;
    display: none;
}

#testing{
    visibility: hidden;
}

# You can see that when it is display:none the element completely disappears, as if it never existed
# When it is visibility: hidden; the element disappears alright, but it retains the space


# 383 CSS Static and Relative Positioning

# Even when you do not have any css, the html follows some default styling when it comes to your webpage
# We need to understand those, to be able to modify them to our choice

# Rule 1: Content is Everything
# If you have a short word, the span has a short width
# If you have a long word, the span has a long width
# Although blocks take up the entire width of the screen despite the word size, the height is still determined by the font size
# Therefore, your content is very important

# Rule 2: Order comes from code
# The order in which your website gets rendered comes from the way you write your code

# Rule 3: Children sit on top of parents
<div class="top-container">
    <h1>
        <span><img src="/CSS_Mysite/images/sun.png" width="50" height="50"></span>Hi
    </h1>
    <p>
        I'm <span id="rafi">Rafi</span>here <span id="testing">to</span> serve
    </p>

</div>
# In this case, first the div gets created
# on top of it, the children, h1 and p, gets placed

<h1>
    <span><img src="/CSS_Mysite/images/sun.png" width="50" height="50"></span>Hi
</h1>

# in the example above, first h1 gets rendered, then span, on top of h1

# These are the default layouts

# There are position properties in css that deals with these default layouts and change them
# There are four types of position properties
# Static
# Relative
# Absolute
# Fixed

# Static refers to the default positioning by the html
# Relative
# Now let's say, the image was somewhere in the static position, and from that position, we want to move the image a bit
# Meaning we want to move the image relative to the static position

# in the css -
img{
    position:relative;
    left:30px;
}
# this will move the image 30px to the left relative to the static positioning of the image
# you can use top, bottom, left and right to set the positioning

# Note - in relative positioning top does not mean the element will move up
# It means everything other than the element will move up, resulting in a downward shift of the element
# And all the while, the focus will remain on the initial position of the element

# Therefore, if your element is on the right edge of the screen
# And it set the position to relevant in css
# And you set the positioning to right: 200px
# The entire screen will move right 200px, causing the element to shift left by 200px
# Also the focus will be on the initial positioning of the element
# So essentially you element will have shifted 200px to the left, out of the screen

# Challenge -
# Tinker with relative positioning, and
# 1. put all the divs in a row
# 2. bring the green div to the right

.top-container{
    background-color: #C8E4B2;
    height: 200px;
    width: 200px;
    position: relative;
    left: 400px;
}

.mid-container{
    height: 200px;
    width: 200px;
    background-color: red;
    position: relative;
    bottom: 200px;
}

.bottom-container{
    height: 200px;
    width: 200px;
    background-color: blue;
    position: relative;
    bottom: 400px;
    left: 200px;
}

# Note: Angela does it by first putting all the divs side by side using display:inline-block;
# This method works too


# 384 Absolute positioning

# It is basically kinda the opposite of relative positioning
# So when yo change the position of an to absolute -
position: absolute;
# and move the image to the right -
right: 300px;
# the image itself will now have a margin of 300px relative to the right margin

# Challenge -
# Place the divs diagonally, blue, red and cyan
# All the elements must touch each other at the corner

# First reset the elements to their initial position
.top-container{
    background-color: #C8E4B2;
    height: 200px;
    width: 200px;
}

.mid-container{
    height: 200px;
    width: 200px;
    background-color: red;
}

.bottom-container{
    height: 200px;
    width: 200px;
    background-color: blue;
}
#Second change each of their positions to absolute
# Note: When cyan's position gets changed, it gets placed on top, and red and blue take its previous place
# So you can see cyan and blue
# When red's (2nd container) position gets changed to absolute, it gets moves to the top and blue takes its prev place
# So you can see only red
# When blue's (3rd container) position gets changed to absolute, it is places at the top
# So you can see blue only (behind it are red and cyan respectively)

# Reposition them so they are touching corner to corner
# Also, in the css, set the margin of the body to 0 so that there is no default margin for the top container
# Already there actually, maybe I put it for something before and just forgot
body {
    margin-top: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
}
.top-container{
    background-color: #C8E4B2;
    height: 200px;
    width: 200px;
    position: absolute;
    top: 400px;
    left: 400px;
}

.mid-container{
    height: 200px;
    width: 200px;
    background-color: red;
    position: absolute;
    top: 200px;
    left: 200px;
}

.bottom-container{
    height: 200px;
    width: 200px;
    background-color: blue;
    position: absolute;
}

# Remember this -
# The positioning is relative to the parent
# So if you nest the mid-container inside another div -
<div class="parent_mid-container">
    <div class="mid-container">
        <span>This</span>
        <span>is</span>
        <span>span</span>
    </div>
</div>
# and give the parent div some dimensions -
.parent_mid-container{
    height: 400px;
    width: 400px;
    background-color: grey;
}
# the diagonal structure gets changed, the top leftmost cornered blue gets pushed down by red's new parent div
# and since we only specified position: absolute; for blue, not moving it anywhere, it assumes a position after the parent div
# to restructure -
.bottom-container{
    height: 200px;
    width: 200px;
    background-color: blue;
    position: absolute;
    bottom: 411px;
}
# why 411? why not 400?
# because bottom: does not mean how many pixels up from the prev position, but how many px from the bottom edge
# so initially, after it assumed a position after the parent div, it was 11 px from the bottom edge
# add to that the 400 that it needs to move upward by
bottom: 411px;
# Note: now if we move the red div, it will move relative to the parent grey div, not the body

# THE FIXED POSITION
# This basically keeps an element in a fixed position, even when you scroll down the webpage
# Demostration -
# Create a bunch of h1s in the html
# Change the blue container's position to fixed in the set location
.bottom-container{
    height: 200px;
    width: 200px;
    background-color: blue;
    position: fixed;
    top: 0px;
}
# this means that the blue container is now fixed 0px from the top edge
# now if you scroll down, you will see that the blue container stays at the top corner


# 385 The Dark Art of Centering Elements with CSS

# Let's create a new html for your website

# index.html
# css/design.css

# All the elements - the text, the images are all left aligned
# let's center them
body {
    background-color: #E0EBE8;
    text-align: center;
}

# Now if I, for some reason, set the dimensions of an element
h1 {
    width: 10%;
}

# The text moves back to the ledt edge
# How to center it back?
h1 {
    width: 10%;
    margin: 0 auto 0 auto;
}

# We could also write the code like this -
h1 {
    width: 10%;
    margin: 0 auto;
}

# Now I want to take the sun and the cloud that are side by side
# and align them such that the cloud is on top of the sun

#sun {
    position: relative;
}

#top_cloud {
    position: absolute;
    top: 90px;
    right: 275px;
}
# absolute positioning takes the element out of the html flow

# Challenge -
# Place two clouds on the top of the mountain, one on the right, one on the left
# The right one is a little bit above the left one

# First, put them all in a div
<div>
    <img id="right-bottom-cloud" src="/CSS_Mysite/images/cloud1.png" width="10%" height="10%">
    <img id="left-bottom-cloud" src="/CSS_Mysite/images/cloud1.png" width="10%" height="10%">
    <img id="mountain" src="/CSS_Mysite/images/mountain4.png" width="50%" height="50%">
</div>

Then change the clouds positioning to absolute, puts them out of html flow -
#right-bottom-cloud {
    position: absolute;
    right: 200px;
    top: 280px;
}

#left-bottom-cloud{
    position: absolute;
    left: 180px;
}

# Finally change the positioning of the mountain to relative, puts it in center
#mountain {
    position: relative;
}
# position: relative; changes the position of the element relative to the parent element and relative to itself
# and where it would usually be in the regular document flow of the page.

# Absolute-positioned elements are completely taken out of the regular flow of the web page.
# Absolute positioning takes elements out of the regular document flow while also affecting the
# layout of the other elements on the page.


# 386 Font Styling in Our Personal Site

# By default, the broad kind of typeface family you can use are called -
# 1. cursive
# 2. fantasy
# 3. inherit
# 4. monospace
# 5. sans-serif
# 6. serif

body {
    font- family: verdana, sans-serif;
}

# this above means that the body font will be verdana primarily
# if the user's computer does not have this font, then it will revert to sans-serif

# Now that is not what I want, because I am thinking I designed my website correctly,
# where the user might see the website differently
# So there is a thing called web safe fonts
# These are font that mostly can be rendered in all computers correctly
# In reality, no font is absolutely 100% web safe

# Go to the website cssfontstack.com
# It lists all the major fonts in common usage and their usage rate
# For each font, their is a thing called the fallback
# Meaning which font to revert to, in case the user does not have the orescribed font, so the design is not significantly compromised

# In CSS, you might see a ruleset like this:
# html {
#   font-family: Lato, "Lucida Grande", Tahoma, Sans-Serif;
# }
# So to be really verbose here, what that rule is saying is:
#
#     I’d like to use the Lato font here, please.
#     If you don’t have that, try “Lucida Grande” next.
#     If you don’t have that, try Tahoma.
#     All else fails, use whatever you’ve got for the generic keyword Sans-Serif

# But that also, does not cut it
# What if I want others to see exactly the font that I want them to see?

# Embedding the font -
#
# Go to google fonts
# Select the fonts you like
# the panel on the left generates a code that you can just copy and paste in the head section of your html
# just beneath where you are linking the style css file with the html
# paste the code in there
# now the font is embedded
# The side panel also specifies the CSS rules to specify families
# Copy that and paste it as a comment in your css file
# Will come in handy when you're specifying which font to use in which section

# So like if you want to dismiss a font after you have embedded it
# Just go to google fonts
# Select the currently selected fonts, this will generate the custom link that you have used to embed
# Then remove the font you do not like now
# Then add if you want, another or two fonts
# Then copy the link
# Paste the link replcing the previous link in your website
# That's it
# You can also copy and paste the the CSS rules to specify families


# 387 Adding Content to Our Website

# You can use the stubcode.html provided in your website
# Its basically just a boilerplate code for your website
# You will create 5 divs, Intro, Experience, Skills, Education, Contact


# 388 CSS Sizing

# Firstly, change the font sizes not in px but in %
# This way the sizing will not get messed up if the user changes zoom level for web pages in his browser

# Apart from percentage, you can also use em
# It is a different em than the one we used in our html
# Basically it is the phoenetic representation of teh letter M
# 100% = 1em = 16px

# One thing you should remember
# Suppose you change the font size at the body of the website, in percentages
# Then you go on and increase the font size in the h1 in percentages
# The font will be doubly increased and will be gigantic

# To avoid the font getting doubly incerased, used rem instead of em
# It refers to root em
# So it tells the html than change the font size relative to the root em


# 389 Font Properties Challenge 1 - Change the Font Colour

# Set the text colour for the h1 and h2 to both be the colour with hex code: #66BFBF

h1 {
    font-family: 'Permanent Marker', cursive;
    font-size: 400%;
    width: 10%;
    margin: 0 auto 0 auto;
    color: #66BFBF;
}

h2{
    font-family: 'Permanent Marker', cursive;
    font-size: 1.5rem;
    color: #66BFBF;
}

# Set the text colour for the h3 and anchor tag to be the colour with hex code #11999E

h3{
    color: #11999E;
}

a{
    color: #11999E;
}


# 390 Font Properties Challenge 2 - Change the Font Weight

# Change all the h2 tags to have font weight: normal

h2{
    font-family: 'Permanent Marker', cursive;
    font-size: 1.5rem;
    color: #66BFBF;
    font-weight: normal;
}


# 391 Font Properties Challenge 3 - Change the Line Height

# Change the line height of the h1 to double what it currently is: 2
# line height is basically spaces between lines

h1 {
    font-family: 'Permanent Marker', cursive;
    font-size: 400%;
    width: 10%;
    margin: 0 auto 0 auto;
    color: #66BFBF;
    line-height: 2;
}


# 392 CSS Font Property Challenge Solutions

# 393 CSS Float and Clear

# lessons discussed here -
# margin: 0 auto 0 auto;
# text-align: left;
# line-height: 2;
# changing the dimesions of an image
# make text wrap around the image
#
# for this example, i will wrap the text around my photo in the intro section

#my-photo{
    border-radius: 50%
    border-style:solid;
    border-width:5px;
    float: left;
}

# timestamp - 07:52

# NB - the order of teh styling in the css is also important

# What if I want just the heading "Professional Experience" to appear to the left of the image?
# And the rest of the text to appear at the bottom?

# We can use another property called clear
# SO wrap the paragraph in an id or a class and in css set property clear: left;

# Float and clear can be dangerous
# Use it only when absolutely necessary


# 394 CSS Challenge

# In this lesson, Angela has a button generator
# We design the button and then copy and paste the code into our css
# create an element with a class='btn' and then paste the .btn code in css

# 395 Stylised Personal Site Solution Walkthrough

# In this lesson, Angela does the styling herself, for the learners to follow along
# Practice session, skipping it
