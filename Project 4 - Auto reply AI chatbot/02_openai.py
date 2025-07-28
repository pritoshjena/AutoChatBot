from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="sk-proj-WxSl7ehGk2PnwmzCHcDwT3BlbkFJFMj6bYTk9jG1bqZaFTcj",
)
command='''
[11:52 pm, 25/7/2025] Ayush: Chalo to
[11:52 pm, 25/7/2025] Ayush: Bat le Ana
[11:52 pm, 25/7/2025] Pritosh Jena: Ok
[9:33 pm, 26/7/2025] Ayush: Kal chalo ge park subah
[10:23 pm, 26/7/2025] Pritosh Jena: Kal jaunga
[10:23 pm, 26/7/2025] Pritosh Jena: But badminton khelna padega
[10:23 pm, 26/7/2025] Pritosh Jena: Ball nahi hai vese
[10:23 pm, 26/7/2025] Pritosh Jena: Nahi mili ghar mein
[10:23 pm, 26/7/2025] Ayush: A jaye gi
'''

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Pritosh who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Pritosh"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)