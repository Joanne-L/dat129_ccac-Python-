# -*- coding: utf-8 -*-\
# Personal Project
# Python 2
# Joanne

# This program will be used to track they type and duration of  interuptions during work.

# The user press s to begin which logs the date and time. Each time there is 
# a distraction the user will press a letter corresponding to the identity of
# interruption i for instant message v for visitor p for phone call or e for
# email t for text, m for meeting and b for break.  The date and time of the 
# interruption is logged and the system waits for the user to press f to finish
# the interruption and the date and time are again logged.  The user may press
# q to quit logging at the end of the day.  The stop date and time is logged 
# and the program is ended. All data is written to a csv file.

#import module dateime and csv
import datetime
import csv

# Begin data collection
def GatherInput1():
    # Open File Used to Print Messages for Gather Input Function
    with open ('Msg_GIF1.txt') as GIF1:
       GIF1 = GIF1.read()
    Key = input(GIF1)
    Valid1 = ['s','S']
    # Validate Entry
    while Key not in Valid1:
        # Print Error Message from file indicating the correct key press required
        with open ('Msg_GIF2.txt') as GIF2:
            GIF2 = GIF2.read()
        raise TypeError(GIF2)
    # Create Date Time 
    DT = datetime.datetime.now()
    # Create Entry List
    Entry = [Key, DT] 
    # Open File to Write .csv
    with open('file.csv', 'a', newline = '\n') as csvfile:
        # creating a csv sriter object
        csvwriter = csv.writer(csvfile)
        # Write to the File
        csvwriter.writerow(Entry)
        # Close the File
        csvfile.close()
    # Return Entry to main
    return Entry

def LogInterruptions():
    # Print Instruction Message and Gather Input
    with open ('Msg_LIF1.txt') as LIF1:
       LIF1 = LIF1.read()
    Key = input(LIF1)
    # Create Entry Validation Lists
    Valid1 = ['e','E','t','T','p','P','v','V','b','B','m','M','i','I','q','Q']
    Valid2 = ['q','Q']
    #Process Entry and contineu on if Entry is not found in Valid2
    while Key not in Valid2:
        # Process Entry and continue on if Entry is not found in Valid1
        if Key not in Valid1: 
            # Print Error Message from File for invalid entry
            with open ('Msg_LIF2.txt') as LIF2:
                LIF2 = LIF2.read()
                Key = input(LIF2)
        # If Entry was valid and found in Valid1 begin logging       
        elif Key in Valid1:
            # Create Date Time 
            DT = datetime.datetime.now()
            # Create Entry List
            Entry = [Key, DT] 
            # Open File to Write .csv        
            with open('file.csv', 'a', newline = '\n') as csvfile:
                    # creating a csv sriter object
                    csvwriter = csv.writer(csvfile)
                    # Write to the File
                    csvwriter.writerow(Entry)
                    # Print the log msg from file and print Entry
                    with open ('Msg_LIF3.txt') as LIF3:
                        LIF3 = LIF3.read()
                    print(LIF3)
                    print(Entry)
                    # Close the csv file
                    csvfile.close()
            # Print waiting for entry message       
            with open ('Msg_LIF3.txt') as LIF4:
                LIF4 = LIF4.read()
                print(LIF4)
            # Validate entry     
            Key = input()
            Valid3 = ['f','F']
            while Key not in Valid3:
                print(LIF4)
                Key = input()
            else: 
                Key in Valid3
                # Create Date Time 
                DT = datetime.datetime.now()
                # Create Entry List
                Entry = [Key, DT] 
                # Open File to Write .csv        
                with open('file.csv', 'a', newline = '\n') as csvfile:
                    # creating a csv sriter object
                    csvwriter = csv.writer(csvfile)
                    # Write to the File
                    csvwriter.writerow(Entry)
                    # Print the log info
                    with open ('Msg_LIF3.txt') as LIF5:
                        LIF5 = LIF5.read()
                    print(LIF5)
                    print(Entry)
                    # Close the csv file
                    csvfile.close()
                    Key = input(LIF1)
    # If q is entered end the loop
    else: 
        Valid4 = ['q','Q']
        Key in Valid4
        # Complete final logging    
        # Create Date Time 
        DT = datetime.datetime.now()
        # Create Entry List
        Entry = [Key, DT] 
        # Open File to Write .csv        
        with open('file.csv', 'a', newline = '\n') as csvfile:
                # creating a csv sriter object
                csvwriter = csv.writer(csvfile)
                # Write to the File
                csvwriter.writerow(Entry)
                # Close the csv file
                csvfile.close()
                # Create Return Variable to pass to main
                Process = Entry   
        return Process

# Use main to begin and end program
def main():
    Entry = GatherInput1()
    print(f"The Start Time has been logged:\n{Entry}")
    Process = LogInterruptions()
    print(f"Logging has been terminated:\n{Process}")
main()


     



                                                          
