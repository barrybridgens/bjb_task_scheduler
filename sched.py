# bjb_task_scheduler
# (c) 2014 Barry Bridgens

# Fixed input file for now
input_file_name = 'input.txt'

class Task:
	def __init__(self, description, duration):
		self.description = description
		self.duration = duration

	def parse_duration(self, dur):
		pass

	def dump(self):
		print(self.description, self.duration)

class Tasks:
	pass

class Resource:
	def __init__(self, name):
		self.name = name

class Resources:
	pass

class Scheduler:
	def __init__(self):
		self.READ_TASKS = 1
		self.READ_RESOURCES = 2
		self.tasks = [] # replace with Tasks class
		self.resources = [] # relace with Resources class

	def read_input_file(self, fn):
		mode = self.READ_TASKS
		with open(fn, "r") as f:
			for line in f:
				if line.strip() == '---':
					mode = self.READ_RESOURCES
				else:
					if mode == self.READ_TASKS:
						task_data = line.split('|')
						task = Task(task_data[0].strip(), task_data[1].strip())
						self.tasks.append(task)
						task.dump()
					else:
						print(line.strip())
				


if __name__ == "__main__":
	sched = Scheduler()
	sched.read_input_file(input_file_name)
