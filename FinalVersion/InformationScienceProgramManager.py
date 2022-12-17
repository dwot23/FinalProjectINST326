"""Final Project INST326
Name: Dwight Guevara, Tao Lin, Abroo, Melika Moshirian Fard
Desc: An Information Science Program Manager that checks whether or not the student has finished their Information Science Program."""
import csv
class classes:
    
    def __init__(self, classes:str):
        """Takes a list of classes from the csv file and puts them into a class object
    
    Args:
        classes: Classes that the student has taken according to the csv file.
        """
        self.classes=classes
        
    def iscore(self):
        """Takes own class and determines if class is a core class or not.
    
    Args:
        self
    Returns:
        core (bool): Returns a boolean value on whether or not the class is a core class.
        """
        if self.classes in ['inst301', 'inst311', 'inst314', 'inst326', 'inst335', 'inst327', 'inst352', 'inst362', 'inst346', 'inst490', 'engl393']: #returns true if it contains any of these classes
            core=True
            return core
        else: #returns false if it does not contain any of core classes
            core=False
            return core
    def __repr__(self):
        """Represents returns into something readable.
    
    Args:
        self
    Returns:
        self.classes (string): Returns the student class.
        """
        return f'{self.classes}'

    
def main(studentlist:str):
    """Takes the student classes file and puts into a lists. It iterates through each row (each row containing one class that the student has taken) and separates each class as either core or elective.
    It checks if the student has finished their core or elective classes. The program closes if it confirms that the student has taken classes necessary to graduate. If the student has not finished their course work,
    it will notify the student and can give information on classes that the student has not taken
    
    Args:
        studentlist (str) : the path of the file that contains the student's courses taken.
    """
    studentmajorclasslist =[]
    studentelectiveclasslist=[]
    with open(studentlist) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader: #for each row in the csv, get first element and run it as an object for classes. Gather bool value on whether or not the calss is a core class or not.
            studentclass=classes(row[0]) #creates a class object
            corevalue=studentclass.iscore() #checks if the the class is a core class or not
            if corevalue is True: 
                
                studentmajorclasslist.append(str(studentclass)) #append to major class list if the class is a core class
            else:
                studentelectiveclasslist.append(str(studentclass))    #append to elective class list if the class is an elective class
    finishedcoreclass=coreclasses(studentmajorclasslist) #run function and return whether or not the student has finished his/her core classes
    finishedelectiveclass=electiveclasses(studentelectiveclasslist)  #run function and return whether or not the student has finished his/her elective classes
    if finishedcoreclass==True and finishedelectiveclass ==True: #if both core and elective classes are finished, end program with a short congratulatory print statement
        print("Congratulations, you are ready to graduate. Please seek your counselor for further steps.")
        print("Thank you for using the Information Science Program Manager.")
    else: #if the student has not finished his/her classes, offer whether or not they want to see more information on any class that is currently available
        print("You have not completed the Information Science Program as of now. Would you like to see any information for the available classes (y/n)?") 
        answer=input()
        while answer == ('y' or 'n'): #used to make sure answer are within parameters
            if answer=='y':
                classinformation()         
                break
            elif answer=='n':
                break
            else:
                print("Please use 'y' or 'n' in your answer")
        print("Thank you for using the Information Science Program Manager.")
    
def coreclasses(studentmajorclasslist):
    """Takes a list of strings from student core classes according to the main function. It will check if the student has completed all core classes necessary to graduate. If not, the function will output
    core student classes that the student has not taken yet.
    
    Args:
        studentmajorclasslist (list) : the list of strings from core student classes that the student has taken from main function.
    Returns:
        bool: A boolean value that shows whether or not the student has completed core classes
    """
    requiredmajorclass=['inst314', 'inst352', 'inst346', 'inst490', 'engl393', 'inst327', 'inst311', 'inst326', 'inst301']
    isEmpty = (set(requiredmajorclass).difference(set(studentmajorclasslist)) == set()) #gets bool value on whether or not the difference of the student core class and required core classes is empty
    if isEmpty: #if it is empty, print statement
        print("You have taken all core classes necessary.")
        return True
    else: #if it is not empty, print classes that are still missing
        print("The required classes you are still missing: ", set(requiredmajorclass).difference(set(studentmajorclasslist)))
        return False

def electiveclasses(studentelectiveclasslist):
    """Takes a list of strings from student elective classes according to the main function. It will check if the student has completed the number of elective classes necessary to graduate. If not, the function will output
    elective classes student classes that the student has not taken yet.
    
    Args:
        studentelectiveclasslist (list) : the list of strings from elective student classes that the student has taken from main function.
    Returns:
        args (ArgumentParser)
    """
    electiveclasslist=['inst365', 'inst364', 'inst366', 'inst464', 'inst466', 'inst467', 'inst354', 'inst377', 'inst414', 'inst447', 'inst462', 'inst341', 'inst441', 'inst442', 'inst443', 'inst448', 'inst401', 'inst402', 'inst408A', 'inst452'] #all available elective classes
    classcount=0
    for i in studentelectiveclasslist: #count how many electives the student has taken
        classcount=classcount+1
    if classcount>=9: #if the student has taken 9 or more electives, it confirms that they have finished all their electives, rreturn True
        print("You have finished all the required electives.")
        return True
    elif classcount<9: # if the student has less than 9 electives, print how many electives are left
        print(f'You have {9-classcount} elective classes left to take.')
        print("Would you like to see the elective classes that are available to you?(y/n)")
        answer=input()
        while answer == ('y' or 'n'): #while statement to make sure that answer is within parameters
            if answer=='y': 
                print("Here are the elective classes you have not taken yet: ", set(electiveclasslist).difference(set(studentelectiveclasslist))) #show available elective classes that have not been taken by student
                break
            elif answer=='n':
                break
            else:
                print("Please use 'y' or 'n' in your answer")
        return False

def classinformation():
    """A function that will output any class information that the user has inputted. It draws from a csv database that contains all inst classes that are available.
    
    Args:
        none
    Returns:
        none
    """
    loop=True #used to keep loop
    instclass=input("What class would you like to see? (Format: instxxx): ") #value that the student inputs, it is the class that the student would want more information on
    classlist=[]
    with open('classsummaries.csv') as csv_file: # takes every class from the csv file and puts it into a list
        csv_reader = csv.reader(csv_file, delimiter=',') 
        for row in csv_reader:
            classlist.append(row[0])
    while loop==True: 
        with open('classsummaries.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',') 
            for row in csv_reader: #checks each row whether or not the first element of the csv is equal to the student input
                if row[0]==instclass:
                    print(f'{row[0]}: {row[1]}') #prints the summary of the class when the student input == row[0]
                    answerloop=True #used to loop answer
                    while answerloop==True:
                        answer=input('Input another class or type end to stop: ')
                        answer.replace(" ", "")
                        if answer=='end': #breaks current answer loop and csv loop
                            loop=False
                            answerloop=False
                            print('Thank you for using the Information Science Program Manager.')
                            break
                        elif answer.startswith('inst') and answer in classlist: #set the new value of instclass, break current loop and reloop the 'for loop' that contains csv==instclass iteration
                            instclass=answer
                            answerloop=False
                        else: #invalid input
                            print("Invalid input, please try again.")         
                
                           
if __name__ == "__main__":
    """Intializes once the program started, asks for user input and outputs depending on user input.
    
    """
    print("Thank you for using the Information Science Program Manager. Please input your file name (must be in csv form) or type 'class info' for class information.")
    print("If this is your first time using this program, type 'help'." )
    useranswer=input()
    if useranswer == 'help': #used as a help tooltip to make sure the user knows what to do.
        print("To use this program, please create a csv file in the same folder as this program. List all classes that you have taken in one column.")
        print("It should be in the form of course code with course number with no spaces.")
        print("Ex: 'inst326' can be inputted in a cell." )
        print("Please run the program again once you have completed this task.")
    elif useranswer=='class info':# used to go straight into any class information, does not need csv file
        classinformation()
    elif useranswer.endswith('.csv'): #takes the csv file path and runs main function.
        main(useranswer)
    else:
        print("Invalid input, please run the program again.")
