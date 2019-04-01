import random
import vk_api
from config import token


def write_msg(user_id, message):
    random_id = random.randint(1, 1000000)
    vk.method('messages.send', {'user_id': user_id, 'random_id': random_id, 'message': message})


# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)
