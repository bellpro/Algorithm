# 완주하지 못한 선수
# 해결책 1번
# 정렬한 뒤, 반복문을 통해 1대1 비교하여 서로 다른 항목이 나온 사람을 반환

def solution(participant, completion):
    answer = ''

    # 정렬
    participant.sort()
    completion.sort()

    # 완주자 길이만큼 참가자를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 완주자 길이만큼 다 돌아도 없는 경우는 마지막 참가자가 완주하지 못한 선수이다
    return participant[len(participant)-1]

    return answer

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
               ["josipa", "filipa", "marina", "nikola"]))
