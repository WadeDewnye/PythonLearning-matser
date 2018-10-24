
# 定义一个空的类
class Test01():
    # 定义空类,pass代表直接跳过
    # 此处pass必须要有
    pass

# 定义一个对象
mingyue = Test01()


class PythonStudent(Test01):
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'Python'

    def doHomeWork(self):
        print('I do homework ' + self.course)
        # 推荐在函数末尾使用return 语句
        return None

    def callAge(self):
        print('age = ' + str(self.age))


# 实例化
student = PythonStudent()
student.doHomeWork()
student.callAge()
print(PythonStudent.__dict__)
