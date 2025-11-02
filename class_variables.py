# Key take-away: 
# (1) Object refers to instance attributes first, then cls attributes
# (2) Properly choose to use instance variable or class variable
# (3) Classmethod mainly used to modify class attr or used as a constructor
class Employee:

    raise_amount = 1.04    # Example that make sense to be controlled by object itself
    num_of_emps = 0        # Example that should be handled by class
    def __init__(self, first_name, last_name, pay):
        self.fisrt_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)    # Use self.raise_amount to allow instance to overrides it's own constant

    @classmethod                                        # Receive class arugment instead of instance
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod                                        # Classmethod as constructor which provides multiple ways of creating objects
    def from_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, pay)
    
    @staticmethod                                       # Static method take no instance or class, but defined inside a class because it's logically connected to the class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

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

### Modify class attr from class  - untouchable from instance
def increase_num_of_emp():
    print(Employee.num_of_emps)
    emp_3 = Employee('Test2', 'User2', 60000)
    print(Employee.num_of_emps)
# increase_num_of_emp()

### Modify class attr from class  - class method
def modify_raise_amount_by_cls_method():
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    Employee.set_raise_amount(1.05)     # Equivalent to Employee.raise_amount = 1.05
                                        # Equivalent to emp_1.set_raise_amount = 1.05, but rarely do this
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
# modify_raise_amount_by_cls_method()

### Implement Classmethod as a constructor
def create_employee_from_string():
    emp_1_str = 'John-Doe-70000'
    emp_2_str = 'Steve-Smith-30000'
    new_emp_1 = Employee.from_string(emp_1_str)
    print(new_emp_1.__dict__)
# create_employee_from_string()

### Implement Staticmethod
def check_workday():
    import datetime
    my_date1 = datetime.date(2016, 7, 10)
    my_date2 = datetime.date(2025, 10, 30)
    print(Employee.is_workday(my_date1))
    print(Employee.is_workday(my_date2))
# check_workday()