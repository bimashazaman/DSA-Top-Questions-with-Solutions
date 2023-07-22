# Validate Subsequence • §
# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

# A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4] . Note that a single number in an array and the array itself are both valid subsequences of the array.


def tournamentWinner(competitions, results):
    # Initializing a dictionary to store the teams' scores
    scores = {}
    
    # Initializing a variable to store the current best team
    current_best_team = ''
    
    # Iterating over the competitions using enumerate to get both index and value
    for idx, teams in enumerate(competitions):
        
        # Extracting the result of the current match from the results list
        result = results[idx]
        
        # If the result is 0, the away team won, otherwise the home team won
        winning_team = teams[1] if result == 0 else teams[0]
        
        # If the winning team is not already in the scores dictionary, initialize their score as 0
        if winning_team not in scores:
            scores[winning_team] = 0
        
        # Adding 3 points to the winning team's score
        scores[winning_team] += 3
        
        # Checking if the winning team's score is greater than the current best team's score
        # If it is, updating the current best team
        if scores[winning_team] > scores.get(current_best_team, 0):
            current_best_team = winning_team
            
    # Returning the team with the highest score
    return current_best_team




def tournamentWinner2(competitions, results):
    
    # Initialize a dictionary to store team scores.
    scores = {}

    # Iterate over the list of competitions.
    for i in range(len(competitions)):
        # Determine the winner of the competition.
        winner = competitions[i][0] if results[i] == 1 else competitions[i][1]
        
        # Update the score of the winning team.
        if winner in scores:
            scores[winner] += 3
        else:
            scores[winner] = 3

    # Determine and return the team with the maximum score.
    return max(scores, key=scores.get)



def tournamentWinner3(competitions, results):
    # Write your code here.
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == 1 else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points

# O(n) time | O(k) space - where n is the number of competitions and k is the number of teams


def tournamentWinner5(competitions, results):
    # Initialize an empty dictionary to store team scores.
    scores = {}

    # Iterate over competitions, update scores, find max scoring team in one line.
    return max((scores.update({teams[results[i]^1]: scores.get(teams[results[i]^1], 0) + 3}) or teams[results[i]^1] for i, teams in enumerate(competitions)), key=scores.get)

