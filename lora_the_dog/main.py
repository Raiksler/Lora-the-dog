import random
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import dialog_const

def write_msg(chat_id, message, reply_to_id=None):
    vk.method('messages.send', {'chat_id' : chat_id, 'message' : message, 'random_id' : 0})

token_vk = ''
token_weather = '31b18f73dd86405b59278cafaf38654b'

vk = vk_api.VkApi(token=token_vk)                                                  # Авторизация вк
longpoll = VkBotLongPoll(vk, 215943276)                                            # Класс для работы с лонгполл сервером вк

lora_mood = 30                                                                     # Стартовый параметр настроения собаки, заглушка более сложной системы.

for event in longpoll.listen():                                                    # Основной цикл, прослушивание long poll
    print(event)
    if event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'][1:14] == 'club215943276':
            user_message = event.object.message
            if user_message['text'][29] == ',':
                request = user_message['text'][31:].lower()
            else:
                request = user_message['text'][30:].lower()
            chat_id = event.chat_id
            print(request)
            if request in dialog_const.greetings:
                write_msg(message = random.choice(dialog_const.lora_greetings), chat_id=chat_id)
            elif request in dialog_const.good_byes:
                write_msg(message = random.choice(dialog_const.lora_good_byes), chat_id=chat_id)
            elif request in dialog_const.how_are_you:
                if lora_mood > 0:
                    write_msg(message = random.choice(dialog_const.lora_good_mood), chat_id=chat_id)
                else:
                    write_msg(message = random.choice(dialog_const.lora_bad_mood), chat_id=chat_id)
                    write_msg(message = 'Ты можешь "поиграть с Лорой" или "угостить Лору морковкой", чтобы поднять ее настроение!', chat_id=chat_id)
            elif request == 'поиграть с лорой':
                if lora_mood >= -20:
                    write_msg(message = random.choice(dialog_const.lora_play), chat_id=chat_id)
                    write_msg(message = '*Настроение Лоры немного улучшилось*', chat_id=chat_id)
                    lora_mood += 10
                else: 
                    write_msg(message = '*Лора выгладит грустной и больше не хочет с вами играть =(*', chat_id=chat_id)
            elif request == 'угостить лору морковкой':
                 write_msg(message = '*Лора с удовольствием принимает хрустящее угощение!*', chat_id=chat_id)
                 write_msg(message = '*Настроение Лоры немного улучшилось*', chat_id=chat_id)
                 lora_mood += 10
            else:
                write_msg(message = '*Ты был укушен за пятку! Лора пока не понимает, что ты от нее хочешь!*', chat_id=chat_id)
                write_msg(message = '*Настроение лоры немного упало*', chat_id=chat_id)
                lora_mood -= 10
