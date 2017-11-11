# A proxy server written for python 3.6

import sys
import socket
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
        site_data = data.decode().split('\n')[0]
        print("site_data: ", site_data)
        url = site_data.split(' ')[1]
        print(url)
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

        forwardRequests(webserver, port, conn, data, addr)



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

            if len(reply) > 0:
                #Relay unfiltered message to the client
                print("type: ",type(reply))
                conn.send(reply)

                #Notify Proxy Server about the status
                status = float(len(reply))
                status = float(status/1024)
                status = "%.3s" % (str(status))
                status = "%s KB" % (status)

                print("Request done: %s => %s <= " % (str(addr[0]),str(status)))

            else:
                break
        forward_socket.close()
        conn.close()

    except Exception as err:
        print(err)
        forward_socket.close()
        conn.close()
        sys.exit()

initServer()
