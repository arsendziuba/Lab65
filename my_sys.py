import sys

def main():
    # Print computer platform
    print("Computer Platform:", sys.platform)

    # Print installed Python version
    print("Installed Python Version:", sys.version)

    # Check and print size of the string object "abc"
    string_size = sys.getsizeof("abc")
    print("Size of 'abc' string object:", string_size, "bytes")

    # Get the value of n from script arguments or use default value 11
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            n = 11
    else:
        n = 11

    # Create a list variable with number items from 0 to n
    numbers_list = list(range(n))

    # Use a for loop to write every number item into system stdout
    for number in numbers_list:
        sys.stdout.write(str(number))

    # In case of n%2 == 0, exit script execution with n code
    if n % 2 == 0:
        sys.exit(n)

if __name__ == "__main__":
    main()
