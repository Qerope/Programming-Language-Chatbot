import openai
import re

# Initialize OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define function to generate response from OpenAI API
def generate_response(input_text):
    # Define prompt for OpenAI API
    prompt = (f"What is {input_text}?")
    
    # Generate response using OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Extract answer from response
    answer = response.choices[0].text.strip()
    
    # Remove unnecessary text
    answer = re.sub(f"What is {input_text}\?", "", answer)
    answer = re.sub(r"\n\n", "\n", answer)
    
    return answer

# Define main function to handle user input
def main():
    while True:
        # Get user input
        user_input = input("What would you like to know about programming languages? ")
        
        # Generate response
        response = generate_response(user_input)
        
        # Print response
        print(response)

# Run main function
if __name__ == "__main__":
    main()
