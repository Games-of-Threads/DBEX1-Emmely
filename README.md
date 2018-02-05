# Database exercise 1 (Key-Value Stores)
This is a mini project for the database course. The excersise is based off the description in the buttom of this [resource](https://github.com/datsoftlyngby/soft2018spring-databases-teaching-material/blob/master/lecture_notes/01-Intro_to_DB.ipynb)
## Description
### Simple DB with Hashmap-based Index
My program is a Python Class that can be imported as a module with the following functionality:
- Implements a Hashmap-based index in Python  called Dictionary.
- Implements functionality to store your data on disk in a binary file.
- Implements functionality to read your data from disk again, so that you can reinstantiate your database after a shutdown.
Hint: You do not want to serialize and dematerialize the an in memory Hashmap containing all data directly. Instead, you in memory index based on a Hashmap contains information on where in you database file a piece of information is stored.
The result is a Python module which can be used in any Python (3) program. 

In short what the program does:
- It keeps a in-memory Dictionary of all the keys (and some values) in the Key-Value store.
- For every read the in-memory is updated with the value. Making reads of common values fast.
- The in memory also holds all the keys so be it that a none existing key is asked for the in-memory Dictionary can also answer fast. 
- When a key-value pair is asked to be persisted then it saves only the key to the in-memory Dictionary. The in-memory Dictionary is also saved as a binary-file for back up.
- The value to be persisted is saved in one out of 10 Dictionaries as a key-value pair. This Dictionary is always saved to disk as a binary.
The hashed key determines suffix  of the file to load and save to.
The reason that the values are persisted in 10 equal files is that we can store the key values independent of the RAM.

[Inspiration to the solution](http://blog.gainlo.co/index.php/2016/06/14/design-a-key-value-store-part-i/)


------------------
## How to run example with out installation (example program)
[Paste the content in main.py to this page and hit execute](https://www.tutorialspoint.com/execute_python_online.php)
If you don't have python installled and want to test the program you can use this option. You can test the Class direcly without importing it as a module. You can however not see any of the created files therefor I have uploaded the resulting files in the folder "fruits".

## How to run the example program with Python installed

- Pre-conditions: Have Python installed. If you do not have Python 3 installed. [Follow this guide for linux](http://docs.python-guide.org/en/latest/starting/install3/linux/)
or [this guide for Windows](https://www.python.org/downloads/)

To run the example program, simply start by cloning this repository. From your preferred terminal. (I'm using git bash)
```
git clone https://github.com/Games-of-Threads/DBEX1-Emmely.git
```
Then, go to the directory of the repository, and build and run with the following command.
```
python example.py
```
The output of the program is printed.

## How to use the STORE Class as a module

Because store.py is a local library I recommand to put this file in the same directory as your Python program.
In your Python program import the store module and instantiate a STORE like this code example shows:

```
import store.
mystore = store.STORE('fruits')

```



- The database is initalized with a new STORE instance. A empty database is saved to binaryfile by this command. An existing database is loaded with this command.
```[instance] = STORE(<string>)```
 
- This will save the data in the key value store. the key must be string. Value can be any Python type.

```[instance].put_val( <key as string> ,  <value> )```

- This will return the value of the given key

```[instance].read_val( <key as string> )```

- This will delete the value of the given key

```[instance].delete_val( <key as string> )```

- This will return a Python Dictionary of all data as key-values. Probably not so smart if the dataset becomes huge

```[instance].get_all()```

- This will return a Python Dictionary of all data as key-type of value. Probably not so smart if the dataset becomes huge

```[instance].get_all_by_type()```



-------------