import socket
import threading
import boats
import random
import datetime

def to_second(time):
    return int(time.hour * 3600 + time.minute * 60 + time.second)

def now():
    return to_second(datetime.datetime.now())

class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        b=boat_server()

class boat_server():

    def __init__(self):
        self.con()
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind(("10.96.229.74",8888))
        sock.listen(5)
        while True:
            client,addr=sock.accept()
            self.handle_request(client)
            client.close()

    def con(self):
        arr = [0, 0, 0, 0, 0, 0]
        self.control=boats.Control(arr)
        # for i in range(20):
        #     start=(random.randint(6*3600,11*3600))
        #     id=int(random.randint(0,9))
        #     self.control.new_item(id,start)
        #     self.control.end_item(id,start+random.randint(1*3600,6*3600))
        # for i in range(20):
        #     start=(random.randint(12*3600,18*3600))
        #     id=int(random.randint(0,9))
        #     self.control.new_item(id,start)
        #     self.control.end_item(id,start+random.randint(1*3600,6*3600))

    def handle_request(self,client):
        recv_data = client.recv(9999).decode("utf-8") 
        request_header_lines = recv_data.splitlines()
        message=request_header_lines[-1].split(':"')[1].split('"')[0]
        num,action=int(message.split(" ")[0][-1])-1,message.split(" ")[1]
        print(num,action)

        if(action=="A"):
            self.control.new_item(num,now())
            self.control.show_state()        
        elif(action=="U"):
            self.control.end_item(num,now())
            self.control.show_case(num)
        else :
            print("error")
        response_headers = "HTTP/1.1 200 OK\r\n"
        response_headers += "\r\n"
        
        response_body = "msg received!"
        response = response_headers + response_body
        client.send(response.encode("utf-8")) 
    
def server_thread():
    thread = myThread()
    thread.start()


