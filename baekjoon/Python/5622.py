#숫자 하나 누르면 다이얼이 처음 위치로 돌아가고 다음 숫자를 누르려면 다이얼을 처음위치에서 다시 돌려야함
# 숫자 1-> 1초

info = {
    1 : [[],[2]],
    2 : [['A','B','C'],[3]],
    3 : [['D', 'E', 'F'],[4]],
    4 : [['G', 'H', 'I'],[5]],
    5 : [['J', 'K', 'L'],[6]],
    6 : [['M', 'N', 'O'],[7]],
    7 : [['P', 'Q', 'R', 'S'],[8]],
    8 : [['T', 'U','V'],[9]],
    9 : [['W', 'X', 'Y', 'Z'],[10]]
}

io = input()

#시간
clock = 0

for a in io:
    for b in list(info.keys()):
        if a in info[b][0]:
            clock += info[b][1][0]
        else:
            pass
print(clock)


