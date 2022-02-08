#Challenge 14
#Write an algorithm that:
#	•Asks the user to input the traffic light colour. 
#	•If the traffic light colour is green, outputs ‘Go.’
#	•If the traffic light colour is amber, outputs ‘Get Ready.’
#	•Otherwise outputs ‘Stop.’

colour = input("Please enter the trafic light colour: ")

if colour == "green":
	print("GO!!!")
elif colour == "amber":
	print("Get Ready")
else:
	print("Stop")