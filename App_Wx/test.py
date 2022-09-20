import socket


def handle_request(client):
    buf=client.recv(9999)
    ans=buf.decode()
    print(ans)

def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("192.168.3.148",8888))
    sock.listen(5)
    while True:
        client,addr=sock.accept()
        handle_request(client)
        client.close()


if __name__ == "__main__":
    main()
