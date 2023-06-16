from LRU import LRU
from termcolor import colored

def main():
    cache = None

    print(colored("\n~.~ Hello, Welcome To This Program ~.~", "yellow", attrs=["dark"]))

    while True:
        command = input("\nEnter A Command: ").split()
        
        if command[0] == "init":
            capacity = int(command[1])
            cache = LRU(capacity)
            print(colored("Ok", color="green", attrs=["dark"]))
        elif command[0] == "get":
            key = int(command[1])
            value = cache.get(key)
            print(colored(value, color="green", attrs=["dark"]))
        elif command[0] == "put":
            key = int(command[1])
            value = int(command[2])
            cache.put(key, value)
            print(colored("null", color="green", attrs=["dark"]))
        else:
            break
        print(
            colored(f"==> Cache State: {cache.cache}", color="blue", attrs=["dark"]))

    print(colored("\nThank You For Choosing Us :)\n>>> Developed By Maryam Fakhraei & Amirhossein Naseri <<<", "magenta", attrs=["dark"]))
    
if __name__ == "__main__":
    main()
