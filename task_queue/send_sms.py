import requests
import copy
class EmailNotification:
	def send_email(self):
		services = Services.list_of_services
		copy_services = copy.deepcopy(services)
		service_len = len(services)
		if copy_services[0]:
			url = "mail_gun/"
			data = {"sender": "abc@gmail.com", "recipient": "xyz@gmail.com", "subject": "Sending email",
			"body": "Eamil body"}
			response = requests.post(url, data=data)




class Services:
	def __init__(self):
		self.list_of_services = []
		with open(file_name) as f:
			for f1 in f:
				data = f1.split(",")
				list_of_services.append((data[0], data[1]))
