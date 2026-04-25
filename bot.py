import json
import google.genai as genai
from google.genai import types

# Setup and authentication - provide the API key 

API_KEY = "AIzaSyB2UbLZYTuIEM1WWvLdBjPXbbaZyfLPXrk" 
client = genai.Client(api_key=API_KEY)

## Main function that runs the loop 
def run_quiz():

    print("✨ Gemini Quiz Expert (2.5 Flash Mode)")
    
    while True:
        print("\n" + "="*50)
        
        ## Accept user input that is topic or text
        user_topic = input("Topic/Text (or 'exit'): ").strip()
        # Exit condition to stop the program
        if user_topic.lower() == 'exit':
            break
        
        print("Generating questions...")
        try:
            # Send a request to the Gemini model to generate quiz content
            # RTCCO format
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents= (
                f"Task: Create a five 5-question multiple choice quiz on:{user_topic}."
                "Context: The quiz is for a students' self assesment"
                "Constraint: Return only JSON"
                "Output:{'quiz:[{'question':'...','options':['A)..','B) ..'],'correct_answer':'A'}]}"
             )
            )
    quiz_data = json.loads(response.text)  # Convert JSON string to Python dict
    print(json.dumps(quiz_data, indent=2))  # Pretty print the quiz

      # Loop through and print each answer option (A, B, C, D)
    for q in quiz_data["quiz"]:  # Frank
            # Display the current question with a newline for spacing
                print("\n" + q["question"])  # Frank
            # Loop through and print each answer option (A, B, C, D)
                for opt in q["options"]: print(opt)  # Frank
                        # Get user input, remove extra spaces, and convert to uppercase for consistency
                answer = input("Your answer: ").strip().upper()  # Frank
                print("✅ Correct!" if answer == q["correct_answer"] else "❌ Wrong!")
        
