print("Chatbot: Hello! I am your chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Chatbot: I am doing great! How about you?")

    elif "name" in user:
        print("Chatbot: I am a simple Python chatbot.")

    elif "thank" in user:
        print("Chatbot: You're welcome!")

    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day!")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")
