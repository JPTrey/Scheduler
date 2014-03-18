# 'Scheduler.py' by Jon Paul, 2014
# Handles user input and displays all schedules fitting user filters

from operator import attrgetter

""" Global Variables """
default_schedules = []			# all schedules fit to user criteria

""" Classes """
# Course class representing a course entry
class Course:
	def __init__(self, name, number, credits, total_mins, meetings, required):
		self.name = name			# Course name
		self.number = number 		# Course reference number
		self.credits = credits		# Number of credit hours
		self.total_mins = total_mins
		self.meetings = meetings	# Array of meeting times/days
		self.required = required	# True: Course must be added to all schedules
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
	def __init__(self, courses, credits, total_mins, has_monday, has_friday):
		self.courses = courses 					# Courses Associated With This Schedule	
		self.course_count = len(courses)		
		self.credits = credits					# Total credit hours for all classes
		self.total_mins = total_mins			# Total time spent in class each week
		self.has_monday = has_monday			# True: contains at least one Monday course
		self.has_friday = has_friday			#							Friday course

# One (of upto four) meeting times for a course
class Meeting:	
	def __init__(self, day, start_time, end_time):
		self.day = day							# 1 = Monday, ... , 5 = Friday
		self.start_time = start_time
		self.end_time = end_time
		self.duration = self.end_time - self.start_time
		self.hrs_mins = "{hours} hrs, {mins} mins".format(hours=self.duration/60, mins=self.duration%60) 

""" Methods """

# Called when program launches
# returns: a list of courses to be placed into schedules
def getCourses():
	courses = []
	done = False
	j = 0	# place-holder var

	while done is False:
		name = raw_input("Course Name: ")
		number = int(raw_input("Course Number: "))
		credits = int(raw_input("Credits: "))
		perweek = int(raw_input("Meetings per week: "))
		meetings = []
		total_mins = 0						# minutes per week
		for i in range(0,perweek):
			day = raw_input("Meeting #{0} day: ".format(i+1))
			day = getDayInt(day.lower())
			start_time = int(raw_input("Start Time: "))
			end_time = int(raw_input("End Time: "))
			total_mins += end_time - start_time
			meetings.append(Meeting(day, start_time, end_time))
		#total_mins = duration * perweek
		required = raw_input("Required? ('True' or 'False') ")
		newCourse = Course(name, number, credits, total_mins, meetings, required)
		courses.append(newCourse)
		print courses
		
		j += 1
		if (j == 3):
			done = True

	for i in range(len(courses)):
		print "#{i}: {course}".format(i=i, course=courses[i].name)
	
	return courses		

# Called when either courses are first created, or user changes credit preference
# returns: a list of all possible schedules
# TODO: deal with all targets
#		prevent infinite loop condition
def getSchedules(courses, max_credits):
	all_schedules = []					# list of all possible schedules
	marked = 0							# number of courses already within a schedule

	while marked < len(courses):		# while: unique schedules can be constructed
		schedule_courses = []		
		credits = 0
		total_mins = 0
		has_monday = False
		has_friday = False

		# add required courses
		for i in range(len(courses)):
			if courses[i].credits + credits > max_credits:
				continue	
			
			elif courses[i].required:				
				for j in range(len(courses[i].meetings)):
					if courses[i].meetings[j].day == 1:
						has_monday = True
					elif courses[i].meeting[j].day == 5:
						has_friday = True	
				
				schedule_courses.append(courses[i])
				credits += courses[i].credits
				total_mins += courses[i].meetings[j].duration
				marked += 1
		
		# add unused courses
		for i in range(len(courses)):
			if courses[i].credits + credits > max_credits:
				continue
			
			elif courses[i].marked is False:
				for j in range(len(courses[i].meetings)):
					if courses[i].meetings[j].day == 1:
						has_monday = True
					elif courses[i].meeting[j].day == 5:
						has_friday = True	
				
				schedule_courses.append(courses[i])
				courses[i].marked = True				

		# add remaining courses
		for i in range(len(courses)):
			if courses[i].credits + credits > max_credits:
				continue
			
			else:
				for j in range(len(courses[i].meetings)):
					if courses[i].meetings[j].day == 1:
						has_monday = True
					elif courses[i].meeting[j].day == 5:
						has_friday = True	
				schedule_courses.append(courses[i])
		
		all_schedules.append(Schedule(schedule_courses, credits, total_mins, has_monday, has_friday))			
	return all_schedules			

# Called by getCourses()
# returns: day as integer instead of String
def getDayInt(day):
	return {
		'monday':1,
		'tuesday':2,
		'wednesday':3,
		'thursday':4,
		'friday':5
	}[day]

#def displaySchedules():	

# Rebuilds schedule list that satifies user criteria, as set by upto five booleans	
def filterSchedules(schedules, target_credits, no_mondays, no_fridays, min_hours, min_courses):
	global default_schedules
	default_schedules = schedules 	# save for "Default" action
	
	if target_credits > 0:
		schedules = getSchedules(courses, target_credits)	
	if no_mondays:
		for i in range(len(schedules)):
			if schedules[i].has_monday:
				schedules.pop(i)	
	if no_fridays:
		for i in range(len(schedules)):
			if schedules[i].has_friday:
				schedules.pop(i)	
	if min_hours:
		schedules = sorted(schedules, key=attrgetter('total_mins'))	
	if min_courses:
		schedules = sorted(schedules, key=attrgetter('course_count'))		

	if schedules == 0:
		alert("No Schedules Fit Your Preferences")
	else:
		return schedules					


""" Execution """

courses = getCourses()
schedules = getSchedules(courses, 18)		
displaySchedules(schedules)
schedules = filterSchedules(schedules, 0, True, True, False, False)