# 전화번호 목록
# 해결책 1번
# 2중 반복문을 통해 서로가 서로의 접두어인지 전부 확인

def solution(phoneBook):
    # 비교할 A 선택
    for i in range(len(phoneBook)):
        # 비교할 B 선택
        for j in range(i+1, len(phoneBook)):
            # 서로가 서로의 접두어인지 확인
            if phoneBook[i].startswith(phoneBook[j]):
                return False
            if phoneBook[j].startswith(phoneBook[i]):
                return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
