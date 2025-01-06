from helper import load_json_file
import json
from llm_responses import ClaudeConversationChain
import re

Botqns_json = 'Bot_qntions.json'
Give_json = 'Give.json'
Get_json = 'Get.json'
Prompts_json = 'Prompts.json'

# git config --global user.name "SomaSquidgy34"
# git config --global user.email "sa@squidgy.ai"
# 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
# git clone https://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@github.com/Squidgy-AI/BoilerPlateV1.git



def process(Botqns,Give,Get,Prompts):
    # Extract the main question structure and prompt details
    Conv_chain = ClaudeConversationChain(api_key=None) 
    question_set = Botqns['questions']
    prompts = Prompts['Prompts']
    
    # Iterate over each section and question
    for section_name, questions in question_set.items():
        print(f"\nStarting section: {section_name}\n")
        
        for question_key, question_text in questions.items():
            # Display question and prompt for user input
            print(f"\nBOT: {question_text}\n")

        system_inp = "Use this prompt template -" + json.dumps(prompts[section_name])
        user_inp = input("Human - Enter your response: ")
        print("\n")

        min_score = prompts[section_name]['Score_threshold']
        max_attempts = prompts[section_name]['Attempts']

        attempt = 0
        while attempt < max_attempts:
            response = Conv_chain.get_response(system_prompt = system_inp, user_prompt = user_inp)
            score_removed_response = re.sub(r"\n?score:.*", "", response)
            match = re.search(r"score:(\d+)", response)
            if match:
                score_value = match.group(1)
                print("Score value:", score_value)
                if int(score_value) >= int(min_score):
                    print("Min Score value Satisfied")
                    print(f"\nBOT: {score_removed_response}\n")
                    print("\n")
                    break
                else:
                    print("\n Min Score value NOT Satisfied \n")
                    print(f"\nBOT: {score_removed_response}\n")
                    print("\n")
                    system_inp = "Use this prompt template -" + json.dumps(prompts[section_name])
                    user_inp = input("Human - Enter your response: ")
                    attempt+=1
                    continue
            else:
                print("No score value found.")
                print(response)
                break
        
        if attempt == max_attempts-1:
            print(f"\nBOT: {prompts[section_name]["Responses"]["unsatisfies_threshold"]["If over three attempts"][0]}\n")

        if False:
            print("\nFull Conversation History:\n")
            for msg in Conv_chain.get_conversation_history():
                print(f"\n{msg['role'].upper()}: {msg['content']}")
    

if __name__ == "__main__":
    Botqns = load_json_file(Botqns_json)
    #print("Botqns :",Botqns)
    Give = load_json_file(Give_json)
    #print("Give :",Give)
    Get = load_json_file(Get_json)
    #print("Get :",Get)
    Prompts = load_json_file(Prompts_json)
    #print("Prompts :",Prompts)
    process(Botqns,Give,Get,Prompts)