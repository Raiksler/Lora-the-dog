import random
import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import dialog_const

def write_msg(chat_id, message, reply_to_id=None):
    vk.method('messages.send', {'chat_id' : chat_id, 'message' : message, 'random_id' : 0})

def write_weather(day):
    if day == 'today':
        weather = int(requests.get('https://api.open-meteo.com/v1/forecast?latitude=60.7&longitude=28.74&hourly=precipitation,weathercode&daily=weathercode&current_weather=true&timezone=Europe%2FMoscow').json()['daily']['weathercode'][0])
        if weather == 0:
            msg = '*Лора растягивает спинку на солнышке. Небо сегодня чистое.*'
            return msg
        if weather == 1:
            msg = '*Лора зовет гулять, сегодня в целом солнечно.*'
            return msg
        if weather == 2:
            msg = '*Лора смотрит на облака. Погода, очевидно, облачная.*'
            return msg
        if weather == 3:
            msg = '*Лора грустно смотрит в окно, сегодня пасмурно.*'
            return msg
        if weather == 45:
            msg = '*Лора держится к тебе поближе, чтобы не потеряться, ведь сегодня туман!*'
            return msg
        if weather == 48:
            msg = '*Лора задумчиво смотрит на заиндевевшую траву, сегодня изморозь.*'
            return msg
        if weather == 51:
            msg = '*Лора предпочла бы остаться дома, на улице легкая морось.*'
            return msg
        if weather == 53:
            msg = '*Лора предпочла бы остаться дома, на улице моросит.*'
            return msg
        if weather == 55:
            msg = '*Лора предпочла бы остаться дома, на улице морось, переходящая в дождь.*'
            return msg
        if weather == 56:
            msg = '*Не лучшее время, чтобы гулять - на улице легкая ледяная морось.*'
            return msg
        if weather == 57:
            msg = '*Не лучшее время, чтобы гулять - на улице ледяная морось.*'
            return msg
        if weather == 61:
            msg = '*На улице легкий дождик, но Лора всеравно хочет гулять.*'
            return msg
        if weather == 63:
            msg = '*Идет дождь, Лора пытается уворачиваться от капель. Выходит плохо.*'
            return msg
        if weather == 65:
            msg = '*Сегодня сильный дождь, переходящий в ливень льет на улице. Лора с нетерпением ждет когда разойдутся тучки, чтобы идти гулять.*'
            return msg
        if weather == 66:
            msg = '*На улице сегодня град, не самое лучшее время для прогулки.*'
            return msg
        if weather == 67:
            msg = '*Скоро будет сильнейший град, выходить на улицу опасно.*'
            return msg
        if weather == 71:
            msg = '*Сегодня будет легкий снегопад, Лора собирается ловить снежинки!*'
            return msg
        if weather == 73:
            msg = '*Сегодня будет идти снег. Лора собирается ломать снеговиков!*'
            return msg
        if weather == 75:
            msg = '*Сегодня ожидается сильный снегопад. Лора снова будет закапываться в снег!*'
            return msg
        if weather == 77:
            msg = '*Ожидаются снежные зерна... Что бы это ни было...*'
            return msg
        if weather == 80:
            msg = '*На улице ливень, не сильный, но Лора всеравно не хочет идти гулять.*'
            return msg
        if weather == 81:
            msg = '*Лора несет тебе зонт. Он пригодится, ведь сегодня ливень!*'
            return msg
        if weather == 82:
            msg = '*Ожидается сильнейший ливень, гроза, гром, шторм или еще какая-нибудь суровая стихия... В такую погоду хороший хозяин собаку на улицу не выгонит!*'
            return msg
        if weather == 85:
            msg = '*Сегодня будет легкий снегопад, Лора собирается ловить снежинки!*'
            return msg
        if weather == 86:
            msg = '*Сегодня ожидается сильный снегопад. Лора снова будет закапываться в снег!*'
            return msg
        if weather == 95:
            msg = '*Ожидается гроза, Лора опять будет прятаться под кроватью.*'
            return msg
        if weather == 96:
            msg = '*Ожидается гроза с градом. Редкое сочетание, в любом случае с Лорой сегодня не погулять.*'
            return msg
        if weather == 99:
            msg = '*Ожидается гроза с градом. Редкое сочетание, в любом случае с Лорой сегодня не погулять.*'
            return msg
        else:
            msg = '*Лора не смогла распознать погоду за окном =(*'
            return msg
    else:
        weather = int(requests.get('https://api.open-meteo.com/v1/forecast?latitude=60.7&longitude=28.74&hourly=precipitation,weathercode&daily=weathercode&current_weather=true&timezone=Europe%2FMoscow').json()['daily']['weathercode'][1])
        if weather == 0:
            msg = '*Лора растягивает спинку в предвкушении солнышка. Небо завтра чистое.*'
            return msg
        if weather == 1:
            msg = '*Лора зовет гулять, завтра в целом солнечно.*'
            return msg
        if weather == 2:
            msg = '*Завтра Лора опять будет смотреть на облака, ожидается облачность.*'
            return msg
        if weather == 3:
            msg = '*Лора грустно смотрит в окно, завтра будет пасмурно.*'
            return msg
        if weather == 45:
            msg = '*Лора водит в воздухе носом... Очевидно завтра ожидается туман.*'
            return msg
        if weather == 48:
            msg = '*Лора задумчиво смотрит на траву, скорее всего, завтра будет изморозь.*'
            return msg
        if weather == 51:
            msg = '*Лора предпочла бы остаться дома, завтра на улице легкая морось.*'
            return msg
        if weather == 53:
            msg = '*Лора предпочла бы остаться дома, завтра на улице моросит.*'
            return msg
        if weather == 55:
            msg = '*Лора предпочла бы остаться дома, завтра на улице морось, переходящая в дождь.*'
            return msg
        if weather == 56:
            msg = '*Не лучшее время, чтобы гулять - завтра на улице легкая ледяная морось.*'
            return msg
        if weather == 57:
            msg = '*Не лучшее время, чтобы гулять - завтра на улице ледяная морось.*'
            return msg
        if weather == 61:
            msg = '*Завтра на улице легкий дождик, но Лора всеравно хочет гулять.*'
            return msg
        if weather == 63:
            msg = '*Будет дождь, Лора снова будет пытаться уворачиваться от капель =)*'
            return msg
        if weather == 65:
            msg = '*Завтра ожидается сильный дождь, переходящий в ливень льет на улице. Лора с нетерпением ждет когда разойдутся тучки, чтобы идти гулять.*'
            return msg
        if weather == 66:
            msg = '*Завтра на улице град, не самое лучшее время для прогулки.*'
            return msg
        if weather == 67:
            msg = '*Ожидается сильнейший град, выходить на улицу опасно.*'
            return msg
        if weather == 71:
            msg = '*Завтра будет легкий снегопад, Лора собирается ловить снежинки!*'
            return msg
        if weather == 73:
            msg = '*Завтра будет идти снег. Лора собирается ломать снеговиков!*'
            return msg
        if weather == 75:
            msg = '*Завтра ожидается сильный снегопад. Лора снова будет закапываться в снег!*'
            return msg
        if weather == 77:
            msg = '*Ожидаются снежные зерна... Что бы это ни было...*'
            return msg
        if weather == 80:
            msg = '*Завтра ожидается ливень, не сильный, но Лора всеравно не хочет идти гулять.*'
            return msg
        if weather == 81:
            msg = '*Лора несет тебе зонт. Он пригодится, ведь завтра ливень!*'
            return msg
        if weather == 82:
            msg = '*Ожидается сильнейший ливень, гроза, гром, шторм или еще какая-нибудь суровая стихия... В такую погоду хороший хозяин собаку на улицу не выгонит!*'
            return msg
        if weather == 85:
            msg = '*Завтра будет легкий снегопад, Лора собирается ловить снежинки!*'
            return msg
        if weather == 86:
            msg = '*Завтра ожидается сильный снегопад. Лора снова будет закапываться в снег!*'
            return msg
        if weather == 95:
            msg = '*Завтра ожидается гроза, Лора опять будет прятаться под кроватью.*'
            return msg
        if weather == 96:
            msg = '*Завтра ожидается гроза с градом. Редкое сочетание, в любом случае с Лорой не погулять.*'
            return msg
        if weather == 99:
            msg = '*Завтра ожидается гроза с градом. Редкое сочетание, в любом случае с Лорой не погулять.*'
            return msg
        else:
            msg = '*Лора не смогла распознать погоду на завтра =(*'
            return msg

token_vk = ''
vk = vk_api.VkApi(token=token_vk)                                                  # Авторизация вк
longpoll = VkBotLongPoll(vk, 215943276)                                            # Класс для работы с лонгполл сервером вк

lora_mood = 30                                                                     # Стартовый параметр настроения собаки, заглушка более сложной системы.

for event in longpoll.listen():                                                    # Основной цикл, прослушивание long poll
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
            elif request in dialog_const.play:
                if lora_mood >= -20:
                    write_msg(message = random.choice(dialog_const.lora_play), chat_id=chat_id)
                    write_msg(message = '*Настроение Лоры немного улучшилось*', chat_id=chat_id)
                    lora_mood += 10
                else: 
                    write_msg(message = '*Лора выгладит грустной и больше не хочет с вами играть =(*', chat_id=chat_id)
            elif request in dialog_const.feed:
                 write_msg(message = '*Лора с удовольствием принимает хрустящее угощение!*', chat_id=chat_id)
                 write_msg(message = '*Настроение Лоры немного улучшилось*', chat_id=chat_id)
                 lora_mood += 10
            elif request in dialog_const.weather['today']:
                if lora_mood > 0:
                    write_msg(message = write_weather('today'), chat_id=chat_id)
                else:
                    write_msg(message = '*Настроение Лоры упало слишком низко, она не хочет отвечать на вопросы.*', chat_id=chat_id)
                    write_msg(message = 'Ты можешь "поиграть с Лорой" или "угостить Лору морковкой", чтобы поднять ее настроение!', chat_id=chat_id)
            elif request in dialog_const.weather['tomorrow']:
                if lora_mood > 0:
                    write_msg(message = write_weather('tomorrow'), chat_id=chat_id)   
                else:
                    write_msg(message = '*Настроение Лоры упало слишком низко, она не хочет отвечать на вопросы.*', chat_id=chat_id)
                    write_msg(message = 'Ты можешь "поиграть с Лорой" или "угостить Лору морковкой", чтобы поднять ее настроение!', chat_id=chat_id)
            elif request in dialog_const.encorage:
                write_msg(message = '*Лора весело виляет хвостом, ей приятна похвала!*', chat_id=chat_id)
                write_msg(message = '*Настроение Лоры немного улучшилось*', chat_id=chat_id)
                lora_mood += 2
            else:
                write_msg(message = '*Ты был укушен за пятку! Лора пока не понимает, что ты от нее хочешь!*', chat_id=chat_id)
                write_msg(message = '*Настроение лоры немного упало*', chat_id=chat_id)
                lora_mood -= 10
