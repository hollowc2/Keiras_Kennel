import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.delegate import pave_event_space, per_chat_id, create_open



TOKEN = "472710980:AAFEarsik8CKbp_SEKQENuX0LvDLjebx04w"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)
        self._count = 0

    def on_chat_message(self, msg):
        self._count += 1
        self.sender.sendMessage(self._count)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command + ' from user: %s' %chat_id

    if command == '/wave':
        bot.sendMessage(chat_id, 'Hi there')
    elif command == '/pic':
        bot.sendMessage(chat_id, 'Click!')
    else:
        bot.sendMessage(chat_id, 'Not a recognized command, please re-enter the command.')

##
# create a bot on a thread that stays alive for 10 seconds
##
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageCounter, timeout=10),
])


MessageLoop(bot, handle).run_as_thread()


print('Listening ...')

while 1:
    time.sleep(10)
