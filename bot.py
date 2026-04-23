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
            # 2. THE API CALL 
            #1.5-flash is the 'safe' choice for free users
            responce = client.models.generate_content(
                model="gemine-2.5-flash",
                f"Task:create a five 5-question multiple choice quiz on:{user_topics}",
               " context: The quiz is for a students' self assesment"
                "constrains return only JSON"
                "output:{'quiz:[{'question':'...','options':['A)..','B) ..'],'correct_answer':'A'}]}"
             )
            )

        
