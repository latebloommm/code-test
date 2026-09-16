n = int(input("숫자 n을 입력하세요: "))

total = 0

for number in range(1, n + 1):
    total = total + number

print(f"1부터 {n}까지의 합은 {total}입니다.")
