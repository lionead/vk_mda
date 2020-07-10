vk_mda (vk_api mod) ![Python 2.7, 3.4+](https://img.shields.io/pypi/pyversions/vk_api.svg) 
=================================================================================================================================================================================
**vk_mda** – **Модификация модуля** [**vk_api**](https://github.com/python273/vk_api) / Python модуль для создания скриптов для социальной сети Вконтакте (vk.com API wrapper)

* [Примеры использования](./examples) (python3)
* [Официальная документация по методам API](https://vk.com/dev/methods)

```python
import vk_mda.vk_api as vk_api

vk_session = vk_api.VkApi('+71112223344', 'mypassword')
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))
```

Установка
------------
    $ git clone https://github.com/lionead/vk_mda.git
