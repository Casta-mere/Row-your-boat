
import Database_Conn
import datetime
import random


class Boat():
    def __init__(self, state):
        self.state = state


class Case():
    def __init__(self, no):
        self.item = []
        self.no = no
        self.state = 0
        self.time = 0
        self.number = 0
        self.maxtime = 0
        self.averagetime = 0

    def new_item(self, start_time):
        item = Item(start_time)
        self.item.append(item)
        self.state = 1

    def end_item(self, end_time):
        self.item[-1].end(end_time)
        self.state = 0
        self.time += self.item[-1].get_time()
        self.number += 1
        self.averagetime = int(self.time/self.number)
        if(self.maxtime < self.item[-1].get_time()):
            self.maxtime = self.item[-1].get_time()

    def is_free(self):
        return self.state == 0

    def show_Case(self, no):
        print(f"Boat No.{no} stats:\n\tTotal time:   {self.time//60} min(s)\n\tTotal items:  {self.number}\n\tMax time:     {self.maxtime//60} min(s)\n\tAverage time: {self.averagetime//60} min(s)")

    def output(self):
        ans = []
        for i in self.item:
            st, et = i.output()
            ans.append([self.no, st, et])
        return ans


class Item():
    def __init__(self, start_time):
        self.start_time = start_time
        self.end_time = 0
        self.time = 0

    def end(self, end_time):
        self.end_time = end_time
        self.time = self.end_time - self.start_time
        if(end_time < 3600*12):
            self.noon = "AM"
        else:
            self.noon = "PM"

    def get_time(self):
        return self.time

    def output(self):
        return self.start_time, self.end_time


class Control():
    num = 6  # six boats

    def __init__(self, arr):
        self.boats = []
        self.cases = []
        self.db=Database_Conn.mysql("Boat")
        self.colunms = "id int,start_time int,end_time int"
        self.table=str(datetime.datetime.now().strftime("%Y-%m-%d"))
        for i in range(self.num):
            self.boats.append(Boat(arr[i]))
            self.cases.append(Case(i))


    def new_item(self, no, start_time):
        if(self.cases[no].is_free()):
            self.cases[no].new_item(start_time)
            return "Borrow boat %d success" % no
        else:
            return("Boat %d is busy" % no)

    def end_item(self, no, end_time):
        if(not self.cases[no].is_free()):
            self.cases[no].end_item(end_time)
            return "Return boat %d success" % no
        else:
            return("Boat %d is't out" % no)

    def get_state(self):
        ans = []
        for i in range(self.num):
            ans.append(self.cases[i].state)
        return ans

    def show_state(self):
        print(self.get_state())

    def show_all(self):
        for i in range(self.num):
            self.show_case(i)

    def show_case(self, no):
        self.cases[no].show_Case(no)

    def output_all(self):
        ans = []
        for i in range(self.num):
            ans += self.cases[i].output()
        return ans

    def up_load(self):
        self.db.Create_table(self.table,self.colunms)
        data = self.output_all()
        for i in data:
            self.db.update_table(self.table,i)
    
    def down_load(self):
        data=list(self.db.get_data(self.table))
        for i in data:
            self.case(i[0],i[1],i[2])
        

    def case(self,no,st,et):
        self.new_item(no,st)
        self.end_item(no,et)

if __name__ == "__main__":
    control = Control([0, 0, 0, 0, 0, 0])
    
    control.down_load()
    for i in range(20):
        start = (random.randint(6*3600, 11*3600))
        id = int(random.randint(0, 5))
        control.new_item(id, start)
        control.end_item(id, start+random.randint(1*3600, 6*3600))
    for i in range(20):
        start = (random.randint(12*3600, 18*3600))
        id = int(random.randint(0, 5))
        control.new_item(id, start)
        control.end_item(id, start+random.randint(1*3600, 6*3600))
    control.up_load()
