# -*- coding: utf-8 -*-
import vk_mda


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def main():
    """ Пример обработки двухфакторной аутентификации """

    login, password = 'python@vk.com', 'mypassword'
    vk_session = vk_mda.VkApi(
        login, password,
        # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler
    )

    try:
        vk_session.auth()
    except vk_mda.AuthError as error_msg:
        print(error_msg)
        return

    # ...


if __name__ == '__main__':
    main()
