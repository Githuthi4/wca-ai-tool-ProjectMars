import json
import google.genai as genai
from google.genai import types

API_KEY = "AIzaSyBKuhAKK_PkKoZs1rhqVB3k0sL3w5hzc8o" 
client = genai.Client(api_key=API_KEY)

def run_quiz():
    print("✨ Gemini Quiz Expert")
    
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
                model="gemini-2.0-flash",
                contents=(
                    f"Task: Create a five 5-question multiple choice quiz on:{user_topic}."
                    "Context: The quiz is for a students' self assesment"
                    "Constraint: Return only JSON"
                    "Output:{'quiz:[{'question':'...','options':['A)..','B) ..'],'correct_answer':'A'}]}"
                )
            )
            # PARSE JSON
            raw_text = response.text.strip()
            if "```json" in raw_text:
                 raw_text = raw_text.split("```json")[1].split("```")[0].strip()
            quiz_data = json.loads(raw_text)

            # Loop through and print each answer option (A, B, C, D)
            for q in quiz_data["quiz"]:  
                # Display the current question with a newline for spacing
                print("\n" + q["question"])  
                # Loop through and print each answer option (A, B, C, D)
                for opt in q["options"]: 
                    print(opt) 
                # Get user input, remove extra spaces, and convert to uppercase for consistency
                answer = input("Your answer: ").strip().upper()  
                if answer == q["correct_answer"]:
                    print("✅ Correct!")
                else:
                    print(f"❌ Wrong! The correct answer was: {q['correct_answer']}")

        except Exception as e:
            # The 'Safety Net' that prevents crashes
            print(f"⚠️ Something went wrong: {e}")
            print("Please try again or check your internet connection.")

# Start the application
if __name__ == "__main__":
    run_quiz()