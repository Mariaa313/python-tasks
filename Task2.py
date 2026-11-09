#1 ინდექსები და Slicing
word = "programming"
print(word[0])      
print(word[-1])     
print(word[-3])     
print(word[:4])     
print(word[-4:])    
print(word[::2])    
print(word[::-1])   

#2. ელფოსტის დაშლა
email = input("Enter your email address: ")
username, domain = email.split("@")
print("Username:", username)
print("Domain:", domain)  

#3. ტელეფონის ნომრის გასუფთავება
phone = input("Enter your phone number: ")
phone = phone.replace(' ', '')
phone = phone.replace('-', '')
print("Cleaned phone number:", phone)

#4. URL-მისამართის (slug) გენერატორი
title = input("Enter a title: ")
title = title.lower()
words = title.split()
slug = '-'.join(words)
print(slug)

#5. სტუდენტის ბარათი (f-string)
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
language = input("Enter your favorite programming language: ")

print('=' * 25)
print(f"Name: {name.title()}")
print(f"Age: {age}")
print(f"City: {city.title()}")
print(f"Favorite language: {language.upper()}")
print('=' * 25)