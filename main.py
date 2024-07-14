import openai
from datetime import datetime

# Set up your OpenAI API key
openai.api_key = 'sk-proj-C5XIJByKavAynrOKo3boT3BlbkFJ7vtrIhTNPHGTMk16m7Y2'  # Replace with your actual API key

def get_gpt3_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching

    # Greeting responses
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I assist you today?"

    # Farewell responses
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"

    # Inquiries about the chatbot
    elif 'who are you' in user_input or 'what are you' in user_input:
        return "I am a simple chatbot created to assist you with basic questions."

    # Inquiries about the weather
    elif 'weather' in user_input:
        return "I cannot provide real-time weather updates at the moment, but you can check a weather website for the latest information."

    # Inquiries about time
    elif 'time' in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    elif 'what is the use of html' in user_input:
        return "HTML is used to structure and present content on the web."

    elif 'what is the meaning of scattering' in user_input:
        return "The meaning of scattering is used to present content on the web."

    elif 'good morning' in user_input:
        return "Good morning!" have a nice day!

    elif 'good afternoon' in user_input:
        return "Good afternoon!"

    # Use GPT-3 for other queries
    else:
        return get_gpt3_response(user_input)

# Main loop to interact with the chatbot
def main():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

