
import pyttsx3
import webbrowser
import requests, json 
import wikipedia
import re
import webbrowser as sr
import speech_recognition as sr
import googletrans
from googletrans import Translator
from datetime import date, datetime 
from random import randint 
from time import sleep
from youtube_search import YoutubeSearch


api_key = "c325cb3d103d37e68dd38bb439625f50"


ow_url = "http://api.openweathermap.org/data/2.5/weather?"

list_weather = ["Ha Noi" , "London" , "New York", "Paris" ,"Los Angeles","Bangkok","Tokyo","Seoul","Sydney","Ho Chi Minh City" ]

r=sr.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:


	with sr.Microphone() as source:
	    r.adjust_for_ambient_noise(source,duration=1)
	    # r.energy_threshold()
	    print("say anything : ")
	    audio= r.listen(source)
	    try:
	        you = r.recognize_google(audio)
	    except:
	    	you = ""



	if "Ha Noi" in you:
		n = 0
	if "London" in you:
		n = 1
	if "New York" in you:
		n = 2
	if "Paris" in you:
		n = 3
	if "Los Angeles" in you:
		n = 4
	if "Bangkok" in you:
		n = 5
	if "Tokyo" in you:
		n = 6
	if "Seoul" in you:
		n = 7
	if "Sydney" in you:
		n = 8
	if "Ho Chi Minh City" in you:
		n = 9

	print("You say : " + you)

	if you == "":	
		robot_brain = "i can't hear you, try again"

	elif "translate" in you:
		t = Translator()
		a = t.translate(you, src="en", dest = "vi")
		print (a.text)
		robot_brain = you + " is mean " + a.text + "in Vietnamese"

	elif "hello" in you:
		robot_brain = "Hello Nam"
	elif "love" in you:
		robot_brain = "It must be your lovely wife, who i love most, Nguyen Huong Giang "
	elif "goodnight" in you:
		robot_brain = "Goodnight"
	elif "how are" in you:
		robot_brain = "Strong as the battery of the computer"
	elif "joke" in you:
		robot_brain = "Why the broken pencil can not write"  
		robot_brain_1 = "It is pointless"

	elif "YouTube" in you:
		url = "https://www.youtube.com/?gl=VN"
		webbrowser.open_new(url)
	elif "Facebook" in you:
		url_1 = "https://www.facebook.com/huonggiang.nguyen.18092001"
		webbrowser.open_new(url_1)

	elif "music" in you:
			result = YoutubeSearch(you, max_results=1).to_dict()
			result = YoutubeSearch(you, max_results=1).to_dict()
			url = "https://www.youtube.com" + result[0]['url_suffix']
			webbrowser.open(url)
			robot_brain = "Here is your song"

	elif "your" in you :
		you = randint(1,3)
		if you == 1:
			robot_brain = " I am an assistant , Tavis"
		if you == 2:
			robot_brain = " My name is Tavis "
		if you == 3:
			robot_brain = " Tavis and your's assistant "

	elif "name" in you:
		robot_brain = "NGO HA NAM"


	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")

	elif "you" in you :
		you = randint(1,3)
		if you == 1:
			robot_brain = " I am an assistant , Tavis"
		if you == 2:
			robot_brain = " My name is Tavis "
		if you == 3:
			robot_brain = " Tavis and your's assistant "

	elif "tell me " in you :
		contents = wikipedia.summary(you).split('\n')
		robot_brain = "Here is your impormation" + " " + contents[0]
		sleep(3)

	elif "searching " in you:
		reg_ex = re.search('mở (.+)', you)
		if reg_ex:
			domain = reg_ex.group(1)
			url = 'https://www.' + domain
			webbrowser.open(url)

	elif "what" or "tall" or "height" or "age" or "old" or "when" in you:
		url =f"https://www.google.com/search?q={you}"
		webbrowser.open_new(url)
		robot_brain = "here is your search"


	elif "bye" in you :
		robot_brain = "Bye Master Nam"
		print ("Robot say :" + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break

	elif list_weather[n] in you:
		city = list_weather[n]
		call_url = ow_url + "appid=" + api_key + "&q=" + city 


		response = requests.get(call_url) 


		data = response.json() 

		if data["cod"] != "404": 
			
			city_res = data["main"] 

			current_temperature = city_res["temp"] 

			current_pressure = city_res["pressure"]  

			current_humidiy = city_res["humidity"] 

			wthr = data["weather"] 

			weather_description = wthr[0]["description"] 


			robot_brain = ("the Temperature  is " + str(current_temperature - 273.15) + "celsius" +
				"\n atmospheric pressure is " + str(current_pressure) + "hPa" +
				"\n humidity is " + str(current_humidiy) + "% " + 
				"\n and In generally, we can say the weather is " + str(weather_description)) 




	print ("Robot say :" + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
	if "joke" in you:
		print ("Robot say :" + robot_brain +" - "+ robot_brain_1)
		robot_mouth.say(robot_brain_1);sleep(3)
		robot_mouth.runAndWait()

	







