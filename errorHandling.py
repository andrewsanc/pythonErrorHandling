'''
Python Jupyter - Error Handling. Try and Except block
'''
#%%
while True:
  try:
    age = int(input('What is your age: '))
  except ValueError:
    print('Please enter a valid number')
  except ZeroDivisionError:
    print('Please enter age > than 0')
  else:
    print(f'you are {age} years old')
    break

#%%
