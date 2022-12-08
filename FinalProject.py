"""
Tao
Melika
Dwight
Abroo
"""


class RequiredClasses:
    
    
    def __init__(self, major:str , elective:str):
        self.major = major
        self.elective = elective
    
    
    def major(self):
        return self.major
    
    def elective(self):
        return self.elective
    
    def major(self,major:str):
        if RequiredClasses.isvalidmajor(major):
            self.major = major
        else:
            raise ValueError("Didn't fullfill all major requirements")
        
        
    def isvalidmajor(cls, value:str):
        
        
        while value == False:
            if value in ['inst314', 'inst352']:
            
             value += value[value]
            else:
             return False