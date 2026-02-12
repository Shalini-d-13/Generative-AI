user= input("you:").lower()
bot="" #response variable 
if user=="hi":
    bot="hello"
elif user=="hello":
    bot="how may i assist you"
elif user=="name:":
    bot="i am simple chatbot"
elif user=="how are you?":
    bot="i am fine, thank you"
elif user=='bye':
    bot="goodbye"
else:
    bot="i am sorry, i don't understand"
print("bot:", bot)