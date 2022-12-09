# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:22:27 2022

@author: Tao
"""

import sys
import argparse
import csv

class RequiredClasses:
    
    
    def __init__(self, major:str):
        self.major = major
        
    
    
    def major(self):
        return self.major
    
    def elective(self):
        return self.elective
    
    def major(self,major:str):
        if RequiredClasses.isvalidmajor(major):
            self.major = major
        else:
            RequiredClasses.ismissingclasses(major)
            raise ValueError("Didn't fullfill all major requirements missing classlist", self.ismissingclasses)
        
        
    def isvalidmajor(cls, value:str):
        if value in ['inst314', 'inst352']:
            return True
        else:
            return False
        
        
    def ismissingclasses(cls,value:str):
        
        
        while value == False:
                if value in ['inst314', 'inst352']:
                    print(value)
                else:
                    value == False

def main(filename:str):
    
    classlist = []
    major = str
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            majors = RequiredClasses(major)
            classlist.append(majors)
            
    return  classlist

if __name__ == "__main__":
    """Used to run main
        
    """
    run = main('listofclasses.csv')
    print(run)
