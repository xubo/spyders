
def wrapper1(func):
    def shape_func(args):
        print("start wrapper...")
        func(args)
        print("stop wrapper.")
    return shape_func

@wrapper1
def hello2(args):
    print("Hello")
    print(args)

hello2("asdfasdf")