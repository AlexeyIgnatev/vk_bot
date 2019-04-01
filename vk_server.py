from vk_api.longpoll import VkLongPoll, VkEventType
import api

# Работа с сообщениями
longPoll = VkLongPoll(api.vk)

# Основной цикл
for event in longPoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            # Сообщение от пользователя
            text = event.text

            api.write_msg(event.user_id, 'Прочитал ваше сообщение + {}'.format(text))
