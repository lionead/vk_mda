import vk_mda as vk_api
from vk_mda.keyboard import VkKeyboard
from vk_mda.bot_longpoll import VkBotLongPoll, VkBotEventType
import json


token = ''
group_id = 0


vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

'''
Создаём клавиатуру и добавляем Callback-кнопку
'''
keyboard = VkKeyboard(inline=True)
keyboard.add_callback_button('Нажми меня')


'''
Основной Longpoll для считывания событий
'''
longpoll = VkBotLongPoll(vk_session, abs(group_id))

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.message.text == 'test':
            print(event)
            vk.messages.send(peer_id=event.message.peer_id,
                             message='Test\n\nЕсли не работает, то скорее всего ты не с мобильной версии -- m.vk.com',
                             keyboard=keyboard.get_keyboard(),
                             random_id=0)
    elif event.type == VkBotEventType.MESSAGE_EVENT:
        print('i see')
        print(event.obj)
        test = {
            "type": "show_snackbar",
            "text": "Привет!"
        }
        vk.messages.sendMessageEventAnswer(event_id=event.obj.event_id,
                                           user_id=event.obj.user_id,
                                           peer_id=event.obj.peer_id,
                                           event_data=json.dumps(test))
    else:
        print(event)
        print(event.type)
