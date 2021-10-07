# https://leetcode.com/problems/employee-importance/

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

# FIRST ATTEMPT
def getImportance(employees, id):
        # i is not the same with id
        # first we need to get a list of all the subordinates
        # then loop over the employee list to tally up the total importance
        
        # recursion function
        # base case: when subordinates is empty, return
        # else: loop
        
        def recursive(sub, employees):
            subordinates = sub
            if sub == []:
                return [];
            else:
                for i in sub:
                    for employee in employees:
                        if i == employee.id:
                            subordinates.extend(recursive(employee.subordinates, employees))
                            break;
                return subordinates
            
        subordinates = []
        importance = 0;
        for employee in employees:
            if employee.id == id:
                subordinates = recursive(employee.subordinates, employees)
                importance += employee.importance
                break;
        

        for e in employees:
            if e.id in subordinates:
                importance += e.importance
        return importance

e = [Employee(1, 5, [2,3]), Employee(2,3,[4]), Employee(3,4,[]),Employee(4,1,[])]
id = 1
print(getImportance(e,id))