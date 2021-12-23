def solution(genres, plays):
    answer = []
    genres_dic = {}
    g_p_list = []
    # 장르 딕셔너너리
    for i in range(len(genres)):
        # 장르 존재 안하면, 재생횟수 저장
        if genres[i] not in genres_dic:
            genres_dic[genres[i]] = plays[i]
        # 장르 존재하면, 재생횟수 더함
        else:
            genres_dic[genres[i]] += plays[i]
        # 장르, 재생횟수, 고유번호를 한개의 리스트로 만들어줌
        g_p_list.append([genres[i], plays[i], i])

    # 장르-재생횟수 에서 총 재생횟수를 기준 내림차순 정렬
    genres_dic = sorted(genres_dic.items(), key=lambda item: -item[1])
    # 장르 오름차순, 재생횟수 내림차순, 고유번호 오름차순 정렬
    g_p_list = sorted(g_p_list, key=lambda x: (x[0], -x[1], x[2]))

    # 내림차순으로 정렬된 장르 반복
    # pop = 3100, classic = 1450
    for g in genres_dic:
        cnt = 0
        for i in range(len(g_p_list)):
            # 같은 장르 2개이면, 다른 장르
            if cnt == 2:
                break
            # 장르가 같으면, 고유번호 추가
            if g[0] == g_p_list[i][0]:
                answer.append(g_p_list[i][2])
                cnt += 1

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))