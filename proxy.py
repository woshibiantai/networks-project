# A proxy server written for python 3.6

import os
import sys
import socket
import requests
import re
import json
from _thread import *


maximum_concurrent_connections = 5 # Maximum number of concurrent connections held by the server
buffersize = 4096                  # Socket Buffer max size

# Get the port number you wish to listen on, manually input by the user
try:
    listen_on_port = int(input('Enter the port you wish to listen on: \n > '))

except KeyboardInterrupt:
    print('Keyboard Interrupt Detected! \n Exiting Proxy Application..........')
    sys.exit()

def initServer():
    '''
    Initialize the Proxy Server
    :returns: None
    '''

    try:
        # Initiate Socket, bind to port and start listening on port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.gethostname())
        sock.bind(('', listen_on_port))
        sock.listen(maximum_concurrent_connections)

        print('Sockets successfully initialized..........')

    except Exception as err:
        # Error handling if Socket fails to initialize
        print('Socket initialization failed........ \nExiting........')
        print(err)
        sys.exit()

    # Main loop
    while True:
        try:
            # Accept incoming connections
            conn, addr = sock.accept()
            print('new request received!')
            # Retrieve client data
            data = conn.recv(buffersize)
            start_new_thread(handleConnections, (conn, data, addr))

        except KeyboardInterrupt:
            sock.close()
            print('Proxy Server Terminating...........')
            sys.exit()


def handleConnections(conn, data, addr):
    '''
    Request from user (connected to Proxy) will be processed in this function
    :returns: None
    '''

    try:
        # print('splitting...')
        site_data = data.decode('utf-8', 'ignore').split('\n')[0]

        if('GET' in site_data):
            print('site_data: ', site_data)
            url = site_data.split(' ')[1]
            print('url: ',url)
            # Find the position of the ://
            http_position = url.find('://')

            if(http_position == -1):
                temp = url
            else:
                temp = url[(http_position+3):] #Get the URL without the HTTP:// bit

            port_position = temp.find(':') # Get the position of the Port, if any

            webserver_position = temp.find('/') # Get the position of the webserver's end

            if(webserver_position == -1):
                webserver_position = len(temp)

            webserver = ''
            port = -1

            if(port_position == -1 or webserver_position < port_position):
                port = 80
                webserver = temp[:webserver_position]

            else:
                #In the event that a specific port is used
                port = int((temp[(port_position+1)])[:webserver_position-port_position-1])
                webserver = temp[:port_position]


            if check_websites_blacklist(url, 'prefs.json'):

                #If websites are blacklisted, return error-HTML code to browser
                error_header = 'HTTP/1.1 403'
                conn.send(error_header.encode('utf-8'))
                pass

            else:

                r = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'})
                print(r.status_code)
                reply_as_string = r.text
                reply_as_string = modify_HTTP_response(reply_as_string, 'prefs.json')
                conn.send(reply_as_string.encode('utf-8'))



    except Exception as err:
        print(err)
        pass


def check_websites_blacklist(url, json_file):
    '''
    Check if URL is blacklisted
    :returns: Boolean
    '''
    #Opens the json file and passes it in as a dictionary
    main_path = os.path.dirname(__file__)
    json_path = os.path.join(main_path, json_file)
    json_open = open(json_path)
    json_data = json.load(json_open)

    #Loop over all blacklisted sites and return Boolean:True if site is blacklisted
    for site in json_data['Blacklisted_sites']:
        if site == url:
            return True

    return False


def modify_HTTP_response(reply, json_file):
    '''
    Modifies HTTP response String
    :returns: response, as String
    '''

    #Opens the json file and passes it in as a dictionary
    main_path = os.path.dirname(__file__)
    json_path = os.path.join(main_path, json_file)
    json_open = open(json_path)
    json_data = json.load(json_open)


    if('<!DOCTYPE html>' in reply):
        #Check for the end of header, ensure that the header doesn't get modify, only the HTML section
        reply_list = re.split('(<!DOCTYPE html>)', reply)

        # print('reply list: ', reply_list)

        for word in json_data['Wordlist']:
            new_word = json_data['Wordlist'].get(word)

            reply_list[2] = reply_list[2].replace(word, new_word)

        reply = ' '.join(reply_list)

    else:
        #Assume that this is part of the HTML and not a header

        # print('reply else:', reply)

        for word in json_data['Wordlist']:
            new_word = json_data['Wordlist'].get(word)

            reply = reply.replace(word, new_word)


    return reply


initServer()
