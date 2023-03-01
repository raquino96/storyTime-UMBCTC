# Intro
print('=============================')
print('Welcome to AdventureWorld')
print('=============================')
print("")

# Pick a story
print("So, you want to go on an adventure. Alright, let's pick from what's available:")
print("a) Do your taxes.")
print("b) Figure out what that mysterious sound is when you turn on your dryer.")
print("c) Ask your neighbor to stop blasting music at 4am. ")
print()
userSelection = input("Which adventure would you like to attempt: ")
print("")
print("")

# Story 1: multiple choice scenario
if userSelection == 'a':
  print("So you decided to tackle the insurmountable task of doing your taxes. As you pull out your protractor and abacus, a demigorgon pops out from your filing cabinet! You have the following courses of action:")
  # multiple choice selections
  print("a) Try to hit the demigorgon with the curved part of your protractor.")
  print("b) Cower in fear and offer an unripe avocado.")
  print("c) Break your abacus and cover the ground with the beads.")
  print("")
  gorgonSelect = input("What would you like to try: ")
  print("")

  # results of multiple choice selection
  if gorgonSelect == 'a':
    print("You grasp your protractor like a brass knuckle and attempt to strike the demigorgon. The demigorgon easily sidesteps your attempt and then walks over to your computer and implicates you in tax fraud. You are arrested and sent to jail for 50 years.")
  elif gorgonSelect == 'b':
    print("The sight of this monstrosity consumes you with fear and you quickly fall down into a fetal position. You scramble around you and find an unripe avocado that you had planned to eat later in the week, but decide to offer it to the demigorgon in a last ditch effort. The demigorgon slurps down the avocado and makes a satisfied grunt. It hands you a USB with the prviate passkey to a bitcoin wallet with 1000 BTC and then crawls back into your filing cabinet. You retire and live a long, happy life.")
  elif gorgonSelect == 'c':
    print("You decide to try to impede the demigorgon by breaking your abacus and spilling the beads between you and the demigorgon. Unfortunately, the demigorgon has superhuman stability and is easily able to walk on the beads without losing balance. It walks over to your cell phone and drains all of your money from your accounts, leaving you destitute. You quickly starve to death because you never learned how to forage for berries when you were a kid.")
    

#Story 2 numeric input

elif userSelection == 'b':
  print("After the news reported that numerous families were disappearing after their dryers started making clunking sounds, you decide to check your dryer. You put a load of laundry in, turn on the dryer, and then wait a few minutes. Eventually, you start hearing the clunking sound. As you begin investigating, you notice that your dryer actually has a 4-quarter slot. ")
  print("")
  userQuarter = int(input("How many quarters would you like to insert: "))
  print ("")
  #output for different scenarios based on number entered
  if userQuarter == 4:
    print("It seems that the dryer is satisfied. The clunking ceases, and your laundry is adequately dry and fluffy at the end of your cycle. This continues on for the rest of your long life. ")
  elif userQuarter < 4:
        print("Whatever is in the machine is not satisfied. The loading door opens and something grabs you and yanks you inside......your body is never found")
  else:
        print("You jam the machine by trying to stuff too many quarters into the slots. The dryer heats up, almost as if it's angry, and you pass out. Eventually the room heats up so much that your body liquifies and runs down the drain. No one ever figures out what happened to you. ")

#Story 3 'yes' or 'no'
elif userSelection == 'c':
  print("Your neighbor has been consistently throwing massive ragers that run all night into the wee hours of the morning. You've barely slept in the last couple of months due to this. Finally, you decide to confront your neighbor during his latest party. You pound on his door until he opens. He quickly recognizes you and asks \"Is the mitochondria the powerhouse of the cell?\" ")
  cellAnswer = input("You mull on his question for a second, and realize it's a 'yes' or 'no' answer: ")
  print("")
  #output for 'yes', 'no', and any other input
  if cellAnswer == 'yes':
    print("Your neighbor realizes that you are correct, and immediately shuts down the party and apologizes to you. Years later, you find out that your neighbor was a scientist and your answer was the missing component that allowed him to cure cancer. You and your loved ones live long, healthy lives as a result.")
  elif cellAnswer == 'no':
    print("Your neighbor frowns as if he hoped the answer would be different. Days later, you find out that his parties were actually huge research sessions that were attempting to cure numerous diseases. Unfortunately, your answer of 'no' caused your neighbor to ignore mitochondrial research and accidently created a new disease that turns humans inside out. You contract this disease and live a long, painful, and isolated life.")
  else:
    print("Your neighbor surmises that you are either intoxicated or unintelligent as he could make no sense of your answer. He decides to steal your car as he feels you are a danger on the road. You quickly starve to death because you never figured out how to use Uber Eats or DoorDash.")
