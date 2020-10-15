first_term = 0

while first_term < 10:   
    second_term = 1
    first_term += 1
    while second_term < 11:
        product = second_term * first_term
        print(f"{first_term} x {second_term} = {product}\n")
        second_term += 1
    if first_term != 10:
        print("...\n")
    
    
    

