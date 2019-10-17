'''
Python Jupyter - Error Handling part 2.
'''
#%%
def numSum(num1, num2):
  try:
    return num1 + num2
  except (TypeError, ZeroDivisionError) as err: # You can wrap errors together with parenthesis.
    print(f'{err}. Please Enter some numbers')

print(numSum(1,0))

#%%
