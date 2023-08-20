import openai
import speech_recognition as sr
import pyttsx3

class TextAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.listener = sr.Recognizer()
        self.openai_api_key = "Enter your openai key.."
        openai.api_key = self.openai_api_key

    def run(self):
        ops = int(input("What's your choice? Enter 1 for voice and 2 for text: "))
        if ops == 1:
            self.microconnection()
        elif ops == 2:
            self.text()
        else:
            print("Wrong input...")

    def microconnection(self):
        with sr.Microphone() as source:
            print("Speak now...")
            voice = self.listener.listen(source)
            data = self.listener.recognize_google(voice)
            print("You said:", data)
            if "exit" in data:
                exit()
            self.prog(data)

    def text(self):
        data = input("Enter your questions here: ")
        print("Your question is:", data)
        self.prog(data)

    def prog(self, data):
        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=data,
            max_tokens=1024,
            temperature=0.5,
            n=1,
            stop=None
        )
        response = completion.choices[0].text
        print("AI Response:", response)
        self.engine.say(response)
        self.engine.runAndWait()

if __name__ == "__main__":
    assistant = TextAssistant()
    assistant.run()
