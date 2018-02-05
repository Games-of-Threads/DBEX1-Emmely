# Database exercise 1 (Key-Value Stores)
This is a mini project for the database course. The exercise is based off the description in the bottom of this [resource](https://github.com/datsoftlyngby/soft2018spring-databases-teaching-material/blob/master/lecture_notes/01-Intro_to_DB.ipynb)
## Description
### Simple DB with Hashmap-based Index
My program is a Python Class that can be imported as a module. Following functionality is implemented:
- Implements a Hashmap-based index. In Python a HashMap is called Dictionary.
- Implements functionality to store your data on disk in a binary file.
- Implements functionality to read your data from disk again, so that you can reinstantiate your database after a shutdown.

### Little bit about the implementation


In short what the program does:
- It keeps a in-memory Dictionary of all the keys (and some values) in the Key-Value store.
- For every read the in-memory Dictionary is updated with the value. Making reads of common values fast.
- The in memory also holds all the keys.
- When a key-value pair is to be persisted or updated. It saves the key to the in-memory Dictionary. The in-memory Dictionary is also saved as a binary-file for back up in this operation.
- The value to be persisted is saved in one out of 10 Dictionaries as a key-value pair. This Dictionary is always saved to disk as a binary. 
A hash value of the key determines suffix of the file to load or save to. 
The reason that the values are persisted in 10 equal files is that we can store the key values independent of the RAM. [Inspiration to the solution](http://blog.gainlo.co/index.php/2016/06/14/design-a-key-value-store-part-i/)

This Python library [Pickle](https://docs.python.org/3.1/library/pickle.html) was chosen for the marshaling and unmarshaling of the Dictionary.
A Python Dictionary can hold any object type so in this implementation the values in the database can be of mixed types.



------------------
## How to Run an Example Online (no Python installation needed)

If you don't have Python installed and want to test the program you can use this option. [Paste the content in main.py to this page and hit execute](https://www.tutorialspoint.com/execute_python_online.php).You can test the Class direcly without importing it as a module. You can however not see any of the created files therefor I have uploaded the resulting files in the folder "fruits".

## How to Run the Example Program with Python Installed

- Pre-conditions: Have Python installed. If you do not have Python 3 installed. [Follow this guide for Linux](http://docs.python-guide.org/en/latest/starting/install3/linux/)
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

## How to Use the STORE Class as a Module

Because store.py is a local library I recommend to put this file in the same directory as your Python program.
In your Python program import the store module and instantiate a STORE like this code example shows:

```
import store.
mystore = store.STORE('fruits')

store.tell_me_about_the_store()
store.put_val( 'ananas' ,  '111' )
store.put_val( 'mango' ,  [1,2,3,] )
store.put_val( 'banana' ,  {'333':333} )

store.put_val( 'apple' ,  '222' )
store.put_val( 'pear' ,  '333' )
print(store.read_val('pear'))
store.read_val( 'apple' )
print(store.get_all())
store.delete_val('pear')
print (store.get_all())
print (store.get_all_by_type())

```



- The database is initialized with a new STORE instance. A empty database is saved to binary file. An existing database is also loaded if a database with input string exists.

```[instance] = STORE(<string>)```
 
- This will save the data in the key value store. the key must be string. Value can be any object type.

```[instance].put_val( <key as string> ,  <value> )```

- This will return the value of the given key

```[instance].read_val( <key as string> )```

- This will delete the value of the given key

```[instance].delete_val( <key as string> )```

- This will return a Python Dictionary of all data as key-values. Probably not so smart if the dataset becomes huge

```[instance].get_all()```

- This will return a Python Dictionary of all data as key-object type. Probably not so smart if the dataset becomes huge

```[instance].get_all_by_type()```

- Info about the database

```[instance].tell_me_about_the_store()```





-------------

Implementation by Emmely Lundberg cph-el69