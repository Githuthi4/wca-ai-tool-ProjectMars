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

        if user_topic.lower() == 'exit':
            break
        
        print("Generating questions...")
        try:
        
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

        
