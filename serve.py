import socket
def main():
    host=socket.gethostname()
    port=12345
    serversocket=socket.socket()
    serversocket.bind((host,port))
    serversocket.listen(1)
    print("scoket is listening")
    while True:
        conn,addr=serversocket.accept()
        print("socket is get connection from %s"%str(addr))
        msg="get connection from"+"\r\n"
        conn.send(msg.encode("ascii"))
        conn.close()
if __name__=='__main__':
    main()
