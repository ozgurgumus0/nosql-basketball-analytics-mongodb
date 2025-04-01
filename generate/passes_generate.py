import random
import json

players_stats = [
    {"_id": 1, "game_id": 1, "minutes": "42:09"},
    {"_id": 2, "game_id": 1, "minutes": "37:14"},
    {"_id": 3, "game_id": 1, "minutes": "35:10"},
    {"_id": 4, "game_id": 1, "minutes": "34:54"},
    {"_id": 5, "game_id": 1, "minutes": "29:48"},
    {"_id": 6, "game_id": 1, "minutes": "20:34"},
    {"_id": 7, "game_id": 1, "minutes": "16:02"},
    {"_id": 8, "game_id": 1, "minutes": "15:30"},
    {"_id": 9, "game_id": 1, "minutes": "3:19"},
    {"_id": 10, "game_id": 1, "minutes": "2:40"},
    {"_id": 11, "game_id": 1, "minutes": "0:42"},
    {"_id": 12, "game_id": 1, "minutes": "38:14"},
    {"_id": 13, "game_id": 1, "minutes": "36:29"},
    {"_id": 14, "game_id": 1, "minutes": "36:07"},
    {"_id": 15, "game_id": 1, "minutes": "28:47"},
    {"_id": 16, "game_id": 1, "minutes": "14:19"},
    {"_id": 17, "game_id": 1, "minutes": "20:17"},
    {"_id": 18, "game_id": 1, "minutes": "18:29"},
    {"_id": 19, "game_id": 1, "minutes": "18:29"},
    {"_id": 20, "game_id": 1, "minutes": "10:41"},
    {"_id": 21, "game_id": 1, "minutes": "7:42"},
    {"_id": 22, "game_id": 1, "minutes": "5:17"},
    {"_id": 23, "game_id": 1, "minutes": "4:58"}
]

players_info = [
    {"_id": 1, "name": "Jayson Tatum", "team": "Boston Celtics", "position": "Forward"},
    {"_id": 2, "name": "Jaylen Brown", "team": "Boston Celtics", "position": "Guard"},
    {"_id": 3, "name": "Derrick White", "team": "Boston Celtics", "position": "Guard"},
    {"_id": 4, "name": "Jrue Holiday", "team": "Boston Celtics", "position": "Guard"},
    {"_id": 5, "name": "Al Horford", "team": "Boston Celtics", "position": "Center"},
    {"_id": 6, "name": "Kristaps Porzingis", "team": "Boston Celtics", "position": "Forward"},
    {"_id": 7, "name": "Sam Hauser", "team": "Boston Celtics", "position": "Forward"},
    {"_id": 8, "name": "Payton Pritchard", "team": "Boston Celtics", "position": "Guard"},
    {"_id": 9, "name": "Luke Kornet", "team": "Boston Celtics", "position": "Center"},
    {"_id": 10, "name": "Svi Mykhailiuk", "team": "Boston Celtics", "position": "Guard"},
    {"_id": 11, "name": "Oshae Brissett", "team": "Boston Celtics", "position": "Forward"},
    {"_id": 12, "name": "Luka Doncic", "team": "Dallas Mavericks", "position": "Guard"},
    {"_id": 13, "name": "Kyrie Irving", "team": "Dallas Mavericks", "position": "Guard"},
    {"_id": 14, "name": "P.J. Washington Jr.", "team": "Dallas Mavericks", "position": "Forward"},
    {"_id": 15, "name": "Derrick Jones Jr.", "team": "Dallas Mavericks", "position": "Forward"},
    {"_id": 16, "name": "Daniel Gafford", "team": "Dallas Mavericks", "position": "Center"},
    {"_id": 17, "name": "Josh Green", "team": "Dallas Mavericks", "position": "Guard"},
    {"_id": 18, "name": "Maxi Kleber", "team": "Dallas Mavericks", "position": "Forward"},
    {"_id": 19, "name": "Dereck Lively II", "team": "Dallas Mavericks", "position": "Center"},
    {"_id": 20, "name": "Jaden Hardy", "team": "Dallas Mavericks", "position": "Guard"},
    {"_id": 21, "name": "Tim Hardaway Jr.", "team": "Dallas Mavericks", "position": "Forward"},
    {"_id": 22, "name": "Dante Exum", "team": "Dallas Mavericks", "position": "Guard"},
    {"_id": 23, "name": "Dwight Powell", "team": "Dallas Mavericks", "position": "Center"}
]

# Convert minutes to total seconds
def convert_to_seconds(minutes):
    mins, secs = map(int, minutes.split(':'))
    return mins * 60 + secs

# Generate random timestamp within the player's playing time
def generate_random_timestamp(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{random.randint(0, minutes):02}:{random.randint(0, seconds):02}"

# Determine quarter based on timestamp
def get_quarter(timestamp):
    mins, secs = map(int, timestamp.split(':'))
    total_secs = mins * 60 + secs
    if total_secs <= 720:
        return 1
    elif total_secs <= 1440:
        return 2
    elif total_secs <= 2160:
        return 3
    else:
        return 4

# Generate random passes between players
def generate_random_passes(players_stats, num_passes):
    passes = []
    for i in range(1, num_passes + 1):
        passing_player = random.choice(players_stats)
        receiving_player = random.choice([p for p in players_stats if p['_id'] != passing_player['_id']])
        
        total_seconds_passing = convert_to_seconds(passing_player['minutes'])
        total_seconds_receiving = convert_to_seconds(receiving_player['minutes'])
        
        timestamp = generate_random_timestamp(min(total_seconds_passing, total_seconds_receiving))
        quarter = get_quarter(timestamp)
        
        pass_event = {
            "pass_id": i,
            "game_id": passing_player['game_id'],
            "event_type": "pass",
            "timestamp": timestamp,
            "quarter": quarter,
            "passing_player_id": passing_player['_id'],
            "receiving_player_id": receiving_player['_id']
        }
        passes.append(pass_event)
    return passes

# Number of passes to generate
num_passes = 301

# Generate passes
passes = generate_random_passes(players_stats, num_passes)

# Print results
print(json.dumps(passes, indent=2))
