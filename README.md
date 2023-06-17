# least-recently-used
This Python program implements a Least Recently Used (LRU) cache using a dictionary as the cache and a list as a queue to keep track of the order of keys. The cache has a fixed capacity, which is specified by the user when initializing the cache object.
The program provides a command-line interface for interacting with the cache. The following commands are supported:

init <capacity>: Creates a new cache with the specified capacity.
get <key>: Retrieves the value associated with the given key from the cache, if it exists. Otherwise, returns 1.
put <key> <value>: Inserts or updates the key-value pair in the cache. If the key already exists in the cache, its value is updated. If the cache is full, the least recently used key-value pair is evicted to make room for the new one.
The state of the cache is printed after each command execution.

## Usage: 
1. Run main file.
2. The program will prompt you to enter commands until you enter an invalid or exit command.
3. After entering the command, the program will displays something based on command.

### Example: 
Here's an example session demonstrating the usage of the program:

~.~ Hello, Welcome To This Program ~.~

Enter A Command: init 2
Ok
==> Cache State: {}

Enter A Command: put 1 1 
null
==> Cache State: {1: 1}

Enter A Command: put 2 2 
null
==> Cache State: {1: 1, 2: 2}

Enter A Command: get 1
1
==> Cache State: {1: 1, 2: 2}

Enter A Command: put 3 3 
null
==> Cache State: {1: 1, 3: 3}

Enter A Command: get 2
-1
==> Cache State: {1: 1, 3: 3}

Enter A Command: put 4 4
null
==> Cache State: {3: 3, 4: 4}

Enter A Command: get 1 
-1
==> Cache State: {3: 3, 4: 4}

Enter A Command: get 3 
3
==> Cache State: {3: 3, 4: 4}

Enter A Command: get 4
4
==> Cache State: {3: 3, 4: 4}

Enter A Command: <anything>

Thank You For Choosing Us :)
>>> Developed By Maryam Fakhraei & Amirhossein Naseri <<<