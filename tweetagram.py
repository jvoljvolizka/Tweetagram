import tweepy
import telegram
import atexit

# Authentication Data
consumer_key ="edit_here"
consumer_secret ="edit_here"
access_token ="edit_here"
access_token_secret ="edit_here"

# Telegram Bot Data
bot = telegram.Bot(token = "edit_here")
bot_chat_id = "edit_here"

# Twitter User Data
twitter_id = "edit_here"

class streamListener(tweepy.StreamListener):

    def on_status(self, status):
        print("\n" + status.extended_tweet["full_text"] + "\n")
        bot.send_message(chat_id=bot_chat_id, text=status.extended_tweet["full_text"])

    def on_error(self, status_code):
        if status_code == 420:
            print("[!] Error occurred.")
            bot.send_message(chat_id=bot_chat_id, text="Error occurred.")
            return False

def atExit():
    print("[*] Stopped.")
    bot.send_message(chat_id=bot_chat_id, text="Stopped.")

atexit.register(atExit)

print("[*] Trying to authenticate.")
bot.send_message(chat_id=bot_chat_id, text="Trying to authenticate.")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("[✓] Authenticated successfully.")
    bot.send_message(chat_id=bot_chat_id, text="Authenticated successfully.")
except:
    print("[!] Authentication failed.")
    quit()

print("[*] Starting to listen.")
bot.send_message(chat_id=bot_chat_id, text="Starting to listen.")

streamListener = streamListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
