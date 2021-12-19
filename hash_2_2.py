# 전화번호 목록
# 해결책 2번
# 정렬 후, 1중 반복문을 통해 앞 번호가 뒷 번호의 접두어인지 확인

def solution(phoneBook):
    # 정렬
    phoneBook.sort()

    # 전화번호부 2개씩 확인해서 접두어인지 확인
    for i in range(len(phoneBook) - 1):
        if phoneBook[i+1].startswith(phoneBook[i]):
            return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
