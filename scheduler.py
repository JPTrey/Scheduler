# Scheduler.py by Jon Paul, 2014
# Handles user input and returns all schedules fitting user filters

"""
scheduler.py
	1. Prompt user to fill out a class form
		a. Class name and/or number
		b. Total credits
		c. Meeting days/times
		d. Required?
	2. Repeat until user specifies "Done"
	3. i = j = 0
	4. Construct a new Schedule object
		a. Add to Schedules[i,j]
		b. j++
	5. Add all required courses in credit order
		a. Report time conflicts, if present; halt
	6. Add unused electives at random
		a. subject to target/maximum credits and days
		b. Mark electives as used
	7. Add used elective courses random
		a. subject to target/maximum credits and days
	8. If courses remain
		a. i++, j  = 0
		b. repeat step 3
	9. Else if all courses are used
		a. j = 0
		b. display schedule[i,j]
	10. If user augments days or target credits textarea
		a. Place all current schedules into Schedules[i]
		b. Hide Schedules[i]
		c. i++
	11. If user presses "Left" button
		a. j--
	12. If user presses "Right" button
		a. j++
	13. If user accepts schedule
		a. print out course numbers and names; halt

	• Step 1 could be reduced to 1a and 1d.
		
	

Version(s):
	1. Intakes a set of classes and returns all possible schedules
		a. Required classes
	2. Filters, including preferred free days and target credts
	3. Lookup and add classes
		a. Suggest classes based on target credits
	4. Build a schedule file compatible with the Skidmore registrar
"""


""" Variables """
i = 0					# schedule slot
schedules = []			# all schedules fit to user criteria
courses = []			# all courses within a schedule
finished = False 		# True: user has selected "Done"


""" Classes """
# Course object representing a class entry
class course:
	def __init__(self, name, credits, total_hours, number, meetings, required):
		self.name = name			# Course name
		self.credits = credits		# Number of credit hours
		self.number = Number 		# Course reference number
		self.meetings = meetings	# Array of meeting times/days
		self.required = required	# True: Course must be added to a schedule
		self.marked = False			# False: Course has yet to be added to a schedule
	
	# Called when course has been added to any schedule
	def mark():
		self.marked = True

	# Called when criteria for schedules has changed
	def unmark():
		self.marked = False	

class schedule:
	def __init__(self, classes, target_days, target_credits, target_hours, total_hours):
		self.classes = Classes 					# Classes Associated With This Schedule
		self.target_days = target_days			# Days Limited by User
		self.target_credits = target_credits	# Credits Preferred By User
		self.target_hours = target_hours		# Hours in Class Preferred By User
		self.total_hours = total_hours			# Total Number of Hours Spent in Class

class meeting:	
	def __init__(self, start_time, end_time, day):
		self.start_time = start_time
		self.end_time = end_time
		self.day = day					# 1 = Monday, ... , 5 = Friday



