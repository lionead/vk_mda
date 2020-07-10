vk_api [![PyPI](https://img.shields.io/pypi/v/vk_api.svg)](https://pypi.org/project/vk_api/) ![Python 2.7, 3.4, 3.5, 3.6, 3.7](https://img.shields.io/pypi/pyversions/vk_api.svg) [![Telegram Chat](https://img.shields.io/badge/-Telegram%20Chat-green?logo=telegram&color=27A7E5)](https://t.me/python273_vk_api)
=================================================================================================================================================================================
**vk_api** – Python модуль для создания скриптов для социальной сети Вконтакте (vk.com API wrapper)

* [Документация](https://vk-api.readthedocs.io/en/latest/)
* [Примеры использования](./examples) (python3)
* [Документация по методам API](https://vk.com/dev/methods)
* [Альтернативы vk_api](https://github.com/python273/vk_api/issues/356) (асинхронность; боты)

```python
import vk_api

vk_session = vk_api.VkApi('+71234567890', 'mypassword')
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))
```

Установка
------------
    $ pip install vk_api
