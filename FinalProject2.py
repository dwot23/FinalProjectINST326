import sys
import argparse
import csv
class classes:
    
    def __init__(self, classes):
        self.classes=classes
        
    def iscore(self):
        if self.classes in ['inst314', 'inst352', 'inst346', 'inst490', 'engl393', 'engl394', 'inst327', 'inst311', 'inst326', 'inst311', 'inst301']:
            core=True
            return core
        else:
            core=False
            return core
    def __repr__(self):
        return f'\'{self.classes}\''
def main(studentlist:str):
    studentmajorclasslist =[]
    studentelectiveclasslist=[]
    requiredmajorclass=['inst314', 'inst352', 'inst346', 'inst490', 'engl393', 'engl394', 'inst327', 'inst311', 'inst326', 'inst301']
    requiredelectiveclass=[]
    with open(studentlist) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            studentclass=classes(row[0])
            corevalue=studentclass.iscore()
            if corevalue is True:
                studentmajorclasslist.append(studentclass)
            else:
                studentelectiveclasslist.append(studentclass)
    print(studentmajorclasslist)
    print(requiredmajorclass)
    print("The required classes you are still missing: ", set(requiredmajorclass).difference(set(studentmajorclasslist)))



if __name__ == "__main__":
    run = main('studentlist.csv')
