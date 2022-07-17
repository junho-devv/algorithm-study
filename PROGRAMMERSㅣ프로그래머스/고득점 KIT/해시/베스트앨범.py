def solution(genres, plays):
    answer = []

    dict_genre = {e: [] for e in set(genres)}
    for genre, play, idx in zip(genres, plays, range(len(plays))):
        dict_genre[genre].append([play, idx])

    sorted_genre = sorted(list(dict_genre.keys()), key=lambda d: sum(map(lambda g: g[0], dict_genre[d])), reverse=True)

    for genre in sorted_genre:
        list_genre = [e[1] for e in sorted(dict_genre[genre], key=lambda _: (_[0], -_[1]), reverse=True)]
        answer += list_genre[:min(len(list_genre), 2)]

    return answer


if __name__ == "__main__":

    in_g = ["classic", "pop", "classic", "classic", "pop"]
    in_p = [500, 600, 150, 800, 2500]

    print(solution(in_g, in_p))

    in_a = [["a", 2], ["b", 3], ["c", 10]]
    print(sum(map(lambda g: g[1], in_a)))
