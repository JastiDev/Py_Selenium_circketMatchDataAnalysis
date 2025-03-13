import os
import json
import pandas as pd

# Folder path where JSON files are stored
folder_path = "C:\\Users\\admin\\Downloads\\odis_json"  # Change this to your actual folder path

# Lists to store structured data
matches_list = []
deliveries_list = []

# Loop through all JSON files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):  # Process only JSON files
        file_path = os.path.join(folder_path, filename)

        # Generate match_id from file name (remove .json extension)
        match_id = filename.replace(".json", "")

        # Load JSON file
        with open(file_path, "r") as file:
            match_data = json.load(file)

        # Extract Match Metadata
        match_info = match_data.get("info", {})
        match_type = match_info.get("match_type", "Unknown")

        # Skip non-ODI matches
        if match_type != "ODI":
            continue

        venue = match_info.get("venue", "Unknown")
        teams = match_info.get("teams", ["Unknown", "Unknown"])
        toss_winner = match_info.get("toss", {}).get("winner", "Unknown")
        toss_decision = match_info.get("toss", {}).get("decision", "Unknown")
        match_winner = match_info.get("outcome", {}).get("winner", "Unknown")

        matches_list.append({
            "match_id": match_id,
            "venue": venue,
            "team_1": teams[0] if len(teams) > 0 else "Unknown",
            "team_2": teams[1] if len(teams) > 1 else "Unknown",
            "match_type": match_type,
            "toss_winner": toss_winner,
            "toss_decision": toss_decision,
            "match_winner": match_winner
        })

        # Extract Deliveries & Powerplay Data
        powerplay_overs = set()  # Store powerplay overs

        for inning in match_data.get("innings", []):
            batting_team = inning.get("team", "Unknown")

            # Extract Powerplay Info
            for pp in inning.get("powerplays", []):
                start_over, end_over = int(pp.get("from", 0)), int(pp.get("to", 0))
                for over in range(start_over, end_over + 1):
                    powerplay_overs.add(over)  # Mark as powerplay over

            # Extract Deliveries
            for over_data in inning.get("overs", []):
                over_number = int(over_data.get("over", 0))  # Convert to int

                for delivery in over_data.get("deliveries", []):
                    ball_number = int(delivery.get("ball", 0))  # Convert to int
                    
                    deliveries_list.append({
                        "match_id": match_id,
                        "batting_team": batting_team,
                        "over_number": over_number,
                        "ball_number": ball_number,
                        "batter": delivery.get("batter", "Unknown"),
                        "bowler": delivery.get("bowler", "Unknown"),
                        "runs": delivery.get("runs", {}).get("batter", 0),
                        "extras": delivery.get("runs", {}).get("extras", 0),
                        "total_runs": delivery.get("runs", {}).get("total", 0),
                        "wicket": 1 if "wickets" in delivery else 0,
                        "powerplay": 1 if over_number in powerplay_overs else 0  # 1 = Powerplay, 0 = Normal Over
                    })

# Convert to DataFrame
matches_df = pd.DataFrame(matches_list)
deliveries_df = pd.DataFrame(deliveries_list)

# Save to CSV
matches_df.to_csv("odi_matche.csv", index=False)
deliveries_df.to_csv("odi_delivery.csv", index=False)

print("✅ All ODI JSON files processed successfully!")

#MERGE TWO STATIC AND DYNAMIC FILE TO FORM SINGLE FILE
df=pd.read_csv("D:\Cricket_DA_Pro\ODI_Match\odi_matche.csv")
df1=pd.read_csv("D:\Cricket_DA_Pro\ODI_Match\odi_delivery.csv")
#MERGE FILE
df2=pd.merge(df,df1,on="match_id")
df3=pd.DataFrame(df2)
df3.to_csv("ODI_Match.csv")
