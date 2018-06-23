from bot import Bot2_neo
import subprocess


# あらかじめ call_jtalk.sh に実行権限を与えておく
def jtalk(t):
    subprocess.call(["echo call_jtalk.sh " + t], shell=True)


if __name__ == '__main__':
    bot = Bot2_neo("vocabulary_DB.txt")
    t = bot.utter()
    jtalk(t)
