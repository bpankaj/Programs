class Cars:
	def __init__(self):
		self.name = []
		self.reg_no = []
		self.color = []

	def process_data_for_cars(self, file_name):
		with open(file_name) as f:
			#import pdb;pdb.set_trace()
			for f1 in f:
				split_data = f1.split(',')
				self.name.append(str(split_data[0]))
				self.reg_no.append(str(split_data[1]))
				self.color.append(str(split_data[2]))



class Floors:
	def __init__(self):
		self.no_of_spaces = []
		self.floor_no = []
		self.allocated_cars = []

	def process_data_for_floors(self, file_name):
		with open(file_name) as f:
			for f1 in f:
				split_data = f1.split(",")
				self.no_of_spaces.append(int(split_data[0]))
				self.floor_no.append(int(split_data[1]))

class Allocation(Cars, Floors):
	def __init__(self):
		self.allocated_spaces = []
		self.allocated_floors = []


	def car_allocation(self):
		import pdb;pdb.set_trace()
		pass



