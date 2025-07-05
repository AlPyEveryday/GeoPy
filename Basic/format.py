city = '서울'
gu = '마포'
temperature = 32
message1="저는 {}특별시 {}구에 살고 있습니다. 기온이 {}도이네요, 미치겠습니다.".format(city,gu,temperature)
print(message1+'\n')

city2 = "울산"
gun = "울주"
temperature2 = 30
message2 = '%s광역시 %s군에 살고 있습니다. 여기도 기온이 %d도네요, 미치겠습니다'%(city2,gun,temperature2)
print(message2+'\n')
message3 = f'{city2}광역시 {gun}군에 살고 있습니다. 여기도 기온이 {temperature2}도네요, 미치겠습니다'
print(message3+'\n')