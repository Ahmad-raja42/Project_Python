# importing the speechrecognition module
# pip install speechrecognition
import Speech_Recogn as sr

# let's see what is inside sr
# print(dir(sr))

# let's create a recognizer which can recognize my speech
recognizer_engine = sr.recognizer

# let's first attach the microphone with the python script
with sr.Microphone() as mic:

    # let's get the audio
    audio = recognizer_engine.listen(mic)

    # let's convert the text from audio
    output = recognizer_engine.recognize_google(audio)
    print(output)


