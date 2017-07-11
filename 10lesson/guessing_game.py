import random
number_of_guesses = 10
number = random.randint(1,100)
print("Guess the number I have")

 
while number_of_guesses <=10:
    print("You have "+str(number_of_guesses)+ " chances left")
    guess=input()
    guess=int(guess)
    
    number_of_guesses = number_of_guesses -1
    if guess < number:
        print("Your quess is too low. Keep trying.")
        
    if guess > number:
        print("Your guess is too high. Keep trying")
        
    if guess ==number:
       break
   
if guess == number:
     number_of_guesses =10- number_of_guesses
     number_of_guesses = str(number_of_guesses)
     print("Congratulations you have guessed the right number. Thank you for playing." + "You guessed my number in " + number_of_guesses +  "guesses!")
if guess != number:
        number = str(number)
        print("No. The number was thinking of was" + number)
       
        
    
