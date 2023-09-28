def draw_asterisk_tree(height):
    # Draw the tree
    print(" " * (height - 1) + "*")
    print(" " * (height - 2) + "***")
    print(" " * (height - 3) + "*****")
    print(" " * (height - 4) + "*******")
    print(" " * (height - 5) + "*********")
    print(" " * (height - 6) + "***********")
    print(" " * (height - 7) + "*************")
    print(" " * (height - 8) + "***************")

    # Draw the trunk
    print(" " * (height - 1) + "|")


height = 15
draw_asterisk_tree(height)
