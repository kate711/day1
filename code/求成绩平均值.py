number = []
while True:
    x = input('请输入一个成绩：')
    try:
        number.append(float(x))
    except:
        print('不是合法成绩')
    while True:
        flag = input('继续输入吗？（yes/no）')
        if flag.lower() not in ('yes', 'no'):
            print('只能输入yes或no')
        else :
            break
    if flag.lower() == 'no':
        break

print(sum(number)/len(number))