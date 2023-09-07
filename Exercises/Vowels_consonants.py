'''
def calculate(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonants_count = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonants_count += 1
    return vowel_count, consonants_count


def main():
    input_string = input("Enter any text:- ")
    vowel_count, consonants_count = calculate(input_string)

    print("Total vowels:- ", vowel_count)
    print("Total consonants:- ", consonants_count)


if __name__ == "__main__":
    main()
'''


def get_bot_response(user_input):
    responses = {
        "hello": "Hello! How can I assist you?",
        "how are you": "I'm just a chatbot, but I'm here to help!",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm sorry, I didn't quite understand that."
    }

    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])


def main():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day")
            break

        bot_response = get_bot_response(user_input)
        print("Chatbot:", bot_response)


if __name__ == "__main__":
    main()
