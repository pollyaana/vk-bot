# vk-bot
Необходимые действия перед тестированием:

При создании токена доступа к сообществу, необоходимы выставить разрешения на доступ к фотографиям, сообщениям сообщества. 

git clone https://github.com/pollyaana/vk-bot.git 

pip install -r requirements.txt

GROUP_TOKEN - токен сообщества вк

GROUP_ID - id сообщества вк

python3 main.py

P.S К сожалению, не получилось сделать отправку сообщения при первом заходе в чат, получается только приветсвенное после первого отправленного сообщения от пользователя, либо через настройки самой группы :( (можно было решить это с помощью сохранения id пользователя в БД, но опять же таки, отправка сообщения получалось только после первого сообщения от пользователя, а не при заходе в чат)
