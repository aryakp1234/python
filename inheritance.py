# simple inheritance

class WhatsApp:
    def chat(self):
        print ("this is chat feature")


class WhatsApp_Emoji_Update(WhatsApp):
    def emoji(self):
        print("this is emoji feature")

y=WhatsApp_Emoji_Update()
y.chat()
y.emoji()



# multiple inheritance


class WhatsApp:
    def chat(self):
        print ("this is chat feature")


class WhatsApp_Emoji_Update(WhatsApp):
    def emoji(self):
        print("this is emoji feature")

class WhatsApp_Voice_Update(WhatsApp_Emoji_Update):
    def voice(self):
        print ("this is voice feature")

y=WhatsApp_Voice_Update()
y.chat()
y.emoji()
y.voice()
