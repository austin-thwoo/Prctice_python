#int 자료형
print("int 자료형")
print(5)
print(-10)
print(3.14)
print(10000)
print(5+3)
print(2*8)
print(3*(3+1))
print("*"*100)
#String 자료형
print("String 자료형")
print("풍선")
print("ㅋ"*15)
print("이게되네")
print("*"*100)
#boolean 자료형
print("boolean 자료형")
print( 5> 10)
print( 5< 10)
print(True)
print(False)
print("-"*9)
print(not True)
print("*"*100)
#변수
#애완동물을 소개해주세요
print("#애완동물을 소개해주세요")
print("우리집 애기의 이름은 해피이 입니다.")
print("해피의 나이는 5살이고 낮잠을 아주 좋아합니다.")
print("해피는 사람일까요?")
print("*"*100)
print("[애완동물이 바뀐다면?]")
print("*"*100)
animal  = "강아지"
name = "광복이"
age = 12
hobby = "산책"
is_adult = age >= 3
print("우리집"+ animal + "이름은"+ name + "입니다.")
print(name + "나이는 "+str(age)+"살이고 "+hobby+"을 아주 좋아합니다.")#정수형을 출력할때는 문자형으로 감싸주어야 한다
print(name+"은(는) 사람일까요?"+ str(is_adult))
print("*"*100)
print("[+를 , 로 바꿔 쓸 수 있다 이경우 Str()처럼 문자형으로 감싸주지 않아도 된다 단, 자동으로 띄어쓰기 되어지고]")
print("*"*100)
print("우리집",animal,"이름은",name,"입니다.")
print(name,"나이는 ",age,"살이고 ",hobby,"을 아주 좋아합니다.")#정수형을 출력할때는 문자형으로 감싸주어야 한다
print(name,"은(는) 사람일까요?", is_adult)
'''
이렇게 작은 따옴표 세개 안에 묶으면 
한번에 주석처리가
됩니다.
'''
#퀴즈.1
#변수를 이용해서 다음을 출력하시오 
station = "사당" 
print(station,"행열차가 들어오고 있습니다.")

number= (2 + 3)*4
print(number)
number +=2
print(number)
number -=2
print(number)
number *=2
print(number)
number /=2
print(number)
number %=5
print(number)

print(abs(-5))#절댓값
print(pow(4,2))#4의2승
print(max(5,12))#최댓값
print(min(5,12))#최솟값
print(round(3.14))#최솟값
print(round(4.999))#최솟값

from math import * #메쓰라이브러리 소환!!

print (floor(4.99))#내림
print (ceil(3.14))#올림
print(sqrt(16))#제곱근

from random import * #랜덤라이브러리 소환!!

print(random())
print(random()*10)
print(int(random()*10))
print(int(random()*10))
print(int(random()*10)+1)
print(int(random()*10)+1)
print(int(random()*10)+1)
print("-"*100)
print(int(random()*45)+1)#1부터 45이하의 값
print(randrange(1,46))#1부터 45이하의 값
print(randint(1,45))#1부터 45이하의 값

#퀴즈
first=randint(4,28)
second=randint(4,28)
third=randint(4,28)
fourse=randint(4,28)
print("오프라인 스터디 모임 날짜는 매월",first,second,third,fourse,"일로 선정되었습니다" )

sentence= '나는 소년입니다.' 
sentence2= "파이썬은 쉽습니다."
print(sentence)
print(sentence2)
sentence3="""
줄바꿈처리(큰따옴표3개)로 인해 쓴데로 보여지게 됩니다 이 문장은 세줄로 뜨게 됩니다
"""
print(sentence3)
#슬라이싱[]
jumin= "990120-1234567"
print("성별 : ",jumin[7])
if jumin[7] == "1":
    sung="남자"
elif jumin[7] == "2":
    sung="여자"
else:
    sung="불분명"
print("성별 : ", sung)
print("연 : ",jumin[0:2])#0부터 2직전까지(0~2)
print("월 : ",jumin[2:4])#2부터 4직전까지(2~3)
print("일 : ",jumin[4:6])#4부터 6직전까지(4~5)
print("생년월일 : ",jumin[:6])#처음부터 6직전까지
print("뒤 7자리 : ",jumin[7:])#7부터 끝까지
print("뒤 7자리(뒤자리부터): ",jumin[-7:])#맨뒤에서 7부터 끝까지
