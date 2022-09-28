import random
import vk_api
import psycopg2
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import env
from weather import Weather
import dialog_const

class Db_manager:
    def __init__(self):
        self.connection = psycopg2.connect(user='postgres', password='pgadminpass', host='db_server', database='lora_the_dog')   # Измеить db_server на localhost, если приложение разворачивается локально, без использования docker.
        self.cursor = self.connection.cursor()

    def is_chat_in_db(self, id):
        self.cursor.execute('SELECT id FROM chats;')
        return id in [x[0] for x in self.cursor.fetchall()]
    
    def add_chat(self, id):
        self.cursor.execute('INSERT INTO chats (id, mood) VALUES ({chat_id}, 30);'.format(chat_id = id))
        self.connection.commit()
    
    def get_mood(self, id):
        self.cursor.execute('SELECT mood FROM chats WHERE id={};'.format(id))
        return self.cursor.fetchall()[0][0]

    def change_mood(self, id, mood):
        self.cursor.execute("UPDATE chats SET mood={} WHERE id={};".format(mood, id))
        self.connection.commit()

def write_msg(chat_id, message, reply_to_id=None):
    vk.method('messages.send', {'chat_id' : chat_id, 'message' : message, 'random_id' : 0})

if env.vk_token != None:
    token_vk = env.vk_token
    print('В переменных окружения обнаружен заданный токен. Он будет использован для текущего запуска бота. Задать другой токен, можно в файле env.py.')
else:
    print('В файле окружения не задан токен VK. Будет произведен запрос токена через консоль. Задать токен по умолчанию можно в соответствующей переменной файла env.py. Подробности о получении токена в README.')
    token_vk = input('Paste your VK token here: ')

vk = vk_api.VkApi(token=token_vk)                                                  # Авторизация вк
longpoll = VkBotLongPoll(vk, 215943276, wait=25)                                   # Класс для работы с лонгполл сервером вк

print('Бот активен!')

for event in longpoll.listen():                                                    # Основной цикл, прослушивание long poll
    if event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'][1:14] == 'club215943276':
            user_message = event.object.message
            chat_id = event.chat_id
            if not Db_manager().is_chat_in_db(chat_id):                              # Добавляем новый чат в базу данных
                Db_manager().add_chat(chat_id)
            current_mood = Db_manager().get_mood(chat_id)
            if current_mood > 100:
                Db_manager().change_mood(chat_id, 100)
            if current_mood < -50:
                Db_manager().change_mood(chat_id, -50)
            if user_message['text'][29] == ',':                                    # Обработка запятой для обращения в мобильном приложении
                request = user_message['text'][31:].lower()
            else:
                request = user_message['text'][30:].lower()
            if request in dialog_const.greetings:
                write_msg(message = random.choice(dialog_const.lora_greetings), chat_id=chat_id)
            elif request in dialog_const.good_byes:
                write_msg(message = random.choice(dialog_const.lora_good_byes), chat_id=chat_id)
            elif request in dialog_const.how_are_you:
                if current_mood > 0:
                    write_msg(message = random.choice(dialog_const.lora_good_mood), chat_id=chat_id)
                else:
                    write_msg(message = random.choice(dialog_const.lora_bad_mood), chat_id=chat_id)
                    write_msg(message = 'Ты можешь "поиграть с Лорой" или "угостить Лору морковкой", чтобы поднять ее настроение!', chat_id=chat_id)
            elif request in dialog_const.play:
                if current_mood >= -20:
                    write_msg(message = random.choice(dialog_const.lora_play), chat_id=chat_id)
                    write_msg(message = '*Настроение Лоры немного улучшилось*', chat_id=chat_id)
                    Db_manager().change_mood(chat_id, current_mood + 20)
                else: 
                    write_msg(message = '*Лора выгладит грустной и больше не хочет с вами играть =(*', chat_id=chat_id)
            elif request in dialog_const.feed:
                 write_msg(message = '*Лора с удовольствием принимает хрустящее угощение!*', chat_id=chat_id)
                 write_msg(message = '*Настроение Лоры немного улучшилось*', chat_id=chat_id)
                 Db_manager().change_mood(chat_id, current_mood + 10)
            elif request in dialog_const.weather['today']:
                if current_mood > 0:
                    write_msg(message = Weather.get_message('today'), chat_id=chat_id)
                else:
                    write_msg(message = '*Настроение Лоры упало слишком низко, она не хочет отвечать на вопросы.*', chat_id=chat_id)
                    write_msg(message = 'Ты можешь "поиграть с Лорой" или "угостить Лору морковкой", чтобы поднять ее настроение!', chat_id=chat_id)
            elif request in dialog_const.weather['tomorrow']:
                if current_mood > 0:
                    write_msg(message = Weather.get_message('tomorrow'), chat_id=chat_id)   
                else:
                    write_msg(message = '*Настроение Лоры упало слишком низко, она не хочет отвечать на вопросы.*', chat_id=chat_id)
                    write_msg(message = 'Ты можешь "поиграть с Лорой" или "угостить Лору морковкой", чтобы поднять ее настроение!', chat_id=chat_id)
            elif request in dialog_const.encorage:
                write_msg(message = '*Лора весело виляет хвостом, ей приятна похвала!*', chat_id=chat_id)
                write_msg(message = '*Настроение Лоры немного улучшилось*', chat_id=chat_id)
                Db_manager().change_mood(chat_id, current_mood + 2)
            else:
                write_msg(message = '*Ты был укушен за пятку! Лора пока не понимает, что ты от нее хочешь!*', chat_id=chat_id)
                write_msg(message = '*Настроение лоры немного упало*', chat_id=chat_id)
                Db_manager().change_mood(chat_id, current_mood - 10)
