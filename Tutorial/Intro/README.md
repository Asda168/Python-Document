# What is Python?

    Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
    
    It is used for:
        web development (server-side),
        software development,
        mathematics,
        system scripting.

# What can Python do?

    Python can be used on a server to create web applications.
    Python can be used alongside software to create workflows.
    Python can connect to database systems. It can also read and modify files.
    Python can be used to handle big data and perform complex mathematics.
    Python can be used for rapid prototyping, or for production-ready software development.

# Built-in Data Types
    
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType

# Python Function

## function type()
    The type() function returns the type of the specified object
### Syntax
    type(object, bases, dict)
### [Setting the Data Type](https://www.w3schools.com/python/python_datatypes.asp)
    In Python, the data type is set when you assign a value to a variable:

## Example:
### Instructions
    Inside the editor, complete the following steps:
    Create a variable x with the value 5
    Create a variable y with the value 3.14
    Create a variable z with the value "Hello"
    Print the data type of each variable using type()

### Solutions:
    x = 5
    y = 3.14
    z = "Hello"
    
    print(type(x))
    print(type(y))
    print(type(z))
### Result:
    <class 'int'>
    <class 'float'>
    <class 'str'>
        
## Python Numbers
###    There are three numeric types in Python:
*    int: Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
*    float: Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
*    complex: Complex numbers are written with a "j" as the imaginary part:

#### Example:
    x = 1   # int
    y = 1.2 # float
    z = 1j  # complex

##### Example use int() Variable Type:
    x = int(1)   # x will be 1
    y = int(2.8) # y will be 2
    z = int("3") # z will be 3
##### Example use float() Variable type:
    x = float(1)     # x will be 1.0
    y = float(2.8)   # y will be 2.8
    z = float("3")   # z will be 3.0
    w = float("4.2") # w will be 4.2

##### Example use str() Variable type:
    x = str("s1") # x will be 's1'
    y = str(2)    # y will be '2'
    z = str(3.0)  # z will be '3.0'

## Python Strings:
    Strings in python are surrounded by either single quotation marks, or double quotation marks.
    'hello' is the same as "hello".
    You can display a string literal with the print() function:

##### Example: "Hello World!" is the same as 'Hello World!'
    print('Hello World!') 
    print("Hello World!")

##### Quotes inside Quotes
    You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
    
    Example:

        print("It's alright")
        print("He is called 'Johnny'")
        print('He is called "Johnny"')

##### Assign string to a variable:
    Assigning  a string to a variable is done with the variable name followed by an equal sign and the string:
    
    Example:

        a =  "Hello"
        print(a)

##### Multiline Strings:
    You can assign a multiline sting to a variable by using three quotes.
    
    Example: You can use three single/double quotes:
        
        i = ''' I design and engineer end-to-end web applications — from 
                pixel-perfect frontends to robust backend systems and cloud infrastructure.
                Turning complex problems into clean, scalable solutions.'''
        print(i)

##### String are Arrays
    Like many other popular programming languages, strings in Python are arrays of unicode characters.
    However, Python does not have a character data type, a single character is simply a string with a length of 1.
    Square brackets can be used to access elements of the string.

    Example: Get the charactor at position 1 (remember that first charactor has the index or position 0.)
        
        i = "How are you?"
        print(i[1]) #the result show in index 1 of i array
        # Output: o

##### Looping Through a string  
    Since string are arrays, we can loop thrugh the charactors in a string, with a for loop.
    
    Example: Loop through the letters in the word "Apple":
        
        for i in "Apple":
            print(i)
        # Output:   A
                    p
                    p
                    l
                    e
##### String Length
    To get the length of a string, use the len() function.
    
    Example: The len() function return the length of a string:
    
        i = "Hello, Brother"
        print(len(i)) 
        # Output: 14

##### Check String 
    To check if a certain phrase or charactor is present in a string, we can the key "in".
        
        Example: Check if "free" is present in the following text:
            txt = "The best things in life are free!"
            print("free" in txt)
            #Output = true
        
        *********** Use it in if Statement ***********
        Example:  Check if "free" is present in the following text:
            txt = "The best things in life are free!"
            if "free" in txt:
            print("Yes, 'free' is present.")
            #Output: Yes, 'free' is present.

        *********** Check if NOT ***********
        To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
        
        Example: 
            txt = "The best things in life are free!"
            if "Hello" not in txt: 
                print("No, 'Hello' is not present.")
                # Output: No, 'Hello' is not present.

##### Slicing 
    
    You can return a range of characters by using the slice syntax.
    Specify the start index and the end index, separated by a colon, to return a part of the string.

    Example: Get the characters from position 1 to position 4 (not included):
        msg = 'banana'
        print(msg[1:4])
        #Output: ana

    Example: Get the characters from the start to position 4 (not included):
         msg = 'banana'
         print(msg[:4])
         #Output: bana

##### Modify String
    Python has a set of built-in methods that you can use on strings.

    Upper Case: 
        
        Example: The upper() method returns the string in upper case:
            msg = "Hello, World!"
            print(msg.upper())

    Lower Case:
        
        Example: The lower() method returns the string in lower case:
            msg = "Hello, World!"
            print(msg.lower())

                
    Remove Whitespace:
        
        Example: The strip() method removes any whitespace from the beginning or the end:
            msg = " Hello, World! "
            print(msg.lower()) # return "Hello, World!"

    Replace String:
        
        Example: The replace() method replaces a string with another string:
            msg = "Hello, World!"
            print(msg.replace("H", "J")) #Output: Jello, World!

    Split String:
    
        Example: The split() method splits the string into substrings if it finds instances of the separator:
        
           msg = "Hello, World!"
           print(msg.split(",")) #Output: ["Hello", "World!"]

##### String Concatenation
    To concatenate, or combine, two strings you can use the + operator.
        
        Example: Merge variable a with variable b into variable c:
            
            a = "Hello"
            b = "World"
            c = a + b
            print(c)

        Example: To add a space between them, add a " ":
            
            a = "Hello"
            b = "World"
            c = a + " " + b
            print(c)

##### Format String: 
    F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
    To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

        Example: Create an f-string:
            
            age = 36
            txt = f"My name is John, I am {age}"
            print(txt)

##### Escape Character
    To insert characters that are illegal in a string, use an escape character.
    An escape character is a backslash \ followed by the character you want to insert.
    An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
        
        Example: You will get an error if you use double quotes inside a string that is surrounded by double quotes:
            
            txt = "We are the so-called "Vikings" from the north."
            To fix this problem, use the escape character \":
        
        Example: The escape character allows you to use double quotes when you normally would not be allowed:

            txt = "We are the so-called \"Vikings\" from the north."

##### String Method
    
    Method          Description

    capitalize()	Converts the first character to upper case
    casefold()	    Converts string into lower case
    center()	    Returns a centered string
    count()	        Returns the number of times a specified value occurs in a string
    encode()	    Returns an encoded version of the string
    endswith()	    Returns true if the string ends with the specified value
    expandtabs()	Sets the tab size of the string
    find()	        Searches the string for a specified value and returns the position of where it was found
    format()	    Formats specified values in a string
    format_map()	Formats specified values in a string
    index()	        Searches the string for a specified value and returns the position of where it was found
    isalnum()	    Returns True if all characters in the string are alphanumeric
    isalpha()	    Returns True if all characters in the string are in the alphabet
    isascii()	    Returns True if all characters in the string are ascii characters
    isdecimal()	    Returns True if all characters in the string are decimals
    isdigit()	    Returns True if all characters in the string are digits
    isidentifier()	Returns True if the string is an identifier
    islower()	    Returns True if all characters in the string are lower case
    isnumeric()	    Returns True if all characters in the string are numeric
    isprintable()	Returns True if all characters in the string are printable
    isspace()	    Returns True if all characters in the string are whitespaces
    istitle()	    Returns True if the string follows the rules of a title
    isupper()	    Returns True if all characters in the string are upper case
    join()	        Joins the elements of an iterable to the end of the string
    ljust()	        Returns a left justified version of the string
    lower()	        Converts a string into lower case
    lstrip()	    Returns a left trim version of the string
    maketrans()	    Returns a translation table to be used in translations
    partition()	    Returns a tuple where the string is parted into three parts
    replace()	    Returns a string where a specified value is replaced with a specified value
    rfind()	        Searches the string for a specified value and returns the last position of where it was found
    rindex()	    Searches the string for a specified value and returns the last position of where it was found
    rjust()	        Returns a right justified version of the string
    rpartition()	Returns a tuple where the string is parted into three parts
    rsplit()	    Splits the string at the specified separator, and returns a list
    rstrip()	    Returns a right trim version of the string
    split()	        Splits the string at the specified separator, and returns a list
    splitlines()	Splits the string at line breaks and returns a list
    startswith()	Returns true if the string starts with the specified value
    strip()	        Returns a trimmed version of the string
    swapcase()	    Swaps cases, lower case becomes upper case and vice versa
    title()	        Converts the first character of each word to upper case
    translate()	    Returns a translated string
    upper()	        Converts a string into upper case
    zfill()	        Fills the string with a specified number of 0 values at the beginning