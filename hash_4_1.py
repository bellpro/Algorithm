def solution(genres, plays):
    answer = []
    genres_dic = {}
    g_p_list = []
    # 딕셔너리에 넣고
    for i in range(len(genres)):
        if genres[i] not in genres_dic:
            genres_dic[genres[i]] = plays[i]
        else:
            genres_dic[genres[i]] += plays[i]
        # 장르와 재생횟수를 한개의 리스트로 만들어줌
        g_p_list.append([genres[i], plays[i], i])

    # 튜플형태로 총 재생횟수를 기준 내림차순 정렬
    genres_dic = sorted(genres_dic.items(), key=lambda item: -item[1])
    # 장르별 정렬, 인덱스는 큰순으로 정렬
    g_p_list = sorted(g_p_list, key=lambda x: (x[0], -x[1], x[2]))

    for g in genres_dic:
        cnt = 0
        for i in range(len(g_p_list)):
            if cnt == 2:
                break
            if g[0] == g_p_list[i][0]:
                answer.append(g_p_list[i][2])
                cnt += 1

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))