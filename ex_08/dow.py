han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # Guardian in a compound statement
    # 아래 두 조건의 순서를 바꾸면 Error 생김.
    # (최단평가 - 앞 조건이 True이면 뒤 조건은 생각하지 않는 -  때문...)
    if len(wds) < 3 or wds[0] != 'From' : 
        continue
    print(wds[2])