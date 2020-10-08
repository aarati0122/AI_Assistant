import speech_recognition as sr

import webbrowser

import pyaudio

import pyttsx3 as s

import os

import subprocess as sp

s.speak("Welcome to AI Assistant Application")
print("******Welcome to AI Assistant Application*******")

r = sr.Recognizer()

while True:
	with sr.Microphone() as source:
		start = "start saying..."
		s.speak(start)
		print(start)
		audio = r.listen(source,timeout=2,phrase_time_limit=2)
		set=r.recognize_google(audio) 
		print("you said:{}".format(set))
		text="Ok got it......Wait"  
		s.speak(text)
		print(text)

	ch1 = r.recognize_google(audio)
	if ("hello" in ch1) or ("hii" in ch1) or ("hey" in ch1):
		a1="Hello"
		s.speak(a1)
		print("Bot said:" + a1)
	elif ("who" in ch1) and ("are" in ch1) and ("you" in ch1):
		txt="Yes  I  am  your  AI Assistant jack"
		s.speak(txt)
		print("Bot said:" + txt)
	elif ("how" in ch1) and ("are" in ch1):
		a2="I am good"
		s.speak(a2)
		print("Bot said:" + a2)
	elif  ("run" in ch1)or ("Run" in ch1) or ("application" in ch1):
		break
	else:
		print("Sorry could not Recognize try again")
	
	
txt1="Hey  user which Application you want to Run"
s.speak(txt1)
print(txt1)

while True:	
	with sr.Microphone() as source:
		
		p="start saying..."
		s.speak(p)
		print(p)
		audio = r.listen(source,timeout=4,phrase_time_limit=4) 
		text="Ok got it......Wait" 
		print(text) 
		s.speak(text)
	
	ch = r.recognize_google(audio)

	if (("open" in ch) or ("excute" in ch)) and (("docker" in ch) or ("instance" in ch)):
		webbrowser.open("http://192.168.43.86/oslaunch.html")

	elif (("open" in ch) or ("excute" in ch) or ("run" in ch)) and ("command" in ch):
		webbrowser.open("http://192.168.43.86/program.html")

	elif ("check" in ch) or ("os" in ch) and ("active" in ch):
		webbrowser.open("http://192.168.43.86/cgi-bin/docker_image_names.py")

	elif ("open" in ch)and (("search" in ch) or ("os" in ch)):
		webbrowser.open("http://192.168.43.86/search.html")

	elif ("gmail" in ch) or ("website" in ch):
		webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
	
	elif ("aws" in ch) or ("cloud" in ch):
		webbrowser.open("https://aws.amazon.com/free/?trk=ps_a134p000003yhlXAAQ&trkCampaign=acq_paid_search_brand&sc_channel=ps&sc_campaign=acquisition_IN&sc_publisher=google&sc_category=core-main&sc_country=IN&sc_geo=APAC&sc_outcome=Acquisition&sc_detail=aws&sc_content=Brand_Core_aws_e&sc_matchtype=e&sc_segment=453325184782&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Core-Main|Core|IN|EN|Text&s_kwcid=AL!4422!3!453325184782!e!!g!!aws&ef_id=CjwKCAjw2dD7BRASEiwAWCtCb1pIWX5XaTKLGCDFzlHlMvF98FnyRN8Ujpvb8OXhCNPuaowMdvLgixoCjLQQAvD_BwE:G:s&s_kwcid=AL!4422!3!453325184782!e!!g!!aws&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc")
 
	elif (("open" in ch) or ("run" in ch)) and ("firefox" in ch):
		sp.getstatusoutput("start firefox")
	
	elif (("open" in ch) or ("run" in ch)) and ("notepad" in ch):
		sp.getstatusoutput("start notepad")

	elif (("stop" in ch) or ("terminate" in ch) or ("close" in ch)) and (("application" in ch) or ("program" in ch)):
			te="bye have a nice day"
			s.speak(te)
			print(te)
			break
	else:
		error=("Sorry could not Recognize try again")
		s.speak(error)
		print(error)



