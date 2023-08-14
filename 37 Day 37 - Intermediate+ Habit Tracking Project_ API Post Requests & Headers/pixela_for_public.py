import requests
import datetime
import os

# Step 1 - Create your user account
pixela_endpoint = 'https://pixe.la/v1/users'
# the documentation says that there are some required parameters too
# also the token code is up to you to create
user_params = {
    'token': os.environ.get('pixela_token'),
    'username': os.environ.get('pixela_username'),
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@zebrafiche , it is your profile page!","isSuccess":true}

# comment the request out so further running this does not try to create a new account

# Step 2 - create a graph

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

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

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(graph_response.text)
# {"message":"Success.","isSuccess":true}

# comment out the graph creation request so running it again does not attempt to create the graph again


# Post a pixel
def post():
    today = datetime.datetime.now()
    # endpoint to post a pixel/activity
    post_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}"

    activity = input("How much did you work today?: ")

    post_config = {
        'date': today.strftime("%Y%m%d"),
        'quantity': activity
    }

    post_response = requests.post(url=post_endpoint, json=post_config, headers=header)
    print(post_response.text)


# update a pixel
def update():
    update_date = input("Which date do you want to update?(YYYYMMDD): ")
    update_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{update_date}"

    updated_activity = input("How much did you work actually?: ")
    update_config = {
        'quantity': updated_activity,
    }

    # Now for the request, but this is request.put()
    update_response = requests.put(url=update_endpoint, json=update_config, headers=header)
    print(update_response.text)


# delete a pixel
def delete():
    delete_date = input("Which date do you want to delete?(YYYYMMDD): ")
    delete_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{delete_date}"

    # no config because we are straight up deleting, so no arguments(parameters) required

    delete_response = requests.put(url=delete_endpoint, headers=header)
    print(delete_response.text)


if input('Do you want to post new activity?: ') == 'Y':
    post()
if input('Do you want to update previous activity?: ') == 'Y':
    update()
if input('Do you want to delete activity?: ') == 'Y':
    delete()
