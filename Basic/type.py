#str형
item = "hello"
print("item : " + str(item))
print("hello의 타입은 "+ str(type(item))+"입니다\n")

#int형 (파이썬에는 int형의 크기 제한이 없다)
a=5
print("a : "+ str(a))
print("a의 타입은 "+ str(type(a))+"입니다")

b=10**10
print("b : "+ str(b))
print("b의 타입은 "+ str(type(b))+"입니다")

print('안녕하세요 "김지오"입니다\n저는 \'서강대학교\' 학생입니다')

#float형 (파이썬에는 double,long형이 없다)
c=7.5
print("c : "+ str(c))
print("c의 타입은 " + str(type(c))+"입니다\n")

#메모리를 알려주는 함수, 다만 파이썬에서는 메모리를 참조해서 읽는 것은 불가능
d=5
print("c의 주소는 "+str(id(d)))
d=6
print("c의 주소는 "+str(id(d))+"\n")

#간단한 곱셈
quantity = 10
price = 20000
print("총 가격은 " + str(quantity*price)+"원입니다\n")

