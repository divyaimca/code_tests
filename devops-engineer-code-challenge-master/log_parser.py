"""This script reads logfile and prsent below information to the user

    - What are the number of requests served by day?
    - What are the 3 most frequent User Agents by day?
    - What is the ratio of GET's to POST's by day?
"""
__author__ = 'Priyadarshee D Kumar'
__version__ = '0.1'

import argparse
import re
from collections import Counter


def number_of_requests(logs, day):
    """This function will read the logfile and date as input, count the number of requests for the date"""
    count = 0
    for line in logs:
        if day in line:
            count += 1

    return count

###

def most_frequent_user_agents(logs, day):
    """This function will find all the User Agents on a day, Sort the count of Agents and return the 3 most frequent User Agents"""

    all_agents = []
    for line in logs:
        if day in line:
            agent_found = re.split(" ", line)[11].strip(';')
            all_agents.append(agent_found.strip('"'))

    sorted_agents = Counter(all_agents).most_common()
    top_3_agents = [agent[0] for agent in sorted_agents[0:3]]

    return top_3_agents


###

def get_post_ratio(logs, day):
    """This function will read logs, find the GETs and POSTs for a date and return the ratio in %"""

    get_count = post_count = 0
    for line in logs:
        if day in line:
            if "GET" in line:
                get_count += 1
            elif "POST" in line:
                post_count += 1
    try:
        ratio = f"{round(((get_count / post_count) * 100),2)}%"        
        return ratio
    except ZeroDivisionError as err:
        return f"ZeroDivisionError {err}"


###

def read_log_file(log_file):
    """This function will validate the log file prsence, read the log file, return the validation and log entries
    """
    try:
        with open(log_file, 'r') as logs:
            log_entries = logs.readlines()
            return([True, log_entries])
    except FileNotFoundError as err1:
        return([False, err1])
    except IOError as err2:
        return([False, err2])
             
###

def valid_day(date):
    """This regex pattern matching a valid date in format :  dd/Mmm/yyyy, 03/Dec/2022"""

    validate_day = re.compile("^(([1-9])|([0-2][0-9])|([3][0-1]))\/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\/\d{4}$")
    try:
        if validate_day.match(date):
            return True
        else:
            return False
    except TypeError as err:
        return False

###   
  
def usage():
    print(""" 
##############################################################################################################
Usage : log_parser.py [-h] --logFile LOGFILE --date DATE [--action ACTION] 

        optional arguments:
            -h, --help         show this help message and exit
            --logFile LOGFILE  input log file path to be processed
            --date DATE        log day e.g. 03/Dec/2011, 01/Dec/2011
            --action ACTION    all(default) / number_of_requests / get_post_ratio / most_frequent_user_agents
            

Assumptions : 
    1. Log file should be in this format :
        127.0.0.1 - - [01/Dec/2011:00:00:30 -0500] "GET /robots.txt HTTP/1.0" 200 333 "-" "Mozilla/5.0 (compatible; ScoutJet; +http://www.scoutjet.com/)"
    2. User Agent should exist in 12th column
    3. Used python 3.7+
    4. Logfile structure (It can read any number of log files in a directory recursively)
    5. Pass a valid date in format : dd/Mmm/yyyy  , e.g. 03/Dec/2021 
    6. Ratio is presented in %
    7. Logfiles should be with .log extension
    
        Example
        ├── sample.log
        ├── log_parser.py
        └── test_coverae.py
        

    Example : python3 log_parser.py --logFile sample.log --date 03/Dec/2011 [--action all]       
################################################################################################################        
    """)

###

def main(log_file, day, action):
    """
    This section parse Command Line Arguments, take input of log_file, date, action(all(default) / number_of_requests / get_post_ratio / most_frequent_user_agents) and pass them to functions
    """
    logs = read_log_file(log_file)
    valid_log = logs[0]
    
    if valid_day(day):
        if valid_log:
            user_agents = most_frequent_user_agents(logs[1], day)
            ratio = get_post_ratio(logs[1], day)
            requests = number_of_requests(logs[1], day)
            if not action or action == "all":
                print(f"Total Number of requests served on day {day} : {requests} \n")
                print(f"3 most frequent User Agents on day {day} : {user_agents} \n")
                print(f"Ratio of GET's to POST's on day {day} : {ratio} \n")
                return(user_agents, ratio, requests)
            elif action == "number_of_requests":
                print(f"Total Number of requests served on day {day} : {requests} \n")
                return requests
            elif action == "get_post_ratio":
                print(f"Ratio of GET's to POST's on day {day} : {ratio} \n")
                return ratio
            elif action == "most_frequent_user_agents":
                print(f"3 most frequent User Agents on day {day} : {user_agents} \n")
                return user_agents
        else:
            print(f"Please provide a valid logfile : {logs[1]}")        
    else:
        print(f"{day} : Invalid date")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--logFile', type=str, required=True, help='input log file path to be processed')
    parser.add_argument('--date', type=str, required=True, help='log day e.g. 03/Dec/2011, 01/Dec/2011')
    parser.add_argument('--action', type=str, required=False, help='all(default) / number_of_requests / get_post_ratio / most_frequent_user_agents')
    args = parser.parse_args()

    usage()
    main(args.logFile, args.date, args.action)



