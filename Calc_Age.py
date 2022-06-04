###################################################################
#                        Import Module
from termcolor import *
from time import sleep
from colored import fg, attr
###################################################################
###################################################################
#                       Static Variables & Colors
author = "Abdallah Mamdouh"
star   = "*" * 30

bk = 0; rd = 1; gr = 2; yw = 3; bu = 20; cy = 6; w = 15; 
###################################################################

print(f"%s {star} %s".center(40)  % (fg(rd), attr(0)))
print(f"Scripting By %s{author}%s".center(40) % (fg(rd), attr(0)))
print(f"%s {star} %s".center(40)  % (fg(rd), attr(0)))

age = int(input("what\'s your age ?"))

month   = age * 12
weeks   = month * 4
days    = weeks * 365
hours   = days * 24
minutes = days * 60
seconds = minutes * 60

print(
    ''' 
    [1] Months
    [2] Weeks
    [3] Days
    [4] Hours
    [5] Minutes
    [6] Seconds
    [7] All
    '''
)
print(f"%s ==> select Number for print util%s"  % (fg(yw), attr(0)))

number = input()
number.strip()

if number == '1':
    print(f"your lived For: %s {month}   %s Month."   % (fg(gr), attr(0))) 
elif number == '2':
    print(f"your lived For: %s {weeks}   %s Week."    % (fg(gr), attr(0))) 
elif number == '3':
    print(f"your lived For: %s {days}    %S Day."     % (fg(gr), attr(0)))
elif number == '4':
    print(f"your lived For: %s {hours}   %s Hour."    % (fg(gr), attr(0)))  
elif number == '5':
    print(f"your lived For: %s {minutes} %s Minutes." % (fg(gr), attr(0)))
elif number == '6':
    print(f"your lived For: %s {seconds} %s Second."  % (fg(gr), attr(0)))  
elif number == '7':
    print(f"your lived For: %s {month}   %s Month."   % (fg(gr), attr(0)))
    print(f"your lived For: %s {weeks}   %s Week."    % (fg(gr), attr(0)))
    print(f"your lived For: %s {days}    %s Day."     % (fg(gr), attr(0)))
    print(f"your lived For: %s {hours}   %s Hours."   % (fg(gr), attr(0)))
    print(f"your lived For: %s {minutes} %s Minutes." % (fg(gr), attr(0)))
    print(f"your lived For: %s {seconds} %s Second."  % (fg(gr), attr(0)))


sleep(3)