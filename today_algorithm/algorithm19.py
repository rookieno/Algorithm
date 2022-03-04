def solution(genres, plays):
    n = len(genres)
    total_genres_plays = {} # 장르 별로 가장 많은 플레이 수
    genre_index_play = {} # 장르 곡의 고유번호
    for i in range(n):
        genre = genres[i]
        play = plays[i]
        if genre not in total_genres_plays:
            total_genres_plays[genre] = play
            genre_index_play[genre] = [[i, play]]
        else:
            total_genres_plays[genre] += play
            genre_index_play[genre].append([i, play])

    sorted_total_genres_plays = sorted(total_genres_plays.items(), key= lambda x:x[1], reverse=True) 
    result = []
    for genre, value in sorted_total_genres_plays:
        index_play = genre_index_play[genre]
        sorted_index_play = sorted(index_play, key=lambda x: x[1], reverse=True)
        for i in range(len(sorted_index_play)):
            if i > 1: # 2곡씩
                break
            result.append(sorted_index_play[i][0])
    return result


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


print(solution(genres, plays))