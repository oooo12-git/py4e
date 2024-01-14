fname = input("Enter file: ")
if len(fname) < 1 : fname = "clown.txt" # 기본값으로 clown.txt 사용
hand = open(fname) # 핸들 변수

di = dict()
for lin in hand:
    lin = lin.rstrip() # rstrip = 오른쪽 white space 제거
    wds = lin.split() # 빈 공간 기준 단어 나눠서 리스트 반환
    for w in wds:
        # ** idiom: retrieve/create/update counter **
        di[w] = di.get(w,0) + 1
# print(di)

# x = sorted(di.items())
# print(x[:5])

tmp = list()
for k,v in di.items() :
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)
# print("Flipped",tmp)

tmp = sorted(tmp, reverse=True)
# print("Sorted", tmp[:5])

for v,k in tmp[:5] :
    print(k,v)