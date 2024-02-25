def main() :
    print("We are in main method")

# When a program run as standalone script and not as an imported modeule
# then __name__ variable value is set to '__main__'

# When this file is imported into any other python script, then __name__ variable value
# will not be the __main__, it will be the name of file which is NameVariable
if(__name__ == '__main__') :
    main()

