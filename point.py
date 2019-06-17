# class Point

class Point:

    count_of_instance = 1000  # 클래스 변수임 self를 통해야 instance 변수임

    def setx(self, x): # 자바는 생략할 수 있는데 파이썬은 self 생략하면 안됨
        self.x = x

    def getx(self):
        return self.x

    def sety(self, y):
        self.y = y

    def gety(self):
        return self.y

    def show(self):
        print(f'점[{self.x},{self.y}]를 그렸습니다.')

    @classmethod
    def class_method(cls):
        return cls.count_of_instance

    @staticmethod
    def static_method(): # 앞의 두 method들과 다르게 인스턴스나 클래스를 인자로 받지 않습니다.
        print('static method called')
