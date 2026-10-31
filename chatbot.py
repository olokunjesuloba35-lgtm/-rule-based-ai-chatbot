
print("================================")
print("WELCOME TO MY AI CHATBOT")
print("================================")

name = input("What is your name? ")

print("Nice to meet you", name)
print("You can start chatting with me!")
print("Type 'bye' to end the conversation.")

while True:

    message = input("You: ").lower().strip()

    if message == "hello" or message == "hi":
        print("Bot: Hello", name, "!")

    elif message == "good morning":
        print("Bot: Good morning", name, "!")

    elif message == "how are you":
        print("Bot: I am doing great!")

    elif message == "what is your name":
        print("Bot: I am your AI chatbot!")

    elif message == "what can you do":
        print("Bot: I can answer simple questions!")

    elif message == "what color is the sky":
        print("Bot: The sky often appears blue during a clear day!")

    elif message == "bye" or message == "exit":
        print("Bot: Goodbye", name, "!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
