#Impot necessary modules 

from error_observer import ErrorObserver
from warning_observer import WarningObserver
from user_activity_observer import UserActivityObserver
from log_analyzer import LogAnalyzer
import argparse 

#Main function to set up log analysis and observers

def main():

    parser = argparse.ArgumentParser() 
    parser.add_argument("-i", "--input", required = True, help = "Path to the log file to analyze")
    parser.add_argument("-n", type= int, default = 0, help = "Number of lines to analyze from the log file. Default is 0 (analyze all lines).")
    parser.add_argument("--acc", type = float, default = 1.0, help = "Time acceleration factor." )

    with open("logs.txt", "r") as file :
        lines = file.readlines()
    
    log_analyzer = LogAnalyzer(lines)
    error_observer = ErrorObserver()
    warning_observer = WarningObserver()
    user_activity_observer = UserActivityObserver() 