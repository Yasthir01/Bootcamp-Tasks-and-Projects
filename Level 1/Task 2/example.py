# ========= Basic Concept of Programming =========
# Programmers write statements of code to create 'programs', which are runnable files that do something.
# Code can be written in different programming LANGUAGES, such as, Python, Java and C++.
# This course is in the programming language Python.
# After writing Python commands or code we save them in a Python file.
# A Python file has the following file naming format:
#   filename.py (where filename can be any valid filename and .py is the file extension in Windows).
# You can then 'run' the Python file.
# The Python program you have written is executed and displays the outcomes that may result based on what the code statements say.
# Information about how to 'run' Python files are given later in this file.
# We will now show you how to write some basic code in Python, and perform some basic operations.


# ========= Reading Python code ========= 
# You're actually reading a Python program right now.
# Comments in Python appear in GREEN if you have the file opened in Notepad++ and RED if you have it opened in IDLE.
# Keywords of the Python language appear in BLUE in Notepad++ and ORANGE in IDLE. 
# Most other programming languages have the same structure as Python, so if you learn Python, you can learn the others more easily! It's not like learning human languages.
# Almost all programming languages share common SYNTAX.
# Syntax is the "spelling and grammar rules" of a programming language and determines how you write correct, well formed statements.
 
 
#  =========  The print function ========= 
# You may want your program to display or output information to the user.
# The most common way to view program output is to use the print function.
# To use print, we enter the print command followed by one or more arguments.
# In programming, a command is an instruction given by a user telling a computer to do something, while the arguments can be thought of as the value that you want the command to act on.
# Together a command and an argument are known as a statement. 
 
# ************ Example 1 ************
print ("Hello, World!")
# When you run this program the computer will output the argument Hello, World!
# Note that the argument is enclosed in double quotes ("...")
# This is because "Hello, World!" is a string or list of characters.
 
# ************ Example 2 ************
print ("Printing a string.") 
 
# A common SYNTAX error you could make above is by forgetting to add a closing ".
# Remember that all opening quotation marks (") require a closing one!
 
 
# ========= How to Get Input ========= 
# Sometimes you want a user to enter something through the keyboard.
# The following input command will show the text "Enter your name" in the output box of the program and the program will halt
# until the user enters something with their keyboard and presses ENTER.
 
# ************ Example 3 ************
# The following input commands will get the user's name and age. 
 
name = input("Enter your name: ") 
age = input("Enter your age: ")
 
# The variable 'name' stores what the user entered into the box as a String.
# The variable 'age' also stores what the user entered into the box as a String.
# Now, when you try running this file, notice the output produced by the following command.
print (name, age)
 
# A common SYNTAX error you could make above is by forgetting to add a closing ‘)’.
# Remember that all opening brackets ‘(’ , require a matching closing one!
 
 
#  ========= Running Python files ========= 
# Now that you know how to write code, it's time to learn how to execute your code to see what the output is.
# Remember you're actually reading a Python file now. All the Python commands are the statements not seen in GREEN.
# Let's 'RUN' this Python file and take a look at what output it produces (if any).
# When you write Python code, you'll have to run it often to test that your programs are doing what you'd like them to do.
 
# There are different ways to 'run' Python files.
 
#  ========= OPTION 1: Run from IDLE Python GUI (THE EASY WAY) ========= 
# The easiest way to run Python files and this program is through a GUI (Graphical User Interface). 
# Please follow these steps to run this program:
 
# Simply go to the Windows Start Button at the bottom left corner of your screen and enter 'IDLE' into your windows search ('Search for programs and files' box).
# The program 'IDLE (Python GUI)' should appear in the search box. Click on it to open it.
# If you can't find the IDLE program on your computer - you didn't install Python correctly. Contact your mentor for assistance.
# Go to the top left corner of this program (it looks like a white box when open) and click --> File -- Open--> navigate to your Dropbox folder, open the relevant task folder, and open example.py.
# Now your code will open in the Python GUI IDLE. Press F5 on your keyboard to RUN the Python file and the output will appear in a separate Python output (Python Shell) window!
# You can use this method to run ANY Python file (file with a .py extension). 
# If there is an error in your code, the code won't run and the error will be printed out in the Python Shell window.
# Another way to run Python files is to simply right click on this file (example.py) and select 'Open in IDLE'. You may or may not see this option.
 
# Errors are things like trying to add two variables that aren't the same data type, or using a variable that isn't declared! 
# (i.e. if you say num = num1+num2 and you haven't said what num1 and num2 above this statement!)
# We'll talk about errors more later.
 
# Let's put a line just below this comment that will print out the words 'Yay! You ran your first Python program!' when the file example.py is run using IDLE.
 
print ("Yay! You ran your first Python program!")
 
# Now when you follow the instructions above and open example.py in the IDLE program and hit F5. 
# You should see "Yay! You ran your first Python program!" printed out in the Python Shell window!
# Whatever appears in the Shell window after running a program is known as the OUTPUT of a program.
# All the code above that aren't comments also ran, but just storing and declaring variables doesn't produce any output. 
# The Python Shell only shows the output of the program.
# Play around with this program. Change statements and delete things, run the code and see what happens.
 
# We advise that you complete all tasks and open all example files in IDLE from now on.
# Perhaps create a shortcut to IDLE on your desktop so that you can access it faster.
# You can also use Notepad++ to view the example.py files, but Notepad++ can only be used to view the text of a code. You can't run programs from within Notepad++.
 
 
#  ========= OPTION 2: Use any GUI/IDE that you want (ADVANCED) ========= 
# An IDE is a program like the IDLE Python GUI.
# You get many programs that let you run code within them.
# Some of these IDEs are more complicated than others.
# See http://wiki.python.org/moin/PythonEditors for a huge list of your options of different IDEs that you can run Python files from.
# The other option is OPTIONAL. As long as you know how to use IDLE, you can complete our entire course.
 
 
 
# =========== Errors When Running Python Files ===========
# Now that you've learnt how to run a Python file, you should know about errors.
# There are different types of errors, and as a programmer you'll be sure to run into many.
# The process of resolving errors in code is known as 'debugging'.
# This comes from the history of computers, when they were as large as rooms - bugs used to fly into the electronics of computers causing them to fail.
# Hence the term 'debugging' used to mean to literally remove bugs from computer hardware to fix issues.
 
# Any program you write must be EXACTLY correct. 
# All code is CASE SENSITIVE. This means that Print is not the same as print.
# If you enter an invalid Python command, misspell a command or misplace a punctuation mark, you will get a SYNTAX error when trying to run your Python program.
# Syntax in programming is the way things are written, i.e., where spaces go, punctuation goes, and spelling.
# Errors appear in the Python shell when you try run a program and it fails.
# Be sure to read all errors carefully to discover what the problem is.
# Error reports in the Python shell will even tell you what line of your program had an error.
# In Notepad++ the line number is in the left margin.
# Use the line numbers shown in Notepad++ to check that line of your code for an error.
 
 
 
# ****************** END OF EXAMPLE CODE ********************* # 
 
 
# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task. ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it. ===
 