print(float(8))
print(int(3.92))
print(3.14**2)      #제곱
print(3.14//2)      #몫
print(3.14/2)       #정확한 나누기
print(3.14%2)       #3.14로 나눈 나머지

a,b,c = map(int,input("3개의 값을 입력하세요 : ").split(' '))   #3개의 값을 받는 방법
sum=a+b+c
print("3개의 합은 "+ str(sum)+"입니다")
