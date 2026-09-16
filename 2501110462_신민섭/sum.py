n = int(input("자연수 n을 입력하세요: "))

if n < 1:
    print("1 이상의 자연수를 입력하세요.")
else:
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"1부터 {n}까지의 합: {total}")
