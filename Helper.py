import requests 
import os 

class Machine():
	def __init__(self):
		self.Tags = "/api/v4/machine/tags/" # + Bloods 
		self.Profile = "/api/v4/machine/profile/"
		self.Current = "/api/v4/machine/active"

class Challenge():
	def __init__(self):
		self.Retired = "/api/v4/challenge/list/retired"
		self.Active = "/api/v4/challenge/list"
		self.Profile = "/api/v4/challenge/info/"
		self.Download = "/api/v4/challenge/download/"

class User():
	def __init__(self):
		self.ConnectionStatus = "https://www.hackthebox.eu/api/v4/user/connection/status"


class Session():
	def __init__(self):
		self.HTB_API_Key = os.getenv("HTB_Token")
		self.URL = "https://www.hackthebox.eu"
	def Auth(self):
		Headers = {}
		r = requests.get(f"https://www.hackthebox.eu/api/charts/users/scores"){self.HTB_API_Key}")
		print(r.text)



if __name__ == "__main__":
	s = Session()
	s.Auth()