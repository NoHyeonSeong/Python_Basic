# 문자열의 이해(String)
# 1. 문자열 인덱스
# - 문자열은 각 문자마다 순서(인덱스)가 있음
# - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
# - 인덱스 시작은 0
# - 인덱스는 공백 포함
print("="*200)
print("python")

# 2. 문자 추출
# - 인덱스를 통해서 문자 추출
# - 인덱스 범위 벗어난 경우 오류(Error: index out of range)
lang = "Python"
print(lang[0]) # P
print(lang[2]) # t
# print(lang[9])

# -1 인덱스(Reverse Index)
# - 우측에서 좌측으로 인덱스
# - 시작값 -1
print(lang[-1]) # n
print(lang[-3]) # h

# 3. 문자열 슬라이싱
# lang[3]: 문자 1개만 추출
# - 부분 문자열을 추출하고 싶은 경우
# - 시작인덱스, 끝인덱스필요!
msg = "Python is all you need"
print(msg[0:6]) # 끝 인덱스 +1
print(msg[:6]) # 시작 인덱스 생략 -> 자동 0 입력
print(msg[3:]) # 끝 인덱스 생략 -> 자동 -1 입력
print("="*200)

# Quiz
# msg에서 "need"만 추출
# 정방향 인덱스 ->
# 역방향 인덱스 ->
print(msg[-4:])
print(msg[:23])
print(msg[23::-1])
print("="*200)

# 4.문자열 함수
str = "Hello World"

# 4-1.len() : 문자열 길이 계산
print(len(str))

# 4-2.upper() and lower() : 대소문자 변경
# - 데이터 전처리: 1A, 1a => 1A 통일(upper())
print(str.upper())
print(str.lower())

# 4-3.replace() : 문자열 내의 특정 문자 치환
print(str.replace("H", "J"))

# 4-4.split() : 구분자를 기준으로 문자열 분할(Default: 공백)
b = "hello world what a weather"
print(b.split("w"))
print(b.split())

# 4-5.strip() : 문자열의 좌우 공백을 제거
id = "             python1004                  "
print(id)
print(id.strip())

# 4-6.find and rfind() : 문자열 내부의 특정 문자 위치 인덱스 출력
print(str.find("o"))      #Hell[o] world 왼쪽에서 부터 찾음
print(str.rfind("o"))     #hello w[o]rld 오른쪽에서 부터 찾음
print(str.find("world"))  # 없으면 -1출력
print(str.find("World"))  # 첫글자의 인덱스 출력
print(str.rfind("World")) # 첫글자의 인덱스 출력

# 4-7.in() : 특정 문자열 포함하는지 확인(True, False 출력)
print("Hi" in "Hi Python")

# 1. "cherry1004@gmail.com"
#  -> id만 추출 "cherry1004"
#     "job1234@gamail.com"
#     "abc@gamail.com"
id =  "cherry1004@gmail.com"
print(id.find("4"))
val = id[:id.find("@")] # "cherry1004" 출력
print(val)

# 2.

# www.naver.com
# www.daum.net
# www.google.com

# naver, daum, goog만 추출코드
url = "www.naver.com"
start = url.find(".")+1
end =  url.rfind(".")
val = url[start:end]
print(val) #naver