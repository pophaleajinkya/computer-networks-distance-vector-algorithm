from multiprocessing import Pool
import os

# create multiple nodes
Clients = ['u', 'v', 'w', 'x', 'y', 'z']


# Run this line to create multiple router nodes.
def run_clients(nodes):
    os.system(f'python client.py {nodes}')

if __name__ == '__main__':
    with Pool(6) as multipleprocess:
        multipleprocess.map(run_clients, Clients)
    print(multipleprocess)
