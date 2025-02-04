from vk_api.utils import get_random_id
from config import TOKEN, GROUP_ID
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.message['attachments']:
        result = ''
        for attachment in event.message['attachments']:
            images = []
            if attachment["type"] == "photo":
                images.append(attachment['photo'])
                for img in images:
                    result += f"photo{img['owner_id']}_{img['id']}_{img['access_key']},"
        if result:
            vk_session.method("messages.send",
                              {"user_id": event.message['from_id'],
                               "reply_to": event.message['id'],
                               "attachment": result,
                               "random_id": get_random_id()})
