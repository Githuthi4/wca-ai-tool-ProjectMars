import json
from groq import Groq 

# Setup and authentication (API key) 
API_KEY = "" 
client = Groq(api_key=API_KEY)

## Main function that runs the loop 
def run_quiz():

    print("Mars Quiz Expert")
    
    while True:
        
        ## Accept user input that is topic or text
        user_topic = input("Enter Topic/Text (or Exit):").strip()

         # Check if the user wants to close the application
        if user_topic.lower() == 'exit':
            break

        print("Generating questions...")

        try:
            # Send a request to the model to generate quiz content
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": (
                        "Role: You are an Examiner."
                        f"Task: Create a 5-question multiple choice quiz on: {user_topic}. "
                        "Context: The quiz is s for a students' self-assessment"
                        "Constraint: Each question must have 4 options(A-D), Only one corret answer, Keep question clear and concise, Return ONLY raw JSON"
                        "Output: {'quiz': [{'question': '...', 'options': ['A) ..', 'B) ..'], 'correct_answer': 'A'}]}"
                    )}
                ],
                response_format={"type": "json_object"}
            )
            
            # PARSE JSON
            raw_text = response.choices[0].message.content.strip()
            data = json.loads(raw_text)
            
            # LOOP through the quiz 
            score = 0
            # enumerate(..., 1) is what gives us the Q1, Q2, Q3...
            for i, q in enumerate(data['quiz'], 1):
                print(f"\nQ{i}: {q['question']}")
                for opt in q['options']:
                    print(f"  {opt}")
                
                ans = input("Your Answer (A/B/C/D): ").strip().upper()
                if ans == q['correct_answer']:
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ No, it was {q['correct_answer']}")

            ## summary of the score
            print(f"\n FINAL SCORE: {score}/5")

        except Exception as e:
            print(f"Error: {e}")
            print("Try waiting 60 seconds before your next request.")

if __name__ == "__main__":
    run_quiz()
