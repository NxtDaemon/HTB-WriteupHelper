from Writer import log
import time 
import progressbar 

try:
    ToWrite = list(input("Enter all the IDs to generate writeups for > "))
    log.info(f"Generating Writeups for the following IDs {ToWrite}")
    for item in ToWrite:


