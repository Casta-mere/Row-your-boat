
class Control():
    num=10 # ten boats
    class Boat():
        def __init__(self,state):
            self.state=state

    class Case():
        def __init__(self,no):        
            self.item=[]
            self.no=no
            self.state=0

        class Item():
            def __init__(self,start_time):
                self.start_time=start_time
                self.end_time=0
                self.time=0

        def new_item(self,start_time):
            item=Item(start_time)
            self.item.append(item)
            self.state=1
            



    def __init__(self,arr):
        