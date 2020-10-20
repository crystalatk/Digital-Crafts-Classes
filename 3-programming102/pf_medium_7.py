# 7. Caesar Cipher
# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? Learn about it here.

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

plain = list("abcdefghijklmnopqrstuvwxyz")
message = list("lbh zhfg hayrnea jung lbh unir yrnearq")
decoded = []

for j in message:
    if j == " ":
        decoded.append(j)
    for i in range(0, len(plain)):
        if plain[i] == j:
            decoded.append(plain[i - 13])
     
decoded_str = "".join(decoded)
print(decoded_str)