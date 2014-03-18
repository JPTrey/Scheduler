# Scheduler.py by Jon Paul, 2014
# Handles user input and returns all schedules fitting user filters

""" Global Variables """
# schedules = []			# all schedules fit to user criteria
# courses = []			# all courses within a schedule

""" Classes """
# Course object representing a class entry
class Course:
	def __init__(self, name, number, credits, total_hours, meetings, required):
		self.name = name			# Course name
		self.number = number 		# Course reference number
		self.credits = credits		# Number of credit hours
		self.meetings = meetings	# Array of meeting times/days
		self.required = required	# True: Course must be added to a schedule
		self.marked = False			# False: Course has yet to be added to a schedule
	
	def __str__():
		print self.name

	# (elective only) Called when course has been added to any schedule
	def mark():
		self.marked = True

	# Called when criteria for schedules has changed
	def unmark():
		self.marked = False	

class Schedule:
	def __init__(self, classes, target_days, target_credits, target_hours, total_hours):
		self.classes = Classes 					# Classes Associated With This Schedule
		self.target_days = target_days			# Days Limited by User
		self.target_credits = target_credits	# Credits Preferred By User
		self.target_hours = target_hours		# Hours in Class Preferred By User
		self.total_hours = total_hours			# Total Number of Hours Spent in Class

class Meeting:	
	def __init__(self, start_time, end_time, day):
		self.start_time = start_time
		self.end_time = end_time
		self.day = day					# 1 = Monday, ... , 5 = Friday

""" Methods """

# Called when program launches
# returns: a list of classes to be placed into schedules
def getClasses():
	courses = []
	done = false

	while done is False:
		name = raw_input("Course Name: ")
		number = int(raw_input("Course Number: "))
		credits = int(raw_input("Credits: "))
		duration = int(raw_input("80 or 55 mins: "))
		perweek = int(raw_input("Meetings per week: "))
		total_hours = duration * perweek
		meetings = []
		required = raw_input("Required? ('True' or 'False') ")
		newCourse = Course(name, number, credits, total_hours, meetings, required)
		courses.append(newCourse)
		print courses
		done = True
	print courses[i].name

# Called when either courses are first added, or user changes preferences
# returns: a list of schedules fitting the criteria
# TODO: deal with all targets
#		prevent infinite loop condition
def getSchedules(courses, target_days, target_credits, target_hours):
	schedules = []						# schedules fitting the specified criteria
	marked = 0							# courses already within a schedule

	while marked < len(courses):	# while: unique schedules can be constructed
		newSchedule = []
		days = []					
		credits = 0
		hours = 0

		
		# add required courses
		for i in len(courses):
			if courses[i].credits + credits > target_credits:
				break
			else if courses[i].required:				
				newSchedule.append(courses[i])
				credits += courses[i].credits
				marked++
		
		# add unused courses
		for i in len(courses):
			if courses[i].credits + credits > target_credits:
				break
			else if courses[i].marked is False:
				newSchedule.append(courses[i])
				courses[i].marked = True				

		# add remaining courses
		for i in len(courses):
			if courses[i].credits + credits > target_credits:
				break
			# if credits >= target_credits:
			#	break
			else:
				newSchedule.append(courses[i])
		
		schedules.append(newSchedule)				
	return schedules			

def displaySchedules():		


classes = getClasses()
schedules = getSchedules(classes, [1,5], 16, 0)
displaySchedules(schedules)