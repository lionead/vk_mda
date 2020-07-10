# -*- coding: utf-8 -*-
import collections

import vk_mda
from vk_mda.audio import VkAudio


def main():
    """ Пример составления топа исполнителей для профиля вк """

    login, password = 'login', 'password'
    vk_session = vk_mda.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_mda.AuthError as error_msg:
        print(error_msg)
        return

    vkaudio = VkAudio(vk_session)

    artists = collections.Counter(
        track['artist'] for track in vkaudio.get_iter()
    )

    # Составляем рейтинг первых 15
    print('Top 15:')
    for artist, tracks in artists.most_common(15):
        print('{} - {} tracks'.format(artist, tracks))

    # Ищем треки самого популярного
    most_common_artist = artists.most_common(1)[0][0]

    print('\nSearching for {}:'.format(most_common_artist))

    tracks = vkaudio.search(q=most_common_artist, count=10)

    for n, track in enumerate(tracks, 1):
        print('{}. {} {}'.format(n, track['title'], track['url']))


if __name__ == '__main__':
    main()
