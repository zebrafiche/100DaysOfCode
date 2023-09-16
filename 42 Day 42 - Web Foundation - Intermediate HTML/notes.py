# 359 Day 42 Goals_ what you will make by the end of the day

# We are continuing with HTML, and today we will learn some advanced concepts
# By the end of today's lesson we will create contact forms and create basic layout in HTML tables

# And in addition we will put in more elements in our CV website

# We will also get to publish our website


# 360 HTML Tables

# In the previous lesson we used simple HTML list format to list our experiences
# This time, we will do that using tables
# Create a new file named education.html

# The <table> HTML element represents tabular data — that is, information presented in a two-dimensional table
# comprised of rows and columns of cells containing data.

<table>
    <thead>
        <tr>
            <th colspan="2">The table header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>The table body</td>
            <td>with two columns</td>
        </tr>
    </tbody>
</table>

# This will create a two column table with heading "The table header"
# and a row containing "The table body" and "with two columns"

# We could have simply used the <th> inside the <tbody> and provided the header
# But that would have limited the table's functionality, like header freeze and stuff
# So it is better to always use proper segregation

# You might want to isolate the header and body to style them differently


# 361 Using HTML Tables for Layout

# Now currently, the layout of the top section of our digital resume is like this -

# Photo
# Name
# Tags
# Profile

# WHat if I want it to look like this? -

# Photo - Name, Tage, Profile
# So basically the description will be on the right of the photo

# We can do that by substituting the exisitng layout with a table
# So the left colume will contain the photo
# The right column will contain the description
# We can also add cellspacing argument to add some padding like spaces between elements

# So the intro section now looks like this -
#
# <body>
#     <table cellspacing="20">
#         <tr>
#             <td>
#                 <img src="DSC_1667_1-modified.png" alt="Abdullah Al-Rafi's Photo" width="250" height="250">
#             </td>
#             <td>
#                 <h1 style="font-family:tiempos text;">
#                     Abdullah Al-Rafi
#                 </h1>
#                 <p style="font-family:tiempos text; font-size:90%;">
#                     <b>
#                     Business Consultancy | SME Banking | Credit Risk Management
#                     </b>
#                 </p>
#                 <p style="font-family:tiempos text; font-size:80%;">
#                     <em>
#                     Experienced banking professional with a sound experience in areas of Project Management,
#                     Product Launch, Process Reengineering and Credit Risk Management.
#                         <br>
#                         Started career with <strong>IDLC Finance Limited</strong>. in their <strong>Credit Risk
#                         Management Division (Small Enterprise)</strong>.
#                         <br>
#                         Later worked for <strong>BRAC Bank Limited</strong>, the leading SME focused bank in the
#                         country, in the <strong>SME Product Team</strong>. Brought new and Innovative financial
#                         offerings to the market.
#                         <br>
#                         Currently working for <strong>Truvalu.enterprises Limited</strong>, a Netherlands-based impact
#                         investment company engaged in developing SMEs through equity investment and advisory services.
#                     </em>
#                 </p>
#             </td>
#         </tr>
#     </table>



# 362 HTML Tables Code Challenge


# 363 How to Type Emojis

# Method 2: Access Emoji in Windows 10 Using Keyboard Shortcut
#
# Put the cursor in any text field you’d like to insert an emoji. This could be Microsoft Word, Chrome, or Notepad app.
# Press the WIN + . (full stop) keyboard shortcut, or else the WIN + ; (semicolon). Either will open an emoji picker over
# the text field.
# Emoji are divided into several categories: smiley faces and animals, people, celebrations and objects, food and plants,
# transportation and places, symbols.


# 364 HTML Tables Solution Walkthrough

# Ok so this is how I did it -
<table>
    <tr>
        <td style="font-family:tiempos text; font-size:90%;">
            <strong>Python</strong>
        </td>
        <td>
            ★★★☆☆
        </td>
        <td style="font-family:tiempos text; font-size:90%;">
            <strong>Canva</strong>
        </td>
        <td>
            ★★★☆☆
        </td>
    </tr>
    <tr>
        <td style="font-family:tiempos text; font-size:90%;">
            <strong>HTML</strong>
        </td>
        <td>
            ★☆☆☆☆
        </td>
    </tr>
</table>

# Basically have four columns
# Column 1 Python
# Column 2 stars
# Column 3 Canva
# Column 4 stars

# However, Angela does it by nesting a table inside a table
# So a table with two columns and one row
# In the first cell -
# Another table with two columns and two rows (for two skills)

# How to Add Space Between Columns without Affecting Rows in an HTML Table?
# The “padding” property can be used to add extra space between columns. The space can be added between columns from the
# left or right side. In HTML, tables are utilized to display progress reports or for the state of the company.
# It helps to add extra space inside the cell, make data more prominent, and increase readability.

# Do it like this -
<tr>
    <td style="font-family:tiempos text; font-size:90%;">
        <strong>HTML</strong>
    </td>
    <td style="padding-left: 50px;">
        ★☆☆☆☆
    </td>
</tr>


# 365 HTML Forms

# The form element is a way to capture the user's input, feedback, mail etc.
<form>
    <label style="font-family:tiempos text; font-size:80%;">
        Your Name
    </label>
    <input type="text">
    <input type="submit">
    <br>
    <label style="font-family:tiempos text; font-size:90%;">
        Email
    </label>
    <input type="email">
</form>

# timestamp - 05:57


# 366 Forms in Practice - Create a Contact Me Form

# So as of now I am asking the users to submit their names, their emails and their confirmation on the data accuracy
<form>
    <label style="font-family:tiempos text; font-size:80%;">
        Your Name
    </label>
    <input type="text">
    <br>
    <label style="font-family:tiempos text; font-size:90%;">
        Email
    </label>
    <input type="email">
    <br>
    <input type="checkbox">
    <label style="font-family:tiempos text; font-size:90%;">
        The information provide are accurate to my knowledge
    </label>
    <br>
    <input type="submit">
</form>

# But I also want to capture the message if they want to leave me one
# We can do this using text area

<label style="font-family:tiempos text; font-size:80%;">
    Your Message
</label>
<br>
<textarea name="message" id="message" cols="60" rows="10">Type here...</textarea>

# timestamp 01:50


# Now I want the message to be sent to my email

# To send an email using HTML forms, you need to add the email id to the action attribute of the form.
# In that, add email proceeding with mailto: i.e. mailto:connect.rafiabdullah@gmail.com
# additionally add method and encoding type in there as well
<form action="mailto:connect.rafiabdullah@gmail.com" method="post" enctype="text/plain">
# Upon clicking submit, the message only shows message=Hello there, no name
# to enable that, specify the name to the name and email field
<label style="font-family:tiempos text; font-size:80%;">
    Your Name
</label>
<input type="text" name="name">

# and
<label style="font-family:tiempos text; font-size:80%;">
    Your Email
</label>
<input type="email" name="email address">

# Now when I click submit, the mail body contains -
# name=zebra
# email address=rough.rafi@gmail.com
# message=dard e disco

# Now when you press the submit button and nothing happens -
# See here - timestamp - 03:52

# Or consult the Q/A section of this lesson


# 367 [exercise] HTML Challenge

# You need to recreate an html that looks like this -
# Level 1 heading
# Horizontal rule
# Link to MDN docs
# Table(two columns and two rows)

# continued on the html.index file


# 367 Publish Your Website!

# Using github, yuss
# Read the doc -
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

# Basically you need to go to the settings of your repo, in this case v2_CV_Website
# Follow the doc from there

# It takes a little time for the website to get up, maybe half an hour
# Now if it is still not up -

# check if the main file is called index.html, not personal website
# this is important, github is going to look for a file in that name
# Unpublished the page
# How to republish?
# You can re-publish your GitHub Pages website by navigating to the Actions tab of your repository, click on the Pages
# build and deployment workflow, then click the Re-run all jobs button located in the upper right corner of the page.
# After the workflow run has completed, your site will be published.

#
# Now, there can be some issues -
# Make sure the linked files are in the same directory as the index.html
# Make sure the picture is in the project folder
# Make sure the spellings of the files/pictures are corrext


# fin