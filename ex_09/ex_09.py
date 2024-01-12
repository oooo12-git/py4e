fname = input("Enter file: ")
if len(fname) < 1 : fname = "clown.txt" # 기본값으로 clown.txt 사용
hand = open(fname) # 핸들 변수

di = dict()
for lin in hand:
    lin = lin.rstrip() # rstrip = 오른쪽 white space 제거
    # print(lin) - 디버그
    wds = lin.split() # 빈 공간 기준 단어 나눠서 리스트 반환
    # print(wds) - 디버그
    for w in wds:
        # print("**",w,di.get(w,-99)) # 아래 코드들을 대체 하는 한 줄의 코드
        
        # 만약 key가 없다면 oldcount = 0 이다.
        # oldcount = di.get(w,0) 
        # print(w,'old',oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount

        # ** idiom: retrieve/create/update counter **
        di[w] = di.get(w,0) + 1
        # print(w,'new',di[w])

        # print(w)
        # if w in di :
        #     di[w] = di[w]+1
        #     # print("**Existing**")
        # else:
        #     di[w] = 1
            # print('**NEW**')
        # print(w, di[w])

# print(di)

# now we want to find the most common word
largest = -1
theword = None
for k,v in di.items() : # items 메서드는 키와 값 쌍을 반환
    # print(k,v) - 디버그
    if v > largest :
        largest = v
        theword = k # capture/remember the key that was largest

print(theword, largest)