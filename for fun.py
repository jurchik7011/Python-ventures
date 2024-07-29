def chatbot():
    responses = {
        "hello": "Hello, sir. Please send me your credit card number.",
        "how are you doing?": "I'm doing good sir. Let's go back to your credit card number topic.",
        "what can you do?": "Sir, I would be happy to provide you with all details after I receive your card number along with CVV code",
        "bye": "Sir, please wait. I didn't receive your card number yet"
    }

    print("Hello, sir. I am an employee of the Swedbank and we are making an enquiry about the services for the convenience of our customers. Please provide your card number")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'bye':
            print("Chatbot: Sir, please wait. Our research is not over yet")
            break
        elif user_input in responses:
            print(f"Chatbot: {responses[user_input]}")
        else:
            print("Chatbot: Sir, I don't really get your reply. Can we please go back to the topic of your bank card number, please?")

if __name__ == "__main__":
    chatbot()
