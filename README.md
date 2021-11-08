# Election-Analysis
 
 Utilizing knowledge of Python functions and logistics to garner specific results for an election audit.



## Overview of Project

The overall purpose of the project was to hone our skills in Python by supplying the desired information about a Colorado election audit for Colorado Board of Elections employees "Seth" and "Tom".  Utilizing a .csv file given to us about voter information in the election, we made use of "for loops" and "conditional statements", along with other advanced syntax, to present specific information about a local election audit.  Specifically, we were taxed with writing a Python script that, when executed, would give us a neat wall of text describing voter turnout per county and which candidate in the election recieved the greatest number of votes along with general information about most of the basic variables involved in the audit.

## Election Audit Results

### Election Results by Participating Counties

In the entire election 369,711 total votes were cast throughout the 3 counties that participated.  Of the three counties (Denver, Arapahoe, and Jefferson), Denver should have been estimated to create the greatest portion of the pot considering it is, to my knowledge, the only metropolitan area included.  With 306,055 total votes cast in the Denver county it indeed was the heavy majority, making up roughly 82.8% of the total votes cast with Jefferson coming in at second with 10.5% (38,855 votes) and Arapahoe as the smallest contributor at 6.7% (24,801 votes).    

### Election Results by Political Candidate

There was a similarly sized spread of votes based on the Candidate chosen as well which perhaps correlates to county favoritism for specific politicians.  Diana DeGette was the winning candidate at a whopping 272,892 votes or 73.8% of the total with Charles Casper Stockham at 2nd with 85,213 votes (23.0% of total) and Raymon Anthony Doane in last place at a meager 11,606 votes or just 3.1% of the total count in their favor.  Considering Diana was a landslide win and Denver had the most votes cast it can safely be assumed that a majority of Denver voted for Diana even if the entire two other counties combined had a 100% voting rate in her favor!




## Summary

The script used to get this information could be used on any number of elections!  The first step would be to have csv files that we can load information from i.e. raw data about voters that is otherwise too lengthy to interpret.  The code below allowed us to supplement our script with information from that file making it simple to present specific details:

```

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

```
By first importing a csv dependency, we can easily pull data from just about any spreadsheet on any election given we replace the election_results.csv with the relevant data pool.  We could then tweak the script in subtle ways to account for any differences in the type of election like if the regional variables weren't county but rather city, state, or even region!

```
county_options = []
county_votes = {}

```
The county portion of the variables created could be made to represent any sort of area that is needed for one's presented information about the election.  A simple yet exceedingly important piece of code, shown below, would need to be changed if the order of the columns in the original data was presented differently than how it was in our csv file: Ballot ID, "Location/County", Candidate. 

```
# Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
        
```

Since we had referenced the candidate and county based on their index position per Python Syntax, if the orders were in anyway different for the new election data than the corresponding number would have to change with [0] being first in left to right format so then 1, 2, 3 accordingly.  For example, if there was a data set in which State (voter location) was the 3rd row after ballot ID or Candidate (or another variable introduced) then extracting the State name from each row would read something like,
```
State_name = row[2]

```

However, given the sheer size of data pools that can be appointed to election results these minor tweaks seem miniscule in the face of a script that can easily execute information about a desired variable in almost an instant!  Using the script I have created, given the necessary minor adjustments, it would be wise to appropriate it to fit a slew of different kind of election data tables for the quickest and most-pain free experience on the market!
