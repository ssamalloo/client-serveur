import socket,os
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("", 5005))
k = ' '
size = 1024


fname = input("Enter the filename of the image with its extension (e.g: filename.jpg,filename.png \n")
#client_socket.send(fname)
#fname = 'images/'+fname
fp = open(fname,'w')
while True:
            strng = client_socket.recv(512)
            if not strng:
                break
            fp.write(strng)
fp.close()
print ("Data Successfully Received!")
exit()
        #data = 'viewnior '+fname
        #os.system(data)
