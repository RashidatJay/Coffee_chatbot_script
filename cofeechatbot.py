# Define your functions
def coffee_bot():
  print('Welcome to the cafe!')
  size=get_size()
  drink_type=get_drink_type()
  print(f' Alright, thats a {size} {drink_type}!')
  name=input('Can I get your name please?')
  print(f' Thanks {name}! Your drink will be readly shortly.')
  more_drinks()
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res =='c':
    return 'large'
  else:
   print_message()
   prompt= get_size()
   return prompt
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response')
def get_drink_type():
  res=input('''
  What type of drink would you like?
  [a] Brewed Coffee
  [b] Mocha
  [c] Latte
  ''')
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    get_drink_type()
def order_latte():
  res= input('''
  And what kind of milk for your latte?
  [a] 2% milk
  [b] Non-fat milk
  [c] Soy milk
  ''')
  if res=='a':
    return 'latte'
  elif res=='b':
    return 'non-fat latte'
  elif res=='c':
    return 'soy latte'
  else:
    order_latte()
def more_drinks():
  another_order=input('Will you like to order another drink, Yes or No:')
  if another_order == 'Yes':
    size=get_size()
    drink_type=get_drink_type()
    print(f'Your second drink is {size} {drink_type} and its coming right up!')

  else:
    print('Thanks for drinking our cofee, we really appreciate it!')

coffee_bot()

