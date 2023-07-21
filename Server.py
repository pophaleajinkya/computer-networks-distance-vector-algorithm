import socket
import os
import pickle
from _thread import *
from dv_python import main
from ini_dv import position
ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 2004
ThreadCount = 0

#empty lists
router_list = []
router_list1 = []

try:
    ServerSideSocket.bind((host, port)) # bind the host and the port
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(6) # we use in tcp connection
def multi_threaded_client(connection):
    # if the client is connected to the server send the below message
    connection.send(str.encode('Server: JOIN message was Received and Accepted\n'))
    connection.send(str.encode('Router-{} Initial Distance Vector is {}'.format(list(position.keys())[0],position.pop(list(position.keys())[0]))))
    while True:
        data = connection.recv(1024)
        router_list1.append(address) # append all the addresses to a list
        response = data.decode('utf-8') # decode the message
        print(address[0] + ':' + str(address[1]) + ':    ' + response) # print the message sent by the node
        if not data:
            break
        connection.sendall(pickle.dumps(response)) # This function differs from send by blocking I/O until all the data is sent
        break
    connection.close()

while True:
    Client, address = ServerSideSocket.accept() # accept the node which wants to connect with the server
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    router_list.append(address[0] + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Client Number: ' + str(ThreadCount))
    print('Total connected routers are: {}'.format(router_list))
ServerSideSocket.close()