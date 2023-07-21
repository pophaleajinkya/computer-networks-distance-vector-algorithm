import socket
import pickle
from dv_python import main as m

# TCP protocol
ClientMultiSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')
try:
    # JOIN message sent to the Server
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
    res = ClientMultiSocket.recv(1024)
while True:
    # message to be received from the server to each node for every iteration
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
    # import the distance vector algorithm from dv_python file
    reply = pickle.dumps(m('input2.txt'))
    # send the update message to the server regarding each iteration of distance vector algorithm of the node
    ClientMultiSocket.send(str.encode('UPDATE: Node-{}'.format(reply)))
    break
# if all the nodes distances are evaluated the connection closes
ClientMultiSocket.close()
