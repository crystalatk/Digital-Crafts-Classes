level = 0
width = 9
for level in range(0, width, 2):
    level += 1
    in_rows = "*" * int(level)
    print("{:^30}".format(in_rows))
    



