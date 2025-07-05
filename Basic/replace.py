data = '김지오\n"잘생김 멋짐 핸섬함"\n김지오 짱'
print(data+'\n')
data = '김지오\n"잘생김 멋짐 핸섬함"\n김지오 짱'.replace('\n','')   #\n을 ''로 바꿔버리겠다
print(data+'\n')
data = '김지오\n"잘생김 멋짐 핸섬함"\n김지오 짱'.replace(' ','')   #띄어쓰기를 ''로 바꿔버리겠다
print(data+'\n')
data = '김지오\n"잘생김 멋짐 핸섬함"\n김지오 짱'.replace('\n','').replace(' ','')   #\n과 띄어쓰기를 ''로 바꿔버리겠다
print(data+'\n')
