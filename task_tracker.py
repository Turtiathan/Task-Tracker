import time
import kivy

class TaskTracker():
	def __init__(self, location_info):
		self.location_info = location_info
		self.list_of_tasks = {}

	def check_time(self):
		"""
		Returns the time at the user's location.
		"""
		print("The time now is " + str(time.localtime()) + ".")

	def timer(self, minutes):
		"""
		Runs the timmer.
		Input is in minutes but this functions runs them in seconds.
		"""
		seconds = minutes * 60
		time.sleep(int(seconds))
		print("Your time is up.")

	def add_task(self, task, task_time_length):
		"""
		Adds a new task for the Task Tracker.
		The user inputs a name for the task and how long the timer will be for this task.
		"""
		self.list_of_tasks[task] = task_time_length
		print("You have added a new task. It is: " + str(task))
		print("Timer for Task: " + str(task_time_length) + " minutes")

	def remove_task(self, task):
		pass

	def run_task(self, task):
		"""
		This is to run one of the tasks that has been inputted into the program.
		"""
		if task in self.list_of_tasks:
			print("You have picked the task named '" + task + ".' It lasts for " + str(self.list_of_tasks[task]) + " minutes.")
			print("Task started.")
			self.timer(self.list_of_tasks[task])
		else:
			print("Unfortunately, this task does not exist.")
			input("Please press enter to continue.")


	def set_video_to_play(self):
		pass

print("Happy New Year! Welcome to 2020!")
print("This is a program to help you track your tasks with a timer.")
print("It can also play video and audio files depending on the time of day that you specify.")
print("Remember! Procrastination KILLS dreams!")
input("Press enter to run the Task Tracker 2020 program.")

update_location = input("Your current location is: ")
location_info = input("Please enter your timezone or your city to continue. Note: If you misspell, the program will not run!")

taskTracker = TaskTracker(location_info)

input("We will add a task for you. Press enter to continue.")
taskTracker.add_task("Drink a glass of water.", 240)
print("It's a good idea to stay hydraded throughout the day. :)")
start_loop = input("Anyway, press enter to continue.")

while(True):
	taskTracker.check_time()

	print("What would you like to do next?")
	print("A: Pick A Task")
	print("B: Add A Task")
	print("C: Remove A Task")
	print("D: Quit")
	choice = input("Make your choice by entering the letter.").upper()

	if choice == 'D':
		print("Bye-bye! See you next time.")
		break
	elif choice == 'A':
		task = input("Please enter the task you want timed.")
		taskTracker.run_task(task)
	elif choice == 'B':
		print("You have chosen to add a new task.")
		task_name = input("Please enter the name of the task you want to add.")
		task_time_length = input("Please enter the number of minutes for your task. Please use decimal numbers if time is less than one minute (ex: 0.5min for 30sec).")
		try:
			float(task_time_length)
		except ValueError:
			print("This is not a number. Task Tracker 2020 cannot accept a new task without a valid time limit.")
			input("Please press enter to continue.")

		taskTracker.add_task(task_name, float(task_time_length))
	elif choice == 'C':
		pass
	else:
		input("You did not enter a valid choice. Please press enter to continue.")
