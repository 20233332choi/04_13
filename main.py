print("--- 구구단 프로그램 버전 2.0 ---")

k=int(input("정수를 입력:"))
for i in range(1, k+1):
    print(f"\n{i}단:")
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")

