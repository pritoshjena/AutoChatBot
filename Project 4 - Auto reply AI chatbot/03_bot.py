import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
  api_key="sk-proj-WxSl7ehGk2PnwmzCHcDwT3BlbkFJFMj6bYTk9jG1bqZaFTcj",
)

def is_last_message_from_sender(chat_log, sender_name="Pritosh Jena"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(369, 1062)
time.sleep(1)  # Wait for 1 second to ensure the click is registered

while True:

    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(663,179)
    pyautogui.dragTo(1221,1006, duration=1.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(670,202)
    

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)

    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Pritosh who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and respond like Pritosh. Output should be the next chat response (text message only)"},
                {"role": "user", "content": chat_history}])

    response= completion.choices[0].message.content
    pyperclip.copy(response)

    # Step 5: Click at coordinates (1808, 1328)
    pyautogui.click(1042,975)
    time.sleep(1)  # Wait for 1 second to ensure the click is registered

    # Step 6: Paste the text
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

    # Step 7: Press Enter
    pyautogui.press('enter')

