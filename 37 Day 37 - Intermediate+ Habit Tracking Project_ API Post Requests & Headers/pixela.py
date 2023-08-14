import requests
import datetime

# in the pixela website you can see that the signing up is a six-step process
# Step 1 - Create your user account
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

# Step 2 - create a graph

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
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(graph_response.text)
# {"message":"Success.","isSuccess":true}

# What exactly are these headers?
# Just like a header in a document, it is a relevant piece of information
# You know how making api requests requires you to provide your api key as an argument?
# Well this is the same case here

# Step 3 - Get the graph!

# Browse https://pixe.la/v1/users/a-know/graphs/test-graph (replace 'a-know' with 'zebrafiche',
# 'test-graph' with 'graph1', and add .html at the end)
# You can see your graph now!

# comment out the graph creation request so running it again does not attempt to create the graph again

# Post a pixel

# first, use datetime to automate today's date
# import datetime
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

# print(today.strftime("%Y%m%d"))
# 20230626

# Another endpoint to post a pixel/activity
post_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}"

# activity amount in the form of an input
activity = input("How much did you work today?: ")

# The configurations, just like before
post_config = {
    'date': today.strftime("%Y%m%d"),
    'quantity': activity
}

# The header stays the same
# Now for the request
post_response = requests.post(url=post_endpoint, json=post_config, headers=header)
print(post_response.text)
# {"message":"Success.","isSuccess":true}

# go to the graph url again and see the activity pixel in the graph, nice

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
update_response = requests.put(url=update_endpoint, json=post_config, headers=header)
print(update_response.text)

# delete a pixel

# endpoint to delete a pixel activity - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

delete_date = input("Which date do you want to delete?(YYYYMMDD): ")
delete_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{delete_date}"

# header stays the same
# no config because we are straight up deleting, so no arguments(parameters) required

# Now for the request, but this is request.delete()
delete_response = requests.put(url=update_endpoint, json=post_config, headers=header)
print(delete_response.text)

# so we run this everyday with the account creation and graph creation blocks of code commented out
# otherwise it would create a new account and a new graph everyday