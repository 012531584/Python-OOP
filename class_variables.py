# Key take-away: 
# (1) Object refers to instance attributes first, then cls attributes
# (2) Properly choose to use instance variable or class variable
class Employee:

    raise_amount = 1.04    # Example that make sense to be controlled by object itself
    num_of_emps = 0        # Example that should be handled by class
    def __init__(self, first_name, last_name, pay):
        self.fisrt = first_name
        self.last = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)    # Use self.raise_amount to allow instance to overrides it's own constant


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

############## Check apply_raise function
def check_apply_raise():
    print(emp_1.pay)
    emp_1.apply_raise()
    print(emp_1.pay)
# check_apply_raise()

############## Check class attribute
### Modify class attr from class
def modify_raise_amount_by_cls():
    print(emp_1.raise_amount)       # When accessing attribute of an instance, it'll check if instance contains the attribute
                                    # If it doesn't, it'll check the attribute from it's class or inherits
    Employee.raise_amount = 1.05
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
# modify_raise_amount_by_cls()

### Modify class attr from instance
def modify_raise_amount_by_inst():
    print(emp_1.__dict__)
    emp_1.raise_amount = 1.05
    print(emp_1.__dict__)           # emp_2 now has raise_amount attr, so it doesn't refer Employee cls attr
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
# modify_raise_amount_by_inst()

### Modify class attr from class  - 2
def increase_num_of_emp():
    print(Employee.num_of_emps)
    emp_3 = Employee('Test2', 'User2', 60000)
    print(Employee.num_of_emps)
# increase_num_of_emp()