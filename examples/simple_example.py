# -*- coding: utf-8 -*-
import vk_mda


def main():
    """ Пример получения последнего сообщения со стены """

    login, password = 'python@vk.com', 'mypassword'
    vk_session = vk_mda.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_mda.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    """ VkApi.method позволяет выполнять запросы к API. В этом примере
        используется метод wall.get (https://vk.com/dev/wall.get) с параметром
        count = 1, т.е. мы получаем один последний пост со стены текущего
        пользователя.
    """
    response = vk.wall.get(count=1)  # Используем метод wall.get

    if response['items']:
        print(response['items'][0])


if __name__ == '__main__':
    main()
