# 완주하지 못한 선수
# 해결책 3번
# collections.Counter 이용

import collections
def solution(participant, completion):

    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
               ["josipa", "filipa", "marina", "nikola"]))
