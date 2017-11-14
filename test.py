
import os
import sys
import socket
import requests
import json
from pprint import pprint
from _thread import *



def modify_HTTP_response(reply, json_file):
    """
    Modifies HTTP response String
    :returns: response, as String
    """

    #Opens the json file and passes it in as a dictionary
    main_path = os.path.dirname(__file__)
    json_path = os.path.join(main_path, json_file)
    json_open = open(json_path)
    json_data = json.load(json_open)

    for word in json_data["Wordlist"]:
        new_word = json_data["Wordlist"].get(word)

        reply_list = reply.split("<!DOCTYPE html>")

        print(reply_list)


modify_HTTP_response("hello", "prefs.json")
