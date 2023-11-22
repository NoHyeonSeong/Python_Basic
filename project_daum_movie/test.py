# 문제 1. 중첩 for문을 사용해서 다음과 같은 출력이 나오도록 별찍기 코드를 작성하세요.
# 출력 예시
# *
# **
# ***
# ***
# *****

# for i in range(5):
#     for j in range(i + 1):
#         print("*", end = "")
#     print()

def Fib(n):
    a, b = 1, 1
    fib_list = [a]
    if n == 1:
        return fib_list
    for _ in range(1, n):
        a, b = b, a + b
        fib_list.append(a)
    return fib_list

for i in Fib(6):
    print(i)
