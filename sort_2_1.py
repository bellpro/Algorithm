# 가장 큰 수
# 해결책 1번
# 정렬

def solution(numbers):
    # list(map(함수, 리스트)) : map 은 리스트의 요소를 지정된 함수로 처리해주는 함수
    # int 형 리스트를 문자열 리스트로 처리
    numbers = list(map(str, numbers))

    # key 조건에 맞게 정렬
    # x*3: 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교
    # 666, 101010, 222의 첫번째 인덱스 값으로 비교하여 내림차순 정렬 (6 > 2 > 1)
    numbers.sort(key=lambda x: x*3, reverse=True)

    # join 을 통해 문자열 합침
    # 000 처리를 위해 int 변환 후 str 변환
    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))