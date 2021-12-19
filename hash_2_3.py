# 전화번호 목록
# 해결책 3번
# 해시 이용하여 접두어가 존재하는지 확인

def solution(phoneBook):
    hash_map = {}

    # Hash map 생성
    for phone_number in phoneBook:
        hash_map[phone_number] = 1

    # 접두어가 Hash map 에 존재하는지 확인
    for phone_number in phoneBook:
        judoo = ""

        # 각 번호의 접두어 추출 ("1", "12", "123")
        for number in phone_number:
            judoo += number

            # Hash map에 접두어 확인 (기존 번호와 같은 경우 제외)
            if judoo in hash_map.keys() and judoo != phone_number:
                return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))