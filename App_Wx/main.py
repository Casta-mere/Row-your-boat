
import datetime
import Database_Conn as database
import myserver

def to_second(time):
    return time.hour * 3600 + time.minute * 60 + time.second

if __name__ == "__main__":
    myserver.server_thread()
    
    
        
    # control.show_all()
    # db=database.mysql("Boat")
    # db.Create_Database()
    # print(to_second(datetime.datetime.now()))
    # db.Create_Database("Boat"+str(datetime.datetime.now().strftime("%Y-%m-%d")))