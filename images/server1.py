import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5005))
server_socket.listen(5)
import os

#address = "10.27.0.1"
client_socket, address = server_socket.accept()
print ("Connected to - ",address,"\n")

data = client_socket.recv(1024)
print ("The following data was received - ",data)
print ("Opening file - ",data)
img = open(data,'r')
while True:
            strng = img.readline(512)
            if not strng:
                break
            client_socket.send(strng)
img.close()
print ("Data Successfully Sent!")
exit()
        #data = 'viewnior '+data
        #os.system(data)
