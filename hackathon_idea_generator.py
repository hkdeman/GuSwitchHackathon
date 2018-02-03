import random


l = ["A whiteboard app that lets you draw on a whiteboard from your smartphone",
	"Uber for horses","A potty training tutorial for iPad (for kiddos)",
	"Salmon-Scraper: a game where you peel scales off of a fish",
	"FatBit—- like fitBit, but it encourages calming down and lounging",
	"Light-dimmer: a light-dimming switch for your smartphone",
	"A social goal-tracking app, similar to YikYak (anonymous support!)",
	"A dating app for ONLY the socially awkward",
	"Gender-bender: an app that lets you push a button to change your gender.",
	"Potato peel: a game that’s literally just peeling potatoes.",
	"Bloody-murder: an app that emulates a fire alarm so you can fake an emergency (this is actually useful in real-life dangerous situations… and for exam-day)",
	"An app for dogs that teaches dogs how to use a smartphone.",
	"An app for farmers that lets them know if it’s a good day to plant/harvest.",
	"An app that organizes bar bets (requires a witness to distribute the winnings)"]

g= l.copy()

while(len(g)!=0):
	g = input("Enter g to generate: ")
	if(g=="g"):
		c = random.choice(l)
		print(c)
		l.remove(c)
	else:
		print("one job, literally")	
print("Man I got no ideas anymore")
