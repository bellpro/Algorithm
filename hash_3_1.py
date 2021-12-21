# 위장
# 해결책 1번
# 해시 이용

def solution(clothes):
    # 옷을 종류별로 구분
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1

    # 입지 않는 경우를 추가하여 모든 조합 계산
    answer = 1
    for type in hash_map.keys():
        answer *= (hash_map[type] + 1)

    # 아무 종류의 옷도 입지 않는 경우 제외
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

