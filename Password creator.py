print("Welcome user to the password creator.")
user = input("Please enter your user name: ")
print("Very well this password will be created based on uppercase, lowercase, numbers and symbols.")
import random
uppercase = 'ABCDEFGHIJKLMÑNOPQRSTUVWXYZ'
numbers = '0123456789'
lowercase = 'abcdefghijklmñnopqrstuvwxyz'
symbols = '[]{}%&$;._/\()-?¿¡!ª><=:ç^+*'
characters = uppercase + numbers + lowercase + symbols
passlength = 22
password = " ".join(random.sample(characters, passlength))
print(user, "your password has been successfully created")
print(password)
