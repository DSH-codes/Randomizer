


PROJECT TITLE:
Random - IT


DESCRIPTION:
Windows desktop application for generating random numbers within a defined range and quantity. It features a simple 
Tkinter UI with entry validation to accept only digits, using the regex module. The application displays random digits 
on the screen and, if needed, saves every generated result in an overall log. Users can define a personal log, and the 
default logs are located in C:\Users\Documents. Logs can be erased or deleted manually from the folder.  

USAGE:
Set the lower and upper ranges, ensuring that the lower value is less than the upper value. Specify the desired quantity,
with a maximum limit of 999, and press the "Twist the Wheel" button. If a large number of results is generated, they 
will be displayed in a pop-up window. Use the "Only with Digit" or "Remove with Digit" filters to refine your results, 
and be cautious to avoid logical conflicts when using these filters. Additional help can be found by clicking the "?" 
button in the UI. If you want to set an upper limit greater than 999, change the argument at line 272 of the script.

P.S. A compact version (lite) is included.


INFO:
Made by Said Datsaev 
in January 2023
GitHub: DSH-codes 
