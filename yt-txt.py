import speech_recognition as sr
import urllib.request
import re

# get the video id from the link
def get_video_id(link):
    pattern = r"(?<=v=)[\w-]+|(?<=be/)[\w-]+"
    video_id = re.search(pattern, link)
    return video_id.group(0)

# download the audio from the video
def download_audio(link):
    video_id = get_video_id(link)
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = urllib.request.urlopen(url)
    html = response.read()
    audio_url = re.findall(r'(?<="url":"https:).*m4a',str(html))[0].replace("\\u0026","&")
    urllib.request.urlretrieve(audio_url, f"{video_id}.m4a")
    return f"{video_id}.m4a"

# transcribe the audio using Google's speech recognition API
def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# example usage
link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
audio_file = download_audio(link)
text = transcribe_audio(audio_file)
print(text)
