from random import random
from tracemalloc import start
import boats
import datetime
import random
import Database_Conn as db

def to_second(time):
    return time.hour * 3600 + time.minute * 60 + time.second

if __name__ == "__main__":
    # arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # control = boats.Control(arr)
    # for i in range(20):
    #     start=(random.randint(6*3600,11*3600))
    #     id=int(random.randint(0,9))
    #     control.new_item(id,start)
    #     control.end_item(id,start+random.randint(1*3600,6*3600))
    # for i in range(20):
    #     start=(random.randint(12*3600,18*3600))
    #     id=int(random.randint(0,9))
    #     control.new_item(id,start)
    #     control.end_item(id,start+random.randint(1*3600,6*3600))
        
    # control.show_all()

    db.Create_Database("Boat"+str(datetime.datetime.now().strftime("%Y-%m-%d")))