# 문자열 자료형은 할당을 사용할 수 없다. 그러므로 문자열을 바꾸고 싶으면 .replace를 사용하자.

words = 'Connect Foundation'

if 'F' in words:
    n = words.lower()
    nn = n.replace(' ','&')
#    words[7] = '&' # TypeError: 'str' object does not support item assignment
else:
    print(words)
print(nn)