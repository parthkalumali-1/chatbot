import openai

# Set your API key securely (replace with your actual API key, but ideally use environment variables)
openai.api_key = "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"

def chat_with_gpt(prompt):
    try:
        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        # Extract and return the assistant's message content
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Print error message for debugging
        print(f"Error: {e}")
        return "An error occurred while processing your request."

if __name__ == "__main__":
    print("Welcome to GPT Chat! Type 'exit' to quit.")
    while True:
        # Take user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break  # Exit the loop if the user types "exit"
        
        # Process the input and get GPT's response
        response = chat_with_gpt(user_input)
        print(f"GPT: {response}")
