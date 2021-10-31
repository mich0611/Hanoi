from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
stacks = [left_stack, middle_stack, right_stack]
#Set up the Game
num_disks = int(input('\nHow many disks do you want to play with?\n'))
condition = True
while condition:
  if num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))
  else:
    condition = (num_disks < 3)
    print('Successfully Enter')

for i in range(num_disks):
  left_stack.push(num_disks - i)
left_stack.print_items()
num_optimal_moves = 2**num_disks - 1
print("\nThe fastest you can solve this game is in {x} moves".format(x = num_optimal_moves))

#Get User Input
def get_input():
  choices = [i.get_name()[0] for i in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print('Enter {l} for {n}'.format(l = letter, n = name))
    user_input = input('')
    if user_input in choices:
      for i in range(len(stacks)):
        if choices[i] == user_input:
          return stacks[i]
    else:
      print('Invalid input, please enter {lst}'.format(lst = choices))

#Show the figure
def show():
    print('\nAfter your moves\n')
    left_stack.print_items()
    middle_stack.print_items()
    right_stack.print_items()

#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for i in stacks:
    i.print_items()
  while True:
    print('\nWhich stack do you want to move from?\n')
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    # make real move
    while True:
      if to_stack.is_empty() or from_stack.peek() <= to_stack.peek():
        disk = from_stack.pop()
        to_stack.push(disk)
        num_user_moves += 1
        show()
      else:
        print("\n\nInvalid Move. Try Again")
      break
print("\n\nYou completed the game in {s} moves, and the optimal number of moves is {o}".format(s = num_user_moves, o = num_optimal_moves))

    




