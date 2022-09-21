import socket


def handle_request(client):
    # buf=client.recv(9999)
    # ans=buf.decode()
    # print(ans)
    # client.send("ok".encode())
    # 接收对方发送的数据
    recv_data = client.recv(9999).decode("utf-8") 

    request_header_lines = recv_data.splitlines()
    message=request_header_lines[-1]
    print(message)
    # 返回浏览器数据
    # 设置返回的头信息 header
    response_headers = "HTTP/1.1 200 OK\r\n" # 200 表示找到这个资源
    response_headers += "\r\n" # 空一行与body隔开
    # 设置内容body
    response_body = "hello world!"
 

    response = response_headers + response_body
    
    client.send(response.encode("utf-8"))   #转码utf-8并send数据到浏览器


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
