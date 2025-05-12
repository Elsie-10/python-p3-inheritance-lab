#!/usr/bin/env python

class User:
    # a constructor in python must be named __init__
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
my_user= User("my","User")
print(my_user.first_name)
print(my_user.last_name)