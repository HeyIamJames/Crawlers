#reconnaissance scanner python > txtfile
import os


#store results is new directory
def create_dir(directory):
    if not os.path:exists(directory:)
        os.makedirs(directory)


#new file to store results
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


#new