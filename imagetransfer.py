import os   
import sys,time 
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5005))
server_socket.listen(5)

client_socket, address = server_socket.accept()
print "Conencted to - ",address,"\n"

sb = '/mnt/sdcard/sb'

while True:
    files = os.listdir(sb)
    pages = 0;
    while (files):
    print '\nMaybe, pending work'
    for au in files:
        if (au.find('d')>-1): # searching for folder with a d
            os.chdir(sb+'/'+au)
            imgFiles = os.listdir(sb+'/'+au)
            images = [img for img in imgFiles if img.endswith('.jpg')]
            print '\n%s user done' %au
            client_socket.send(au)
            pages = 0;
            #copies all .img files in the folder from server to client
            for imgs in images:
                print imgs
                client_socket.send(imgs)
                file_name = open(imgs,'r')
                while True:
                    strng = file_name.readline(1024)
                    if not strng:
                        break
                    client_socket.send(strng)
                file_name.close()
                print "Data sent successfully"                      
                os.remove(sb+'/'+au+'/'+imgs)
                pages = pages + 1

            time.sleep(1)
            os.chdir(sb)
            os.rmdir(au)

        else:
            time.sleep(2) 
        exit()
