# 완주하지 못한 선수
# 해결책 2번
# 해시 이용

def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    # 참가자의 directory 만들기, [해시 Key] = 해시 value
    # 참가자 해시 Key 들의 합
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    # 참가자 해시 Key 들의 합 - 완주자 해시 Key = 완주 못한 참가자의 Key
    for comp in completion:
        sumHash -= hash(comp)

    # 남은 참가자 해시 key-value 값이 완주하지 못한 선수
    return hashDict[sumHash]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
               ["josipa", "filipa", "marina", "nikola"]))