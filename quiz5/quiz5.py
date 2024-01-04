# x = 0

# while x < 10 :
#     if x < 10:
#         x = x + 1
#     elif x > 8 :
#         print(x)
# print(x)

sentence = input('input your sentence> ')
char_count = 0
for char in sentence :
    if char == " ":
        continue
    char_count = char_count + 1

print(char_count)