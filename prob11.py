# Problem 11

import sys

currentline = ''
prevline = ''

try:
    with open('input11.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        # Ignore the "0 0" line to end the processing
        if line.strip() == "0 0":
            break
        
        currentline = line.strip()  # Remove any leading/trailing whitespace
        #print(f'Current line: {currentline}')
        
        # Split the current line into seconds and nanoseconds
        spaceIndex = currentline.find(" ")
        curr_secs = int(currentline[:spaceIndex])  # Convert to int
        curr_nanoSecs = int(currentline[(spaceIndex + 1):])  # Convert to int
        
        if prevline != '':  # If there was a previous timestamp
            #print(f'Previous line: {prevline}')
            
            # Split the previous line into seconds and nanoseconds
            prevSpaceIndex = prevline.find(" ")
            prev_secs = int(prevline[:prevSpaceIndex])  # Convert to int
            prev_nanoSecs = int(prevline[(prevSpaceIndex + 1):])  # Convert to int
            
            # Calculate the difference in seconds and nanoseconds
            sec_diff = curr_secs - prev_secs
            nanoSec_diff = curr_nanoSecs - prev_nanoSecs
            
            if nanoSec_diff < 0:
                sec_diff -= 1
                nanoSec_diff += 1000000000  # Add one second worth of nanoseconds
            
            # Convert the time difference to full milliseconds (truncate any fractions)
            total_millisecs = (sec_diff * 1000) + (nanoSec_diff // 1000000)
            print(total_millisecs)
        
        # Update prevline to currentline for the next iteration
        prevline = currentline
        
except Exception as e:
    print("Error reading file")
    print(f"The error is {e}")
