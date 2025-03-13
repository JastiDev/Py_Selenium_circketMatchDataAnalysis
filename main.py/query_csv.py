import sqlite3
import pandas as pd
import os

# Define the output folder
output_folder = "D:\\Cricket_DA_Pro\\Query_Results\\"  

# Ensure the output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # Create directory if it doesn't exist

# Verify the directory before proceeding
if not os.path.isdir(output_folder):
    print(f"❌ Error: Directory '{output_folder}' does not exist!")
    exit()
# Load datasets
ODI_Matches = pd.read_csv("D:\\Cricket_DA_Pro\\ODI_Match.csv")
T20_Matches = pd.read_csv("D:\\Cricket_DA_Pro\\T20_Match.csv")
Test_Matches = pd.read_csv("D:\\Cricket_DA_Pro\\Test_Match.csv")

# Create SQLite Database
conn = sqlite3.connect("cricket_analysis.db")
cursor = conn.cursor()

# Load data into SQL tables
ODI_Matches.to_sql("ODI_Matches", conn, if_exists="replace", index=False)
T20_Matches.to_sql("T20_Matches", conn, if_exists="replace", index=False)
Test_Matches.to_sql("Test_Matches", conn, if_exists="replace", index=False)

# Define SQL Queries for each match type
match_types = {
    "ODI_Matches": "ODI",
    "T20_Matches": "T20",
    "Test_Matches": "Test"
}

queries = {
    "Total Matches Played by Each Team": """
        SELECT team_1 AS team, COUNT(*) AS total_matches FROM {table} GROUP BY team_1
        UNION
        SELECT team_2 AS team, COUNT(*) AS total_matches FROM {table} GROUP BY team_2
        ORDER BY total_matches DESC;
    """,
    "Match Outcomes - Team with Most Wins": "SELECT match_winner, COUNT(*) AS matches_won FROM {table} WHERE match_winner IS NOT NULL GROUP BY match_winner ORDER BY matches_won DESC;",
    "Toss Decision Trends": "SELECT toss_decision, COUNT(*) AS count FROM {table} GROUP BY toss_decision;",
    "Venue with Most Matches": "SELECT venue, COUNT(*) AS matches_played FROM {table} GROUP BY venue ORDER BY matches_played DESC LIMIT 5;",
    "Effect of Toss on Match Winner": "SELECT toss_winner, COUNT(*) AS matches_won_as_toss_winner FROM {table} WHERE toss_winner = match_winner GROUP BY toss_winner ORDER BY matches_won_as_toss_winner DESC;",
    "Average Runs Per Match for Each Team": "SELECT batting_team, ROUND(AVG(total_runs), 2) AS avg_runs FROM {table} GROUP BY batting_team ORDER BY avg_runs DESC;",
    "Highest Team Total in an Innings": "SELECT batting_team, SUM(total_runs) AS highest_score FROM {table} GROUP BY match_id, batting_team ORDER BY highest_score DESC LIMIT 1;",
    "Best Chasing Teams": "SELECT match_winner, COUNT(*) AS successful_chases FROM {table} WHERE match_winner != batting_team GROUP BY match_winner ORDER BY successful_chases DESC;",
    "Teams with Most Powerplay Runs": "SELECT batting_team, SUM(total_runs) AS powerplay_runs FROM ODI_Matches WHERE powerplay = 1 GROUP BY batting_team ORDER BY powerplay_runs DESC LIMIT 5;",
    "Teams with Best Death Over Performance": "SELECT batting_team, SUM(total_runs) AS death_over_runs FROM {table} WHERE over_number BETWEEN 16 AND 20 GROUP BY batting_team ORDER BY death_over_runs DESC LIMIT 5;",
    "Top 5 Run Scorers": "SELECT batter, SUM(runs) AS total_runs FROM {table} GROUP BY batter ORDER BY total_runs DESC LIMIT 5;",
    "Top 5 Bowlers with Most Wickets": "SELECT bowler, COUNT(wicket) AS total_wickets FROM {table} WHERE wicket > 0 GROUP BY bowler ORDER BY total_wickets DESC LIMIT 5;",
    "Batter with Highest Strike Rate": "SELECT batter, SUM(runs) AS total_runs, COUNT(*) AS balls_faced, ROUND((SUM(runs) / COUNT(*)) * 100, 2) AS strike_rate FROM {table} GROUP BY batter HAVING balls_faced >= 300 ORDER BY strike_rate DESC LIMIT 5;",
    "Best Economy Rate Among Bowlers": "SELECT bowler, SUM(total_runs) AS runs_conceded, COUNT(*) AS balls_bowled, ROUND((SUM(total_runs) / (COUNT(*) / 6)), 2) AS economy_rate FROM {table} GROUP BY bowler HAVING balls_bowled >= 180 ORDER BY economy_rate ASC LIMIT 5;",
    "Most Dangerous Bowlers": "SELECT bowler, ROUND(SUM(total_runs) / COUNT(wicket), 2) AS bowling_average FROM {table} WHERE wicket > 0 GROUP BY bowler HAVING COUNT(wicket) > 10 ORDER BY bowling_average ASC LIMIT 5;",
    "Most Common Match Type": "SELECT match_type, COUNT(*) AS match_count FROM {table} GROUP BY match_type ORDER BY match_count DESC;",
    "Best Finishers": "SELECT batter, SUM(total_runs) AS total_death_over_runs FROM {table} WHERE over_number BETWEEN 16 AND 20 GROUP BY batter ORDER BY total_death_over_runs DESC LIMIT 5;",
    "Which Team Wins Most Matches Batting First?": "SELECT match_winner, COUNT(*) AS wins FROM {table} WHERE match_winner = batting_team GROUP BY match_winner ORDER BY wins DESC;",
    "Which Bowler is Most Effective Against a Specific Batter?": "SELECT bowler, COUNT(wicket) AS dismissals FROM {table} WHERE batter = 'V Kohli' AND wicket > 0 GROUP BY bowler ORDER BY dismissals DESC LIMIT 5;",
    "Batting Performance Against a Specific Bowler": "SELECT batter, SUM(runs) AS total_runs, COUNT(*) AS balls_faced, ROUND((SUM(runs) / COUNT(*)) * 100, 2) AS strike_rate FROM {table} WHERE bowler = 'MA Starc' GROUP BY batter ORDER BY total_runs DESC LIMIT 5;"
}

# Function to sanitize filenames by removing invalid characters
def sanitize_filename(name):
    invalid_chars = r'\/:*?"<>|'
    for char in invalid_chars:
        name = name.replace(char, "_")  # Replace invalid characters with underscore
    return name
# Execute Queries and Print Results
def execute_queries():
    for match_table, match_type in match_types.items():
        print(f"\n{'='*20} {match_type} Analysis {'='*20}")
        for title, query in queries.items():
            formatted_query = query.format(table=match_table)
            print(f"\n🔹 {title}\n" + "-" * 50)
            df = pd.read_sql_query(formatted_query, conn)
            print(df)
           # Check if DataFrame is empty before saving
            if df.empty:
                print(f"⚠️ Skipping {title} for {match_type}: No data found!")
                continue
            
            # Sanitize the filename
            safe_title = sanitize_filename(title)
            file_path = os.path.join(output_folder, f"{match_type}_{safe_title}.csv")

            # Double-check the path before writing
            if not os.path.isdir(output_folder):
                print(f"❌ Error: Output folder does not exist: {output_folder}")
                exit()
            
            # Save the result to CSV
            try:
                df.to_csv(file_path, index=False)
                print(f"✅ Saved: {file_path}")
            except Exception as e:
                print(f"❌ Error saving {file_path}: {e}")


execute_queries()

# Close the connection
conn.close()
