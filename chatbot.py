
def chatbot():
    print("Chatbot: Hello! Welcome to my chatbot.")
    print("Chatbot: Type 'bye' to end the conversation.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi! How can I help you?")

        elif user_input in ["how are you", "how are u"]:
            print("Chatbot: I'm fine, thanks! How about you?")

        elif user_input == "what is your name":
            print("Chatbot: I'm NEXUS!")

        elif user_input == "who created you":
            print("Chatbot: I was created using Python!")

        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()
