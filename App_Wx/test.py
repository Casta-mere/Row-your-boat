import socket


def handle_request(client):
    recv_data = client.recv(9999).decode("utf-8") 
    request_header_lines = recv_data.splitlines()
    message=request_header_lines[-1]
    print(message)
    response_headers = "HTTP/1.1 200 OK\r\n"
    response_headers += "\r\n"
    
    response_body = "hello world!"
    response = response_headers + response_body
    client.send(response.encode("utf-8"))


def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("10.96.229.74",8888))
    sock.listen(5)
    while True:
        client,addr=sock.accept()
        handle_request(client)
        client.close()


if __name__ == "__main__":
    main()
