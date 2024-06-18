import pyttsx3
import time
import sys
engine = pyttsx3.init()
async def on_event(event):
    global engine

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}

def text_to_morse(text):
    morse_code = ' '.join(MORSE_CODE_DICT.get(char.upper(), char) for char in text)
    return morse_code

def play_morse_code(morse_code):

    for char in morse_code:
        if char == '-':
            word = 'Dah'
        elif char == '.':
            word = 'Dit'
        elif char == '/':
            word = ''
            time.sleep(1.5)
        else:
            continue
        
        engine.say(f'{word}')
        engine.runAndWait()
        time.sleep(0.1)  # Adjust the sleep duration as needed

    engine.stop()

def morse_to_text(morse_code):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    morse_code_list = morse_code.split(' ')
    text = ''.join(reverse_dict.get(code, code) for code in morse_code_list)
    return text

def is_morse_code(text):
    return any(char not in '.- /' for char in text)

while True:
    choice = input(f"{'-'*20}\nText to Morse (ttm), Or Morse to Text (mtt):\n{'-'*20}\n ")
    choice = choice.lower()
    while choice not in ["ttm","mtt","quit","exit"]:
        print("Please input mtt or ttm!")
        choice = input("Text to Morse (ttm), Or Morse to Text (mtt): ")
        engine.say("Text to Morse or Morse to Text?")
        engine.runAndWait()
        choice = choice.lower()
    

    if choice == "ttm":
        engine.say("Text to Morse Code")
        engine.runAndWait
        input_text = input(f"{'-'*20}\nWhat do you want to translate?:\n{'-'*20}\n ")
        morse_result = text_to_morse(input_text)
        print(f"{'-'*20}")
        print(f'"{input_text}" to Morse Code: \n\n{morse_result}')
        play_morse_code(morse_result)
        print(f"{'-'*20}")
        continue

    elif choice in ['quit','exit']:
        print("Great having you!")
        engine.say(f'Goodbye')
        engine.runAndWait()
        sys.exit()
        
    else:
        engine.say("Morse To Text")
        engine.runAndWait
        input_text = input(f"{'-'*20}\nWhat do you want to translate?:\n{'-'*20}\n ")
        morse_result = morse_to_text(input_text)
        while morse_result == '':
            print("Please enter something valid!")
            input_text = input("What do you want to translate?: ")
            morse_result = morse_to_text(input_text)
            print(f"{'-'*20}")

        print(f"'{input_text}' to text:\n\n {morse_result}")
        engine.say(morse_result)
        engine.runAndWait()
            

        print(f"{'-'*20}")
        continue
