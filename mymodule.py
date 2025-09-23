def my_add(a,b):
    return a + b

def my_sub(a,b):
    return a - b

class Character:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f'저는 {self.name}입니다.')

print(f"mymodule 안에서의 __name__ : {__name__}")


# 모듈을 불러올 때는 모듈의 이름이 입력됨. 이걸로 모듈에 대한 조건문 만들 수 있음.
if __name__ == '__main__':
    print(my_add(3,2))
    print(my_sub(2,5))
    wizard = Character("법사")
    wizard.speak()