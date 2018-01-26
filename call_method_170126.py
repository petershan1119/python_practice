import time

class Timer():
    """
    Source: https://jupiny.com/2016/09/25/decorator-class/
    __call__: 클래스의 객체가 함수처럼 호출되면 실행되게 만드는 함수
    """
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.function(*args, **kwargs)
        end_time = time.time()
        print("실행시간은 {time}초입니다.".format(time=end_time-start_time))
        return result

@Timer
def print_hello(name):
    print("hello, "+name)

print_hello('python')