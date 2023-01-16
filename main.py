import os
import openai
import json
import customtkinter



def api_response(prompt):
    openai.api_key = "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"
    # openai.api_key = os.environ("OpenAI_Key")


    model_response = str(openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=100,
    temperature=0.9
    ))
    json_obj = json.loads(model_response)
    response = json_obj["choices"][0]["text"]
    return response



# prompt = "def addition(a, 2): what is wrong with this code?"
# a = api_response(prompt)

# print(a)


class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.something = 0
        self.root.title("Open API Chat")
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("500x500") # L x H change back to 270 or 280?
        self.root.config(background="#282828")
        
        
    
    
        self.root.mainloop()
    
    

app = App()