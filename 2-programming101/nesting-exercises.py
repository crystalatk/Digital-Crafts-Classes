#1. Create a program that will accept in input that is assigned to the variable pet_name.
    # If pet_name length is less than 3 characters give a message that the name length is too short.
    # If pet_name lenght is more than 3 characters output "AWWW sweet [pet_name]"
    # If pet_name is "Shadow" output ONLY "El Gato Diablo!"
    # If the input is equal to "Daisy" output ONLY "Good Dog!"

pet_name = input("What is your pet's name? ")
p_len = len(pet_name)

if pet_name == "Shadow":
    print("El Gato Diablo!")
elif pet_name == "Daisy": 
    print("Good Dog!")
else:
    if p_len < 3:
        print("Your name is too short. Please put a valid length name.")
    else:
        print(f"AWWW, sweet {pet_name}!")

