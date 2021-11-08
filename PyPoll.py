# Data we need to Retrieve 

#import dependecies
import csv
import os

#assign a variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")


#assign a variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Total number of votes cast

#1 initialize a total vote counter and declare a list of candidate options

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0 
winning_percentage = 0

#open and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    for row in file_reader:
        #2 add to the total vote count
        total_votes += 1

# A complete list of candidates who received votes

#1 print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

  

# Total number of votes each candidate received

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    



    # Percentage of votes each candidate won


    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #4b format the percentage to 2 decimal places
        format_float_percentage = "{:.2f}".format(vote_percentage)

        # variable for candidate results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


        # print and send to our txt file   
        print(candidate_results)
       
        txt_file.write(candidate_results)

   




    # The winner of the election based on popular vote

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    

    #print summary
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)



  




