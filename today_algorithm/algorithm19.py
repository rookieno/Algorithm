def solution(genres, plays):
    n = len(genres)
    total_genres_plays = {}
    genre_index_play = {}
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
        print(index_play)
        sorted_index_play = sorted(index_play, key=lambda x: x[1], reverse=True)
        print(sorted_index_play)
        for i in range(len(sorted_index_play)):
            if i > 1:
                break
            result.append(sorted_index_play[i][0])
    return result




genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


print(solution(genres, plays))

# def get_melon_best_album(genre_array, play_array):
#     n = len(genre_array)
#     genre_total_play_dict = {}
#     genre_index_play_array_dick = {}
#     for i in range(n):
#         genre = genre_array[i]
#         play = play_array[i]
#         if genre not in genre_total_play_dict:
#             genre_total_play_dict[genre] = play
#             genre_index_play_array_dick[genre] = [[i, play]]
#         else:
#             genre_total_play_dict[genre] += play
#             genre_index_play_array_dick[genre].append([i, play])

#     sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
#     print(sorted_genre_play_array)
#     result = []
#     for genre, _value in sorted_genre_play_array:
#         index_play_array = genre_index_play_array_dick[genre]
#         sorted_index_play_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
#         for i in range(len(sorted_index_play_array)):
#             if i > 1:
#                 break
#             result.append(sorted_index_play_array[i][0])
#     return result


# print(get_melon_best_album(genres, plays))