def main():
    filename = input("Please enter the file name: ")
    filepath = "/Users/janewan/Documents/cs5001/hw05/" + filename
    try:
        f = open(filepath, "r", encoding="utf-8")
    except OSError as e:
        print("Unable to open no_such_file.txt")
        return()
    
    stripped_line = f.readlines()
    print(stripped_line)


main()