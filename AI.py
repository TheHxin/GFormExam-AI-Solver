import openai
import json

def AiPromptGenerator(answerType):
    if(answerType == 0):
        ...
    elif(answerType == 1):
        ...
    elif(answerType == 2):
        ...
    elif(answerType == 3):
        ...

def Get_AI_Answer(answerType,answer,question):
    response = openai.ChatCompletion.create( 
        model = Model_Name,
        messages = [
            {"role": "system", "content": System_Role},
            {"role": "user", "content": AiPromptGenerator(answerType,answer,question)}
        ]   
    )

    return response['choices'][0]['message']['content']

def API_Initialize():
    with json.load(open("API.json","r")) as data:
        API_Key = data["API_Key"]
        Model_Name = data["Model_Name"]
        System_Role = data["System_Role"]

        openai.api_key = API_Key
        return Model_Name , System_Role

Model_Name , System_Role = API_Initialize()