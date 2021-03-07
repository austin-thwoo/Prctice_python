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