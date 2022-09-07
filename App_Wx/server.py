class Boat():
    def __init__(self, state):
        self.state = state


class Case():
    def __init__(self, no):
        self.item = []
        self.no = no
        self.state = 0

    def new_item(self, start_time):
        item = Item(start_time)
        self.item.append(item)
        self.state = 1


class Item():
    def __init__(self, start_time):
        self.start_time = start_time
        self.end_time = 0
        self.time = 0


class Control():
    num = 10  # ten boats

    def __init__(self, arr):
        self.boats = []
        self.cases = []
        for i in range(self.num):
            self.boats.append(Boat(arr[i]))
            self.cases.append(Case(i))
    
    def new_item(self,no,start_time):
        self.cases[no].new_item(start_time)


if __name__ == "__main__":
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    control = Control(arr)
    control.new_item(0, 1)
    print(control.cases[0].item[0].start_time)
    print(control.cases[0].state)
        