from chatterbot import ChatBot
import wikipedia
voice="""
    # Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak
n=1
while n == 1:   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            n=0
 

             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        n=1
         
    except sr.UnknownValueError:
        print("unknown error occurred")
        n=1
"""



















    
import os
import gtts
import pyttsx3
import speech_recognition as sr
#@init(sapi5, debug bool)
from playsound import playsound  
bot = ChatBot('Omnibot')
bot = ChatBot(
    'Omnibot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
bot = ChatBot(
    'Omnibot',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)
from chatterbot.trainers import ListTrainer
def null():
    n=0
    while n < 50:
        n=((n) + 1)
        print('')
trainer = ListTrainer(bot)
voiceon=1

trainer.train([
'How are you today',
'I am doing fine how about you',
'Do you like movies',
'I love movies because they can have good lessons',
'Whats your favorite game',
'Gotta be checkers because it is fun',
'Who made you',
'The one who shall not be named',
'Whats your favorite color',
'I like pink because it is soft',
'Whats your favorite meme',
'I really like the "Thats the battle pass" meme',
'Ok',
'Oki dookie',
'Hi',
'Hello',
'Hello',
'Hi',
'Do you like music',
'I love ajr',
'Do you do drugs',
'Why are you asking a robot this?',
'Whats your favorite food',
'Gotta be cookies',
'Whats your favorite show',
'I like Murder Drones',
'Who are you',
'The one who shall not be named',
'Who is god',
'Luke and kevin',
'What is the meaning of life',
'Capitalism',
'Guess what',
'What',
'Chicken butt',
'I have a very specific set of skill that allow me to be a nightmare to people like you',
'What are your pronouns',
'Shut/The/Fuck/Up/You/Tictok/5yearold',
'Whats your gender',
'Nacho buisness'

    ])
null()
name=input("Enter Your Name: ")
if name == ('wipe'):
    bot.storage.drop()
while True:
    if voiceon == 1:
        print('Speak')
        exec(voice)
        request=(MyText)
        print(name,':',MyText)

        print('Speaking done')
    else:
        request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Pumkin:',response)
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()
