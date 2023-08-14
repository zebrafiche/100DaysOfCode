# 322 Day 37 Goals_ what you will make by the end of the day

# We will learn about advanced authentication methods using the header
# We will also learn how to put POST, PUT and DELETE requests using the requests module

# By the end of the day, we will have built a habit traker


# 323 HTTP Post Requests

# GET - requests.get()
# POST - requests.post()
# PUT - requests.put()
# DELETE - requests.delete()

# In requests.get() we send a request to an external system and get a response in return
# In requests.post() we provide some information to an external system and are not so interested in getting the response
# For example, google sheets has an API that lets you send data to google sheets, we are sending info to the system
# In requests.put() we update a piece of data in an external system, if we want to update sheets we will use this one
# Finally, in requests.delete() we delete a piece of data in an external system

# Today we will be using Pixela, where we will send info of our habits, using requests.get(), which will be tracked
# For signing up to Pixela we need to use some coding, create a new file - pixela.py
# 1. Create a user account in Pixela (Call /v1/users API by HTTP POST)

import requests

# in the pixela website you can see that the signing up is a six-step process
# Step 1 - Create your user account (Call /v1/users API by HTTP POST)
pixela_endpoint = 'https://pixe.la/v1/users'
# the documentation says that there are some required parameters too
# also the token code is up to you to create
user_params = {
    'token': 'tokenforthehabittrackingproject',
    'username': 'zebrafiche',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# Now pass in the arguments
# You do not use params in requests.post(). Since YOU are sending data, you use json as an argument
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@zebrafiche , it is your profile page!","isSuccess":true}

# comment the request out so further running this does not try to create a new account


# 324 Advanced Authentication using an HTTP Header

# Step 2 - Create a graph definition (Call /v1/users/<username>/graphs by HTTP POST)
# So essentially we send information through the API for pixela to grab it and create a graph
# And this time, now that we have created our user account, the endpoint is different - /v1/users/<username>/graphs
# Add to the pixels.py file -

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

# from the documentation, we need -
# Request Header - Key=X-USER-TOKEN ([required]the authentication token specified at the time of user registration.)
# Request Body - another set of parameters that will be passed on as a json argument

header = {
    "X-USER-TOKEN": f"{user_params['token']}"
}

graph_config = {
    "id": "graph1",
    "name": "training",
    "unit": "minutes",
    "type": "float",
    "color": "sora"
}
# Now for the request
response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(response.text)
# {"message":"Success.","isSuccess":true}

# What exactly are these headers?
# Just like a header in a document, it is a relevant piece of information
# You know how making api requests requires you to provide your api key as an argument?
# Well this is the same case here

# Step 3 - Get the graph!

# Browse https://pixe.la/v1/users/a-know/graphs/test-graph (replace 'a-know' with 'zebrafiche',
# 'test-graph' with 'graph1', and add .html at the end)
# You can see your graph now!


# 325 Challenge_ Add a Pixel to the Habit Tracker using a Post Request

# Step 4 - Post value to the graph (Call /v1/users/<username>/graphs/<graphID>)
# comment out the graph creation request so running it again does not attempt to create the graph again
# Post a pixel

# Another endpoint to post a pixel/activity
post_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}"

# The configurations, just like before
post_config = {
    'date': '20230625',
    'quantity': '100.0'
}

# The header stays the same
# Now for the request
response = requests.post(url=post_endpoint, json=post_config, headers=header)
print(response.text)
# {"message":"Success.","isSuccess":true}

# go to the graph url again and see the activity pixel in the graph, nice


# 326 Autofilling today's date using strftime

# in the pixela.py file, add
# use datetime to automate today's date
import datetime
today = datetime.datetime.now()
# concept - strftime
# from datetime import datetime
# now = datetime.now() # current date and time
# year = now.strftime("%Y")
# print("year:", year)
# year: 2018
# month = now.strftime("%m")
# print("month:", month)
# month: 12
# day = now.strftime("%d")
# print("day:", day)
# day: 24
# time = now.strftime("%H:%M:%S")
# print("time:", time)
# time: 04:59:31
# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)
# date and time: 12/24/2018, 04:59:31

print(today.strftime("%Y%m%d"))
# 20230626


# 327 How to use HTTP Put and Delete Requests

# in the pixels.py file, add -
# update a pixel

# endpoint to post a pixel/activity - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

update_date = input("Which date do you want to update?(YYYYMMDD): ")
update_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{update_date}"

# header stays the same
# capture update amount in the form of an input
updated_activity = input("How much did you work actually?: ")
update_config = {
    'quantity': updated_activity,
}

# Now for the request, but this is request.put()
response = requests.put(url=update_endpoint, json=post_config, headers=header)
print(response.text)

# delete a pixel

# endpoint to delete a pixel activity - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

delete_date = input("Which date do you want to delete?(YYYYMMDD): ")
delete_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{delete_date}"

# header stays the same
# no config because we are straight up deleting, so no arguments(parameters) required

# Now for the request, but this is request.delete()
delete_response = requests.put(url=update_endpoint, json=post_config, headers=header)
print(delete_response.text)

