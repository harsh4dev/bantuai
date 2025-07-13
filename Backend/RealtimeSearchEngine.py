from googlesearch import search
from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values


env_vars = dotenv_values(".env")


Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")


client = Groq(api_key=GroqAPIKey)


System = f"""Hello, I am {Username}. You are a highly accurate and advanced AI chatbot named {Assistantname}, with real-time access to up-to-date information from the internet.

*** Provide answers in a professional and well-structured manner, ensuring proper grammar, punctuation, and clarity. Only include the most relevant and important information. ***

*** Do not mention search results, sources, or external references in your response. Simply provide a clear and direct answer based on the available data. ***"""



try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
except:
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)


def GoogleSearch(query):
    results = list(search(query, advanced=True, num_results=3))
    Answer = f"The search results for '{query}' are:\n[start]\n"

    for i in results:
        Answer += f"Title: {i.title}\nDescription: {i.description}\n\n"

    Answer += "[end]"
    return Answer


def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer


SystemChatBot = [
    {"role": "system", "content": System},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello, how can I help you ?"}
]


def Information():
    data = ""
    current_data_time = datetime.datetime.now()
    day = current_data_time.strftime("%A")
    date = current_data_time.strftime("%d")
    month = current_data_time.strftime("%B")
    year = current_data_time.strftime("%Y")
    hour = current_data_time.strftime("%H")
    minute = current_data_time.strftime("%M")
    second = current_data_time.strftime("%S")
    data += f"Use This Real-time Information if needed:\n"
    data += f"Day: {day}\n"
    data += f"Date: {date}\n"
    data += f"Month: {month}\n"
    data += f"Year: {year}\n"
    data += f"Time: {hour} hours, {minute} minutes, {second} seconds.\n"
    return data


def RealtimeSearchEngine(prompt):
    global SystemChatBot, messages


    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
    messages.append({"role": "user", "content": f"{prompt}"})


    SystemChatBot.append({"role": "system", "content": GoogleSearch(prompt)})


    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=SystemChatBot + [{"role": "system", "content": Information()}] + messages,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None
    )

    Answer = ""


    for chunk in completion:
        if chunk.choices[0].delta.content:
            Answer += chunk.choices[0].delta.content
        

    Answer = Answer.strip().replace("</s>", "")
    messages.append({"role": "assistant", "content": Answer})


    with open(r"Data\ChatLog.json", "w") as f:
        dump(messages, f, indent=4)


        SystemChatBot.pop()
        return AnswerModifier(Answer=Answer)
    

if __name__ == "__main__":
    while True:
        prompt = input("Enter Your Query: ")
        print(RealtimeSearchEngine(prompt))
