def euler_phi(n):
    result = n  # 초기 값 설정

    # 소인수 분해
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    # 나머지 소인수 처리
    if n > 1:
        result -= result // n

    return result

# 예제: ϕ(10) 계산
result = euler_phi(10)
print(result)  # 출력: 4