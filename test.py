import time
import sys
from threading import Timer

pname=input(print("enter your name: "))
words=["start","totoro","vegeta","yagami","get","not","amazing","people","interesting","gross","ended","read","accelerate",
		"speed","excellent","negligible","expected","anything","walk","talk","angel","beautiful","haunted","horror","acting",
		"ignore","appearance","dominating","together","forever","yelled","hot","hustle","lime","ladyfinger","mango","height",
		"body","excess","soft","broken","broad","vulture","gaming","software","lovely","life","actually","emit","express",
		"feeling","famous","catch","capable","silent","helpful","caring","knowledgable","afraid","eligible","entity"]

Timer(60, output).start()

i=0
count=0
while True:
	print(words[i])
	userword=input()
	if userword==words[i]:
		count=count+1
	i=i+1

def output():
	print("typing speed: {} words per minute", .format(count))
	sys.exit()