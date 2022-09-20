import boats
import datetime

def to_second(time):
    return time.hour * 3600 + time.minute * 60 + time.second

if __name__ == "__main__":
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    control = boats.Control(arr)

    i=to_second(datetime.datetime.strptime("2020-12-01 12:25:25", "%Y-%m-%d %H:%M:%S"))
    # print(nowtime.strftime("%H:%M:%S"))
    control.new_item(0, i)
    control.end_item(0, to_second(datetime.datetime.now()))
    control.show_all()
    # control.new_item(0, 0)
    # control.end_item(0, 100)
    # control.new_item(0, 200)
    # control.end_item(0, 246)


    # control.show_all()
