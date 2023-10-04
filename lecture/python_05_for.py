# 제어문
#   1. 조건문(if)
#   2. 반복문(for, while)

# 반복문(Loop)
# - 반복적인 작업을 가능하게 해주는 도구
# - list, str, tuple 등 컬렉션 타입의 아이템을 하나씩 순회하면서
#   사용 가능(for)
# - 특정 조건을 만족하는 경우(while)

# 반복횟수 0 => for
# 반복횟수 X => while

# *for문 기본문법
#   for i in [1, 2, 3]:
#     print(i)

# *range() 함수
# - dafault: 시작(0), 증감(+1)
# - range(시작, 끝, 증감)
# - range(3)        => 0, 1, 2
# - range(1, 10)    => 1, 2, 3, 4, 5, 6, 7, 8, 9
# - range(2, 5, 2)  => 2, 4

# range()를 활용해서 1~9까지 출력하는 for문
for i in range (1, 10):
    print(i)

# List를 활용한 for문
temp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for alpha in temp:
    print(alpha)

# *enumerate()
# - 반복횟수(index) 출력하고 싶은 경우!
# - enumerate()
for i, alpha in enumerate(temp):
    print(i + 1, alpha)

print("="*20);

# 구구단 2단 출력
# 2X1=2
# 2x2=4
#...
# 2x9=18

# input() 활용해서 사용자가 입력한 값(2~9) => 해당 단 출력
# dan = int(input("단수: "))
# for i in range(1, 10):
#     print(f"{dan}x{i}={i*dan}")

print("="*20);
# 2단 9단까지 출력 => 중첩for
# 2X1=2
# 2x2=4
#...
# 2x9=18
# 3x1=3
#...
# 9x9=81
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i}x{j}={j*i}")

# dict를 사용한 for문
temp = {"A" : 1,
        "B" : 2,
        "C" : 3,
        "D" : 4}
print("="*20);
# dict => for => Key값 출력
# keys(), values(), items(0
for element in temp.values():
    print(element)

for key, value in temp.items():
    print("*****")
    print(key)      # key
    print(value)    # value

# break, continue
# break: 즉시 반복문을 빠져 나가세요.
# continue: 즉시 다음 반복으로 넘어가세요.

# a를 출력하다가 3을 만나면 멈추세요.
print("="*20);
a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        break
    print(i)

# 홀수만 출력
print("="*20);
for i in range(30):
    if i % 2 == 0:
        continue
    print(i)

