# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has requested the follwowing audit of a recent local congressional election, including the total votes cast, the nummber and percentage of votes broken down by county, and the number and percentage of votes cast for each candidate.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.66.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockhamm
    - Diana DeGette
    - Raymon Anthony Doane
- The  candidate results were:
    - Charles Casper Stockham recieved 23.0% of the vote and 85,213 total votes.
    - Diana DeGette recieved 73.8% of the vote and 272,892 total votes.
    - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 total votes.
- The winner of the election was:
    - Diana DeGette, who recieved 72.8% of the vote and 272,892 total votes.
- The largest number of votes were cast(82.8%) by residents of Denver.
[Full analysis results here.](/analysis/election_analysis.txt)]

## Challenge Summary
This script has been written in a way to be reusable for any election with minimal modifications. Another csv file can be 
substituted for the one used here which will require minor code adjustments to work assuming the file has not been given 
the exact same name. Similar small modifications could be made to change the output for state elections.
