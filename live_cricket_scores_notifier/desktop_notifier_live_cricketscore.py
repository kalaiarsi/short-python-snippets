from gi.repository import Notify
import requests
import os
import bs4
from time import sleep
Notify.init("Cricket Score")

for i in range(10):
	res=requests.get("http://www.cricbuzz.com/live-cricket-scores/19169/rsaw-vs-indw-1st-odi-icc-championship-match-india-women-tour-of-south-africa-2018")
	soup=bs4.BeautifulSoup(res.text,"html.parser")
	score=soup.find("span",{"class":"cb-font-20 text-bold"}).text
	notification = Notify.Notification.new( "Score", score, os.getcwd()+"/cricket.jpeg")
	notification.set_app_name("Live Cricket Score")
	notification.show()
	sleep(120)

