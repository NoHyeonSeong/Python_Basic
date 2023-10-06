# 입력된 단수를 출력하는 코드
# dan = int(input("단수: "))
# for i in range(1, 10):
#    print(f"{dan}x{i}={i*dan}")


# 문제2) 2단부터 9단까지  출력하는 코드
# 2X1=2
# 2x2=4
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i}x{j}={j*i}")

# 문제3) list a의 평균값을 계산하세요.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# total => 총합
total = 0
for i in a:
    #total = total + i
     total += i
length = len(a)
result = total / length
# round(값, 소수점숫자) : 반올림
print(round(result, 2)) # 평균값

# 문제4) list b에서 최소값 찾기!
b = [22, 1, 4, 7, 98]

# num_min = min(b)
num_min = b[0] # 최소값 담을 공간
for x in b:    # 5번 반복
    if x < num_min:
        num_min = x
print(num_min)  # 1 출력

# 문제5) list c의 최소값, 최대값 찾기
c = [2, 5, 7, 1, 8]
num_min = c[0]
num_max = c[0]

for i in c:
    if i < num_min:
        num_min = i
    else:
        num_max = i
print(num_min)  # 1 출력
print(num_max)  # 8 출력

print("="*100)
# 문제6)
# 사용자가 입력한 값 1, 2, 3 통과
# 아닌 경우 다시 입력하도록

# count = 0   # 틀린 횟수
# while True:
#     if count >= 3:
#         print("프로그램을 사용할 수 없습니다.")
#         break
#
#     num = int(input("값: "))
#     # if 4 > num > 0: # num = 1, 2, 3
#     if num in [1, 2, 3]:
#         print(f"{num}을 입력하셨습니다.")
#         break
#     else:
#         print("1, 2, 3의값만 입력해주세요.")
#         count += 1
# 문제7) 1부터 100까지 총합을 출력하는 코드
# - for문으로 작성
# - while문으로 작성

sum = 0
a = range(1, 101)
for i in a:
    sum += i
print(f"총합(for): {sum}")

#
# a = [range(1, 101)]
# for i in a:
#     a = sum(i)
# print(a)

# - while문 작성
num = 0
total = 0

while True:
    num += 1
    if num == 101:
        break
    total += num
print(f"총합(while): {total}")

# sum1 = 0
# i = 1
# while i < 101:
#     sum1 += i
#     i += 1
# print(sum1)


