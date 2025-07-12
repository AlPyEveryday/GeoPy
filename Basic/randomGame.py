import random

a = random.randint(1,100)

for i in range (1,11):
    ans = int(input(str(i)+"번째 기회 입니다. 값을 입력하세요: "))
    if ans < a:
        print(str(ans)+"보다 큽니다.\n")
    elif ans > a:
        print(str(ans)+"보다 작습니다.\n")
    else:
        print("드디어 정답!\n")
        exit(0)
print("그걸 못맞추냐;")
