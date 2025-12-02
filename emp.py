import pytest
def emp_details(name,emp_id,department,salary):
    result = (
       f"Employee Name:{name}\n"
       f"Employee ID:{emp_id}\n"
       f"Department:{department}\n"
       f"Salary:{salary}"
    )
    return result
if __name__=="___main___":
    name="Alice"
    emp_id="E1001"
    departmant="IT"
    salary=55000
    print(emp_details(name,emp_id,department,salary))
