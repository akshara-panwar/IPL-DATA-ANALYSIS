# IPL Match Data Analysis Project
# This project is about analyzing IPL match data using Python.
# I explored different match insights like team wins,
# toss impact, venues, and player performances.
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_csv(r'C:\Users\Akshara\Downloads\Match_Info.csv')
# Display the first 10 rows of the dataset
print(data.head(10))
#check for missing values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())
# Team Performance Analysis
# combine both team columns to calculate total matches played
all_teams = pd.concat([data['team1'], data['team2']])
# count total matches played by each team
team_performance = all_teams.value_counts().head(10)
print("Team Performance Analysis:")
print(team_performance)
# Plotting the team performance
plt.figure(figsize=(10, 6))
team_performance.plot(kind='bar', color='skyblue')
plt.title('Team Performance Analysis')
plt.xlabel('Teams')
plt.ylabel('Number of Matches')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('01_team_performance.png')
plt.show()
#Finding The Most Successful Team
most_successful_team = data['winner'].value_counts().idxmax()
print("\nMost Successful Team:", most_successful_team)
#Win Comparison Between Teams
win_counts = data['winner'].value_counts().head(10)
print("\nWin Comparison Between Teams:")
print(win_counts)
# Plotting the win comparison between teams
plt.figure(figsize=(10, 6))
win_counts.plot(kind='bar', color='orange')
plt.title('Win Comparison Between Teams')
plt.xlabel('Teams')
plt.ylabel('Number of Wins')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('02_win_comparison.png')
plt.show()
print("Winner of the most matches:", most_successful_team)
#Toss Analysis
toss_winner_counts = data['toss_winner'].value_counts().head(10)
print("\nToss Analysis:")
print(toss_winner_counts)
# Plotting the toss analysis
plt.figure(figsize=(10, 6))
toss_winner_counts.plot(kind='bar', color='purple')
plt.title('Toss Analysis')
plt.xlabel('Teams')
plt.ylabel('Number of Toss Wins')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('03_toss_analysis.png')
plt.show()
#Toss Winner vs Match Winner Analysis
toss_winner_vs_match_winner = data.groupby(['toss_winner', 'winner']).size().unstack(fill_value=0)
print("\nToss Winner vs Match Winner Analysis:")
print(toss_winner_vs_match_winner)
# Plotting the toss winner vs match winner analysis
toss_winner_vs_match_winner.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Toss Winner vs Match Winner Analysis')
plt.xlabel('Toss Winner')
plt.ylabel('Number of Matches')
plt.xticks(rotation=90)
plt.legend(title='Match Winner', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('04_toss_vs_match_winner.png')
plt.show()
#Bat First vs Chase First Analysis
bat_first = data[data['toss_decision'] == 'bat']
chase_first = data[data['toss_decision'] == 'field']
print("\nBat First vs Chase First Analysis:")
print("Matches where teams batted first:", len(bat_first))
print("Matches where teams chased first:", len(chase_first))
# Plotting the Bat First vs Chase First Analysis
labels = ['Batting', 'Chasing']
sizes = [len(bat_first), len(chase_first)]
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
plt.title('Bat First vs Chase First Analysis')
plt.axis('equal')
plt.savefig('05_bat_vs_chase.png')
plt.show()
#Venue Analysis
venue_counts = data['venue'].value_counts().head(10)
print("\nTop 10 Venues:")
print(venue_counts)
# Plotting the top 10 venues
plt.figure(figsize=(10, 6))
venue_counts.plot(kind='bar', color='green')
plt.title('Top 10 Venues')
plt.xlabel('Venues')
plt.ylabel('Number of Matches')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('06_venue_analysis.png')
plt.show()
#Matches Played In Different Stadiums
stadium_counts = data['venue'].value_counts().head(10)
print("\nMatches Played in Different Stadiums:")
print(stadium_counts)
#High Frequency Venues
high_freq_venues = data['venue'].value_counts().head(10)
print("\nHigh Frequency Venues:")
print(high_freq_venues)
#Player Analysis
player_counts = data['player_of_match'].value_counts().head(10)
print("\nTop 10 Players of the Match:")
print(player_counts)
# Plotting the top 10 players of the match
plt.figure(figsize=(10, 6))
player_counts.plot(kind='bar', color='red')
plt.title('Top 10 Players of the Match')
plt.xlabel('Players')
plt.ylabel('Number of Awards')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('08_top_players.png')
plt.show()
#Match Trends
data['date'] = pd.to_datetime(data['match_date'])
data['year'] = data['date'].dt.year
matches_per_year = data['year'].value_counts().sort_index().head(10)
print("\nMatches Per Year:")
print(matches_per_year)
# Plotting matches per year
plt.figure(figsize=(10, 6))
matches_per_year.plot(kind='line', marker='o', color='blue')
plt.title('Matches Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Matches')
plt.xticks(matches_per_year.index)
plt.grid()
plt.tight_layout()
plt.savefig('07_matches_per_year.png')
plt.show()
# Winning Pattern Analysis 
winning_pattern = data.groupby(['year', 'winner']).size().unstack(fill_value=0)
print("\nWinning Pattern Analysis:")
print(winning_pattern)





