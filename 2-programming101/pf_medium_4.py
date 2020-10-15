width = int(input("Width?\n"))
height = int(input("Height?\n"))


empty_w = int(width - 2)
empty_h = int(height - 2)
edges = "*" + (" " * empty_w) + "*" + "\n"
line_stars = "*" * width + "\n"
middle = edges * empty_h

print(line_stars + middle + line_stars)