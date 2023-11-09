
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


# def is_authenticated_decorator(function):
#     # wrapper will take the user object
#     def wrapper(user):
#         # condition to check if the user is logged in
#         if user.is_logged_in == True:
#             # if true, then function() will be executed
#             function(user)
#     return wrapper

def is_authenticated_decorator(function):
    # wrapper will take the user object, in this case declaring a tuple
    def wrapper(*args):
        # condition to check if the user(the first item in the tuple) is logged in
        if args[0].is_logged_in == True:
            # if true, then function() will be executed, with the user(the first item in the tuple) as an input
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)


