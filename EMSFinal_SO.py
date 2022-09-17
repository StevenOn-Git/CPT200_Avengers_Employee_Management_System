'''
Description:
Employee Management System developed for CPT200 course. Ashford university

Version:
Original Script - Steven On - 20190625

References Used:
	1. python By Programiz. (2019). Python Objects and Class. Retreived from https://www.programiz.com/python-programming/class
	2. Python Central. (2019). How to Get a Sub-string From a String in Python - Slicing Strings. Retreived from https://www.pythoncentral.io/how-to-get-a-substring-from-a-string-in-python-slicing-strings/
	3. patorjk.com (2019). Text to ASCII Art Generator. Retreived from http://www.patorjk.com/software/taag/#p=display&f=Doom&t=EMS%20Project
	4. Mark Rushakoff [Screen Name]. (2019, Oct. 11). How to capitalize the first letter of each word in a string (Python)?. StackOverflow. Retrieved From https://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string-python
	5. Rajendra Dharmkar [Screen Name]. (2017, Dec. 8). How to check if a Python string contains only digits? tutorialspoint. Retrieved From https://www.tutorialspoint.com/How-to-check-if-a-Python-string-contains-only-digits
	6. tutorialspoint. (Date Accessed: 2019, Jun. 6). Python - Exceptions Handling. Retrieved from http://www.tutorialspoint.com/python/python_exceptions.htm
	7. user25312 [Screen Name]. (2010, Dec. 27). Check if a number is int or float. StackOverFlow. Retrieved from https://stackoverflow.com/questions/4541155/check-if-a-number-is-int-or-float
	8. Varun [Screen Name]. (2018, Feb. 17). Python : How to Check if an item exists in list ? | Search by Value or Condition. thispointer.com. Retrieved from https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/  
	9. mykyong [Screen Name]. (2016, Jan. 21). Python – How to split a String. Mkyong.com. Retrieved from https://www.mkyong.com/python/python-how-to-split-a-string/
'''
################ Functions ########################
import os

################ Functions ########################
def titleScreen():
	print(' ________  ___ _____  ______          _           _   ')
	print('|  ___|  \\/  |/  ___| | ___ \\        (_)         | |  ')
	print('| |__ | .  . |\\ `--.  | |_/ / __ ___  _  ___  ___| |_ ')
	print('|  __|| |\\/| | `--. \\ |  __/ \'__/ _ \\| |/ _ \\/ __| __|')
	print('| |___| |  | |/\\__/ / | |  | | | (_) | |  __/ (__| |_ ')
	print('\\____/\\_|  |_/\\____/  \\_|  |_|  \\___/| |\\___|\\___|\\__|')
	print('                                    _/ |              ')
	print('                                   |__/               ')

#Function for user to enter a float type.
def enterSalary(salary):
	while isinstance(salary,float) == False:
		try:
			if(isinstance(salary,str) == True):
				salary = float(salary)
			break
		except:
			print('Salary must be a float!')
			salary = float(input('Enter Employee Salary (####.##): '))
			continue
	return salary

def createNewEmp():
	class Employee:
		Name = input('Enter Employee Name: ').title()
		SSN = input('Enter Employee SSN (#########): ')

		#add while loop to make sure SSN is 9 numbers or if SSN only contains numbers
		while(len(SSN) !=9 or SSN.isdigit() == False):
			print('SSN must be 9 numbers!')
			SSN = input('Enter Employee SSN: ')
		Phone = input('Enter Employee Phone Number(##########): ')

		#add while loop to make sure Phone is 10 numbers or if SSN only contains numbers
		while(len(Phone) !=10 or Phone.isdigit() == False):
			print('Phone number must be 10 numbers!')
			Phone = input('Enter Employee Phone Number(##########): ')
		Email = input('Enter Employee Email Address: ')
		Salary = enterSalary(input('Enter Employee Salary (####.##): '))

	#add employee to dictionary
	empDict[Employee.SSN] = Employee

def updateEmpSSN(name,ssn,phone,email,salary):
	class Employee:
		Name = name
		SSN = ssn
		Phone = phone
		Email = email
		Salary = salary

	#add employee to dictionary
	empDict[Employee.SSN] = Employee

def displayEmp(Name,SSN,Phone,Email,Salary):
	x = '' #Create blank variable to return nothing
	print('\n----------------------------',Name,'-----------------------------')
	print('SSN: ' + SSN[:3] + '-' + SSN[3:5] + '-' + SSN[5:9])
	print('Phone: (' + Phone[:3] + ') ' + Phone[3:6] + '-' + Phone[6:10])
	print('Email:', Email)
	print('Salary: $' + format(float(Salary),'.2f'))
	print('-----------------------------------------------------------------------\n')
	return x #return nothing so you don't get that extra "none" at the end of the code	

def getFilePath(fileName):
	fileTypeFinder = fileName.find('.')
	#The file type will always be txt!
	if fileTypeFinder <1:
		fileName = fileName + '.txt'
	else:
		fileName = fileName[0:int(fileTypeFinder)] + '.txt'
	#create file located in same path of this script!
	filePath = os.path.join(folderPath,fileName)
	return filePath

################ Variables ########################
#employee's list will also be the counter
empList = []
empSelectionList = []
empDict = {}
#All files will be stored in this script's directory. Find the folder and script path
scriptpath = os.path.realpath(__file__)
folderPath = os.path.split(scriptpath)[0]

################ Main Process #####################
#Main Selection Screen
while True:
	try:
		#Welcome the User with a title screen
		titleScreen()			
		print('\nThere are (%d) employees in the system.' % len(empDict.keys()))
		print('----- Main Selection Screen -----')
		print('1: Add Employee')
		print('2: View all Employees')
		print('3: Search employee by SSN')
		print('4: Edit employee information')
		print('5: Export employees’ information to text file')
		print('6: Import employees’ information from text file\n')

		userSelection = int(input('Select an option: '))
		#If user selected 0 or number > 6 throw error
		if userSelection >6 or userSelection == 0:
			raise Exception('')
		#If user selected 1 Go to add employee
		elif userSelection == 1:
			while True:
				try:
					print('\n##### Enter New Employee Information #####')
					#call function to create new employee and add to dictionary
					createNewEmp()
					break
				except Exception as e:
					print('\nERROR:',str(e) + '\nTry Again!')
					continue
		#If user selected 2 Go to view all employees					
		elif userSelection == 2:
			if len(empDict.keys()) <1:
				print('\nThere are no employees to view!')
			else:
				print('\n##### View Employee Details #####')
				while True:
					try:
						#create temp dictionary list finder
						for key in empDict.keys():
							empList.append(key)
						#loop through employee selections for user
						for i in range(len(empList)):
							print("Enter %d to display %s's information" % (int(i)+1,empDict[empList[i]].Name))
							#add all available selections to empSelectionList
							empSelectionList.append(int(i)+1)
						#ask user to make a selection
						empSelection = int(input('Enter a number to view employee information or enter 0 to exit: '))	
						if empSelection == 0:
							#empty empList
							empList = []							
							#user will exit display employee screen
							break
						elif empSelection in empSelectionList:
							#Split employee information capture by comma
							empData = empList[int(empSelection)-1]
							#pass employee user selection to displayEmp function
							displayEmp(empDict[empData].Name,empDict[empData].SSN,empDict[empData].Phone,empDict[empData].Email,empDict[empData].Salary)
							#empty empSelctionlist
							empSelectionList = []
							#empty empList
							empList = []
							continue
						else:
							#empty empList
							empList = []
							raise Exception('')
					except Exception as e:
						print('\nERROR: You must enter an employee number!')
						continue
		#If user selected 3 Go to employee search
		elif userSelection == 3:
			while True:
				try:
					if len(empDict.keys()) <1:
						print('\nThere are no employees to search!')
						break
					else:
						print('\n##### Employee Search #####')
						#Use the employee dictionary (empDict) to search for an employee
						testSSN = input("Enter An Employee's SSN or 0 to return to menu: ")
						if testSSN == '0':
							break
						else:
							displayEmp(empDict[testSSN].Name,empDict[testSSN].SSN,empDict[testSSN].Phone,empDict[testSSN].Email,empDict[testSSN].Salary)
				except Exception as e:
					print('ERROR: SSN',str(e),'Not Found!')
		#If user selected 4 Go to employee edit
		elif userSelection == 4:
			while True:
				try:
					if len(empDict.keys()) <1:
						print('\nThere are no employees to edit!')
						break
					else:
						print('\n##### Employee Edit #####')
						#Use the employee dictionary (empDict) to search for an employee
						testSSN = input("Enter An Employee's SSN or 0 to return to menu: ")
						if testSSN == '0':
							break
						else:
							while True:
								try:
									#display employee info first
									displayEmp(empDict[testSSN].Name,empDict[testSSN].SSN,empDict[testSSN].Phone,empDict[testSSN].Email,empDict[testSSN].Salary)
									#ask user what would they like to edit
									print('----- Edit Selection -----\n0: Exit\n1: Name\n2: SSN\n3: Phone\n4: Email\n5: Salary')
									editVar = int(input("Enter selection to edit %s's information: " % empDict[testSSN].Name))
									if editVar == 0:
										break
									elif editVar == 1:
										while True:
											try:
												#edit employee's Name
												empDict[testSSN].Name = input("Enter Employee's New Name: ").title()
												break
											except Exception as e:
												print('ERROR:',str(e))
									elif editVar == 2:
										#edit User's SSN
										while True:
											try:
												#edit employee's SSN
												SSN = input("Enter Employee's new SSN (#########): ")

												#add while loop to make sure SSN is 9 numbers or if SSN only contains numbers
												while(len(SSN) !=9 or SSN.isdigit() == False):
													print('SSN must be 9 numbers!')
													SSN = input("Enter Employee's new SSN (#########): ")

												#add new dictionary item												
												updateEmpSSN(empDict[testSSN].Name,SSN,empDict[testSSN].Phone,empDict[testSSN].Email,empDict[testSSN].Salary)

												#delete old SSN
												oldSSN = empDict[testSSN].SSN
												empDict.pop(oldSSN)

												#change ssn edit to new SSN employee
												testSSN = SSN
												break
											except Exception as e:
												print('ERROR:',str(e))										
									elif editVar == 3:
										while True:
											try:
												#edit employee's Phone Number
												empDict[testSSN].Phone = input('Enter Employee Phone Number(##########): ')

												#add while loop to make sure Phone is 10 numbers or if SSN only contains numbers
												while(len(empDict[testSSN].Phone) !=10 or empDict[testSSN].Phone.isdigit() == False):
													print('Phone number must be 10 numbers!')
													empDict[testSSN].Phone = input('Enter Employee Phone Number(##########): ')
												break
											except Exception as e:
												print('ERROR:',str(e))										
									elif editVar == 4:
										while True:
											try:
												#edit employee's Email
												empDict[testSSN].Email = input("Enter Employee's New Email: ")
												break
											except Exception as e:
												print('ERROR:',str(e))
									elif editVar == 5:
										while True:
											try:
												#edit employee's Salary
												empDict[testSSN].Salary = enterSalary(input('Enter Employee Salary (####.##): '))
												break
											except Exception as e:
												print('ERROR:',str(e))										
									else:
										raise Exception('')
										break
								except Exception as e:
									print('ERROR: SSN',str(e),'Not Found!')
									break
				except Exception as e:
					print('ERROR: SSN',str(e),'Not Found!')
		#If user selected 5 Export employee informaiton to text file
		elif userSelection == 5:
			while True:
				try:
					#if there are no entries in the EMS system, you cannot export a file
					if len(empDict.keys()) <1:
						print('\nThere are no employees to export!')
						break
					else:
						print('----- Export Employee Records -----')
						#Capture file name
						fileName = input('Enter Export File Name: ')
						filePath = getFilePath(fileName)
						#create list of SSN's to access employee(s) in the system
						for key in empDict.keys():
							empList.append(key)
						#check to see if the file already exists
						if os.path.exists(filePath):
							overWrite = str(input('File name already exists! Overwrite File? Y/N?'))
							if overWrite.upper() == 'N':
								#add a 1 at the end of the file name
								filePath = getFilePath(fileName + '1')
						#export employees in the system
						with open(filePath, 'w+') as file:
							file.write('EMS Export ' +  fileName + '\n')
							for ssn in empList:
								file.write('%s,%s,%s,%s,%s\n' %(empDict[ssn].SSN,empDict[ssn].Name,empDict[ssn].Phone,empDict[ssn].Email,format(empDict[ssn].Salary,'.2f')))
						#empty the SSN list
						empList = []
						#tell the user where the export file is located
						print('Export Successful!','File Path: ',filePath)
						break
				except Exception as e:
					print('ERROR:', str(e))
		#If user selected 6 Import employee information to text file
		elif userSelection == 6:
			while True:
				try:
					print('----- Import Employee Records -----')
					importList = []
					#look for import files in script path
					for root, directories, files in os.walk(folderPath):
						for file in files:
							#check for txt files only
							if '.txt' in file:
								#append file path to importList
								importList.append(os.path.join(folderPath,file))
					#print import file list for user selection
					for i in range(len(importList)):
						print(str(int(i)+1) + ':' + os.path.split(importList[i])[1])
					#User Selection
					importSelect = int(input('Select An Import File By Number or 0 to exit: '))
					if importSelect == 0:
						#if user selects 0 exit the import screen
						break
					elif importSelect > len(importList):
						#if user selects something else, throw error
						raise Exception('You can only select the available options or 0 to exit!')
					else: 
						#import the file
						with open(importList[int(importSelect)-1], 'r') as importfile:
							#read each line of the file
							lines = importfile.readlines()
							for i in range(len(lines)):
								#skip the first line
								if i>0:
									#parse employee data and split by comma
									employeeData = lines[i].replace('\n','').split(',')
									#use function to update the EMS dictionary
									updateEmpSSN(employeeData[1],employeeData[0],employeeData[2],employeeData[3],employeeData[4])
							print('(%d) employees added to the EMS!\n' % (len(lines)-1))
				except Exception as e:
					print('ERROR:',str(e))
	except Exception as e:
		print('\nERROR:','You must select a displayed option!')