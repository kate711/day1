# 建立某节点的单向链表的算法
import sys


class student:
    def __init__(self):
        self.name = ''
        self.Math = 0
        self.English = 0
        self.no = ''
        self.next = None


head = student()
head.next = None
ptr = head
Msum = Esum = num = student_no = 0
select = 0

while select != 2:
    print('1 新增 2 离开')
    select = int(input('请输入一个选项： '))
    if select == 1:
        new_data = student()
        new_data.name = input('姓名：')
        new_data.no = input('学号：')
        new_data.Math = eval(input('数学成绩：'))
        new_data.English = eval(input('英语成绩：'))
        ptr.next = new_data
        new_data.next = None
        ptr = ptr.next
        num = num + 1

ptr = head.next
print()

while ptr != None:
    print('姓名：%s\t 学号： %s\t 数学成绩： %d\t 英语成绩： %d' % (ptr.name, ptr.no, ptr.Math, ptr.English))
    Msum = Msum + ptr.Math
    Esum = Esum + ptr.English
    student_no = student_no + 1
    ptr = ptr.next

if student_no != 0:
    print("----------------------------------")
    print('本链表中学生的数学平均成绩：%.2f 英语平均成绩：%.2f' % (Msum / student_no, Esum / student_no))
