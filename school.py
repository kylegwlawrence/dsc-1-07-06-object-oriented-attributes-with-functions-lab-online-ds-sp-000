class School():
    
    def __init__(self, name):
        #initiate a school with a name
        self.name = name
        self._roster = {}
        
    def roster(self):
        #method to return the roster for a school
        return self._roster
    
    def add_student(self, name, grade):
        # add name and grade to private variables
        self.name = name
        self._grade = grade
        #if the grade already exists in roster
        if grade in self._roster:
            #add the new kid to the grade
            self._roster[grade].append(name)
        # if grade not in roster
        else:
            #set the new grade equal to a list containing the new name
            self._roster[grade] = [name] 
        # print the updated roster
        return self.roster()
    
    def grade(self, grade):
        # method to return the roster of given grade
        # set equal to dict
        return self._roster[grade]
    
    def sort_roster(self):
        for key, value in self._roster.items():
            # sort each list in place
            self._roster[key].sort()
        #return the dict with alphabetical roster orders
        return self.roster()
            
        