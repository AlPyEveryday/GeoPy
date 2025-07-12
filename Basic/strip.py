data = '      hello geo    '
#data length는 공백 포함
print(data)
print(len(data))
#strip으로 양쪽 공백 제거 가능
print(data.strip())
print("문자열 길이는 " + str(len(data.strip())))
#h index 구하기
print(str(data.index("h"))+"\n")
#l index 구하기 -> 첫 번째 하나만
print(data.index("l"))
## 내가 원하는건 모두 출력하기
arr=[]
for i, ch in enumerate(data):
    if ch == 'l':
        arr.append(i)
print(arr)
