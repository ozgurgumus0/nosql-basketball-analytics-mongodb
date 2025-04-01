import random

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

# Distribute time based on position
def distribute_time(player):
    total_seconds = convert_to_seconds(player['minutes'])
    if player['position'] == 'Guard':
        distribution = {
            "Left Wing": 0.3,
            "Right Wing": 0.3,
            "Left Corner": 0.05,
            "Right Corner": 0.05,
            "Paint": 0.1,
            "Top": 0.2
        }
    elif player['position'] == 'Forward':
        distribution = {
            "Left Wing": 0.2,
            "Right Wing": 0.2,
            "Left Corner": 0.1,
            "Right Corner": 0.1,
            "Paint": 0.3,
            "Top": 0.1
        }
    elif player['position'] == 'Center':
        distribution = {
            "Left Wing": 0.05,
            "Right Wing": 0.05,
            "Left Corner": 0.1,
            "Right Corner": 0.1,
            "Paint": 0.6,
            "Top": 0.1
        }
    time_spent = {section: int(total_seconds * percentage) for section, percentage in distribution.items()}
    return time_spent

# Combine player info and stats
def get_player_position_time(players_stats, players_info):
    player_time_positions = []
    for stat in players_stats:
        player_info = next((p for p in players_info if p['_id'] == stat['_id']), None)
        if player_info:
            time_spent = distribute_time({**stat, **player_info})
            player_time_positions.append({**stat, **player_info, "time_spent": time_spent})
    return player_time_positions

# Generate the results
results = get_player_position_time(players_stats, players_info)

# Display the results
for result in results:
    print(f"Player: {result['name']}, Position: {result['position']}, Time Spent: {result['time_spent']}")
