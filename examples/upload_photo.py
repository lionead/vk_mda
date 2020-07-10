# -*- coding: utf-8 -*-
import vk_mda


def main():
    """ Пример загрузки фото """

    login, password = 'python@vk.com', 'mypassword'
    vk_session = vk_mda.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_mda.AuthError as error_msg:
        print(error_msg)
        return

    """ В VkUpload реализованы методы загрузки файлов в ВК
    """

    upload = vk_mda.VkUpload(vk_session)

    photo = upload.photo(  # Подставьте свои данные
        '/root/3301.jpg',
        album_id=200851098,
        group_id=74030368
    )

    vk_photo_url = 'https://vk.com/photo{}_{}'.format(
        photo[0]['owner_id'], photo[0]['id']
    )

    print(photo, '\nLink: ', vk_photo_url)


if __name__ == '__main__':
    main()
