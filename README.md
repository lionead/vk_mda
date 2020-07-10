vk_mda (vk_api mod) ![Python 2.7, 3.4, 3.5, 3.6, 3.7](https://img.shields.io/pypi/pyversions/vk_api.svg) 
=================================================================================================================================================================================
**vk_mda** – **Модификация модуля** [**vk_api**](https://github.com/python273/vk_api) / Python модуль для создания скриптов для социальной сети Вконтакте (vk.com API wrapper)

* [Документация vk_api](https://vk-api.readthedocs.io/en/latest/)
* [Примеры использования](./examples) (python3)
* [Официальная документация по методам API](https://vk.com/dev/methods)

```python
import vk_mda

vk_session = vk_mda.VkApi('+71234567890', 'mypassword')
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))
```

Установка
------------
    $ pip install vk_mda
