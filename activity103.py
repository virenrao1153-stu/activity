class Employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print("Destructor called")
def Create_obj():
     print('function end...')
     return object
print('Calling Create obj() function...')
obj = Create_obj()
print('Program End...')
