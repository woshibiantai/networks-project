# A proxy server written for python 3.6

import os
import sys
import socket
import requests
import json
import time
from pprint import pprint
from _thread import *


maximum_concurrent_connections = 5 # Maximum number of concurrent conncetions held by the server
buffersize = 4096                  # Socket Buffer max size

# Get the port number you wish to listen on, manually input by the user
try:
    listen_on_port = int(input("Enter the port you wish to listen on: \n > "))
except KeyboardInterrupt:
    print("Keyboard Interrupt Detected! \n Exiting Proxy Application..........")
    sys.exit()

def initServer():
    try:
        # Initiate Socket, bind to port and start listening on port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.gethostname())
        sock.bind(('', listen_on_port))
        sock.listen(maximum_concurrent_connections)

        print("Sockets successfully initialized..........")

    except Exception as err:
        # Error handling if Socket fails to initialize

        print("Socket initialization failed........ \nExiting........")
        print(err)
        sys.exit()

    # Main loop
    while True:
        try:
            # Accept incoming connections
            conn, addr = sock.accept()
            print("new request received!")
            # Retrieve client data
            data = conn.recv(buffersize)
            start_new_thread(handleConnections, (conn, data, addr))

        except KeyboardInterrupt:
            sock.close()
            print("Proxy Server Terminating...........")
            sys.exit()


def handleConnections(conn, data, addr):
    # Request from user (connected to Proxy) will be processed in this function
    try:
        # print(data
        print("splitting...")
        site_data = data.decode("utf-8", "ignore").split('\n')[0]
        print("site_data: ", site_data)
        url = site_data.split(' ')[1]
        print("url: ",url)
        # Find the position of the ://
        http_position = url.find("://")

        print("http_position:", http_position)
        if(http_position == -1):
            temp = url
        else:
            print("entered else: ")
            temp = url[(http_position+3):] #Get the URL without the HTTP:// bit

        port_position = temp.find(":") # Get the position of the Port, if any

        webserver_position = temp.find("/") # Get the position of the webserver's end

        if(webserver_position == -1):
            webserver_position = len(temp)

        webserver = ""
        port = -1

        if(port_position == -1 or webserver_position < port_position):
            port = 80
            webserver = temp[:webserver_position]

        else:
            #In the event that a specific port is used
            port = int((temp[(port_position+1)])[:webserver_position-port_position-1])
            webserver = temp[:port_position]

        # forwardRequests(webserver, port, conn, data, addr)

        if("http://" not in url):
            url = "https://" + url
            print("updated url:", url)

        # MAX_RETRIES = 20
        #
        # session = requests.Session()
        # adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
        # session.mount('https://', adapter)
        # session.mount('http://', adapter)

        # while True:
        #
        #     try:
        #         r = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'})
        #
        #     except Exception as err:
        #         print("Connection refused by server")
        #         print(err)
        #         time.sleep(1)
        #         continue

        r = requests.get(url)

        print(r.text)

        conn.send(r.text.encode('utf-8'))



    except Exception as err:
        print(err)
        pass

def forwardRequests(webserver, port, conn, data, addr):
    try:
        forward_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        forward_socket.connect((webserver,port))
        forward_socket.send(data)

        while True:
            # receive reply from end target (webserver)
            reply = forward_socket.recv(buffersize)

            try:
                reply_as_string = str(reply,'utf-8')

                reply_as_string = modify_HTTP_response(reply_as_string, "prefs.json")

                print("reply: ", reply_as_string)

                modified_reply = reply_as_string.encode('utf-8')

                if len(reply) > 0:
                    #Relay unfiltered message to the client
                    conn.send(modified_reply)

                    #Notify Proxy Server about the status
                    status = float(len(reply))
                    status = float(status/1024)
                    status = "%.3s" % (str(status))
                    status = "%s KB" % (status)

                    print("Request done and sent to: %s , size: %s " % (str(addr[0]),str(status)))

                else:
                    break

            except Exception as err:
                print(err)
                conn.send(reply)

                break

        forward_socket.close()
        conn.close()

    except Exception as err:
        print(err)
        forward_socket.close()
        conn.close()
        sys.exit()

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

    if("<!DOCTYPE html>" in reply):
        reply_list = re.split("(<!DOCTYPE html>)", reply)

        # print("reply list: ", reply_list)

        for word in json_data["Wordlist"]:
            new_word = json_data["Wordlist"].get(word)

            reply_list[2] = reply_list[2].replace(word, new_word)

        reply = ' '.join(reply_list)

    else:

        # print('reply else:', reply)

        for word in json_data["Wordlist"]:
            new_word = json_data["Wordlist"].get(word)

            reply = reply.replace(word, new_word)


    return reply


initServer()