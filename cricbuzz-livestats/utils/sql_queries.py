# ============================================================
# utils/sql_queries.py - All 25 SQL Queries
# ============================================================

SQL_QUERIES = {
    # ============================================================
    # BEGINNER LEVEL (Questions 1-8)
    # ============================================================
    
    "Q1: Players Representing India": {
        "query": """
            SELECT Player_name, Player_role, Batting_style, Bowling_style
            FROM players_india
            LIMIT 20
        """,
        "level": "Beginner",
        "description": "Find all players who represent India. Display their full name, playing role, batting style, and bowling style."
    },
    
    "Q2: Recent Matches": {
    "query": """
        SELECT match_desc, team1, team2, venue, start_date
        FROM matches_recent_q2
        WHERE start_date IS NOT NULL
        ORDER BY start_date DESC
        LIMIT 20
    """,
    "level": "Beginner",
    "description": "Show all cricket matches that were played in the last few days. Include match description, both team names, venue name with city, and match date. Sort by most recent matches first."
},
    
    "Q3: Top ODI Run Scorers": {
        "query": """
            SELECT player_name as Batter, total_runs_scored as Runs, 
                   batting_average as Avg, no_of_centuries as 100s
            FROM records_stats_q3
            ORDER BY total_runs_scored DESC
            LIMIT 10
        """,
        "level": "Beginner",
        "description": "List the top 10 highest run scorers in ODI cricket. Show player name, total runs scored, batting average, and number of centuries."
    },
    
    "Q4: Venues with Capacity > 25,000": {
        "query": """
            SELECT venue_name, city, country, capacity
            FROM venues_capacity_q4
            ORDER BY capacity DESC
            LIMIT 10
        """,
        "level": "Beginner",
        "description": "Display all cricket venues that have a seating capacity of more than 25,000 spectators. Show venue name, city, country, and capacity. Order by largest capacity first."
    },
    
    "Q5: Team Wins": {
        "query": """
            SELECT team_name, wins
            FROM team_wins_q5
            ORDER BY wins DESC
            LIMIT 10
        """,
        "level": "Beginner",
        "description": "Calculate how many matches each team has won. Show team name and total number of wins. Display teams with the most wins first."
    },
    
    "Q6: Players by Role": {
        "query": """
            SELECT role_name, player_count, percentage
            FROM q6_player_roles
            ORDER BY player_count DESC
        """,
        "level": "Beginner",
        "description": "Count how many players belong to each playing role. Show the role, count of players, and percentage distribution."
    },
    
    "Q7: Highest Individual Scores": {
        "query": """
            SELECT format_name, player_name, highest_score, balls_faced, 
                   strike_rate, opponent
            FROM q7_highest_scores
            ORDER BY FIELD(format_name, 'TEST', 'ODI', 'T20')
        """,
        "level": "Beginner",
        "description": "Find the highest individual batting score achieved in each cricket format (Test, ODI, T20I). Display the format, player name, and the highest score."
    },
    
    "Q8: Series Started in 2024": {
        "query": """
            SELECT series_name, series_type, host_country, match_type, 
                   DATE_FORMAT(start_date, '%Y-%m-%d') as start_date
            FROM q8_series_2024
            ORDER BY start_date
        """,
        "level": "Beginner",
        "description": "Show all cricket series that started in the year 2024. Include series name, host country, match type, start date, and total number of matches planned."
    },
    
    # ============================================================
    # INTERMEDIATE LEVEL (Questions 9-16)
    # ============================================================
    
    "Q9: All-Rounders": {
        "query": """
            SELECT player_name, total_runs, total_wickets, 
                   UPPER(format) as format
            FROM q9_all_rounders
            ORDER BY format, total_runs DESC
        """,
        "level": "Intermediate",
        "description": "Find all-rounder players who have scored more than 1000 runs AND taken more than 50 wickets in their career. Display player name, total runs, total wickets, and the cricket format."
    },
    
    "Q10: Last 20 Completed Matches": {
        "query": """
            SELECT match_description, team1_name, team2_name, 
                   winning_team, victory_margin, victory_type, venue_name
            FROM completed_matches
            ORDER BY match_id DESC
            LIMIT 20
        """,
        "level": "Intermediate",
        "description": "Get details of the last 20 completed matches. Show match description, both team names, winning team, victory margin, victory type (runs/wickets), and venue name."
    },
    
    "Q11: Player Format Comparison": {
        "query": """
            SELECT player_name, test_runs, odi_runs, t20_runs, 
                   overall_average, formats_played
            FROM q11_player_format_comparison
            ORDER BY formats_played DESC, overall_average DESC
            LIMIT 20
        """,
        "level": "Intermediate",
        "description": "Compare each player's performance across different cricket formats. For players who have played at least 2 different formats, show their total runs in Test, ODI, and T20I cricket."
    },
    
    "Q12: Home vs Away Performance": {
        "query": """
            SELECT team_name, home_wins, away_wins, 
                   (home_wins + away_wins) as total_wins
            FROM team_home_away_performance
            ORDER BY total_wins DESC
            LIMIT 15
        """,
        "level": "Intermediate",
        "description": "Analyze each international team's performance when playing at home versus playing away. Count wins for each team in both home and away conditions."
    },
    
    "Q13: Batting Partnerships (100+ runs)": {
        "query": """
            SELECT match_description, innings_name, 
                   batsman1_name, batsman1_runs, 
                   batsman2_name, batsman2_runs, combined_runs
            FROM batting_partnerships
            ORDER BY combined_runs DESC
            LIMIT 15
        """,
        "level": "Intermediate",
        "description": "Identify batting partnerships where two consecutive batsmen scored a combined total of 100 or more runs in the same innings. Show both player names, their combined partnership runs, and which innings it occurred in."
    },
    
    "Q14: Bowling Performance at Venues": {
        "query": """
            SELECT bowler_name, venue_name, matches_played, 
                   total_wickets, avg_economy
            FROM bowling_venue_analysis
            ORDER BY avg_economy ASC
            LIMIT 15
        """,
        "level": "Intermediate",
        "description": "Examine bowling performance at different venues. For bowlers who have played at least 3 matches at the same venue, calculate their average economy rate, total wickets taken, and number of matches played at each venue."
    },
    
    "Q15: Close Match Performance": {
        "query": """
            SELECT player_name, close_matches_played, team_wins, 
                   total_runs, average_runs
            FROM close_match_performance
            ORDER BY average_runs DESC
            LIMIT 20
        """,
        "level": "Intermediate",
        "description": "Identify players who perform exceptionally well in close matches. A close match is defined as one decided by less than 50 runs OR less than 5 wickets."
    },
    
    "Q16: Yearly Performance Analysis": {
        "query": """
            SELECT player_name, year, matches_played, 
                   avg_runs, strike_rate
            FROM yearly_performance_analysis
            ORDER BY year DESC, avg_runs DESC
            LIMIT 30
        """,
        "level": "Intermediate",
        "description": "Track how players' batting performance changes over different years. For matches since 2020, show each player's average runs per match and average strike rate for each year."
    },
    
    # ============================================================
    # ADVANCED LEVEL (Questions 17-25)
    # ============================================================
    
    "Q17: Toss Analysis": {
        "query": """
            SELECT match_description, toss_winner, toss_decision, 
                   match_winner, toss_winner_won_match
            FROM toss_analysis_q17
            WHERE match_winner IS NOT NULL
            ORDER BY match_id DESC
        """,
        "level": "Advanced",
        "description": "Investigate whether winning the toss gives teams an advantage in winning matches. Calculate what percentage of matches are won by the team that wins the toss."
    },
    
    "Q18: Most Economical Bowlers": {
        "query": """
            SELECT player_name, format, matches_played, 
                   total_overs, total_wickets, economy_rate
            FROM q18_economical_bowlers
            ORDER BY economy_rate ASC
            LIMIT 20
        """,
        "level": "Advanced",
        "description": "Find the most economical bowlers in limited-overs cricket (ODI and T20 formats). Calculate each bowler's overall economy rate and total wickets taken. Only consider bowlers who have bowled in at least 10 matches and bowled at least 2 overs per match on average."
    },
    
    "Q19: Most Consistent Batsmen": {
        "query": """
            SELECT player_name, total_innings, avg_runs, std_dev, 
                   highest_score, lowest_score
            FROM q19_consistent_batsmen
            ORDER BY std_dev ASC
            LIMIT 20
        """,
        "level": "Advanced",
        "description": "Determine which batsmen are most consistent in their scoring. Calculate the average runs scored and the standard deviation of runs for each player. A lower standard deviation indicates more consistent performance."
    },
    
    "Q20: Player Format Analysis": {
        "query": """
            SELECT player_name, total_matches, 
                   test_matches, test_avg,
                   odi_matches, odi_avg,
                   t20_matches, t20_avg
            FROM q20_player_format_analysis
            ORDER BY total_matches DESC
            LIMIT 30
        """,
        "level": "Advanced",
        "description": "Analyze how many matches each player has played in different cricket formats and their batting average in each format. Only include players who have played at least 20 total matches."
    },
    
    "Q21: Performance Ranking System": {
        "query": """
            SELECT player_name, format, batting_points, bowling_points, 
                   total_points, runs, wickets, economy
            FROM q21_Performance_ranking
            ORDER BY total_points DESC
            LIMIT 20
        """,
        "level": "Advanced",
        "description": "Create a comprehensive performance ranking system for players. Combine their batting, bowling, and fielding performance into a single weighted score."
    },
    
    "Q22: Head-to-Head Analysis": {
        "query": """
            SELECT team1, team2, total_matches, 
                   team1_wins, team2_wins,
                   team1_win_pct, team2_win_pct
            FROM q22_head_to_head_analysis
            ORDER BY total_matches DESC
        """,
        "level": "Advanced",
        "description": "Build a head-to-head match prediction analysis between teams. For each pair of teams that have played at least 5 matches against each other, calculate wins and win percentages."
    },
    
    "Q23: Recent Player Form Analysis": {
        "query": """
            SELECT player_name, last_5_avg, last_10_avg, strike_rate, 
                   scores_above_50, consistency_score, form_category
            FROM q23_player_form_analysis
            ORDER BY 
                CASE form_category
                    WHEN 'Excellent Form' THEN 1
                    WHEN 'Good Form' THEN 2
                    WHEN 'Average Form' THEN 3
                    WHEN 'Poor Form' THEN 4
                    ELSE 5
                END,
                last_5_avg DESC
            LIMIT 20
        """,
        "level": "Advanced",
        "description": "Analyze recent player form and momentum. For each player's last 10 batting performances, calculate averages, strike rate trends, scores above 50, and consistency score based on standard deviation."
    },
    
    "Q24: Best Batting Partnerships": {
        "query": """
            SELECT batsman1, batsman2, total_partnerships, avg_runs, 
                   partnerships_above_50, highest_partnership, success_rate
            FROM q24_best_partnerships
            ORDER BY avg_runs DESC
        """,
        "level": "Advanced",
        "description": "Study successful batting partnerships to identify the best player combinations. For pairs of players who have batted together as consecutive batsmen in at least 5 partnerships, calculate average runs, partnerships above 50, highest score, and success rate."
    },
    
    "Q25: Career Trajectory Analysis": {
        "query": """
            SELECT player_name, quarter, avg_runs, strike_rate, 
                   matches_played, trend, career_phase
            FROM q25_player_career_trajectory
            ORDER BY player_name, quarter
        """,
        "level": "Advanced",
        "description": "Perform a time-series analysis of player performance evolution. Track how each player's batting performance changes over time by calculating quarterly averages for runs and strike rate."
    }
}

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_queries_by_level(level):
    """Get queries filtered by level"""
    if level == "All":
        return SQL_QUERIES
    return {k: v for k, v in SQL_QUERIES.items() if v.get('level') == level}

def get_query_by_name(query_name):
    """Get a specific query by name"""
    return SQL_QUERIES.get(query_name)

def get_all_query_names():
    """Get all query names"""
    return list(SQL_QUERIES.keys())

def get_levels():
    """Get all distinct levels"""
    levels = set()
    for q in SQL_QUERIES.values():
        if 'level' in q:
            levels.add(q['level'])
    return sorted(levels)

def get_queries_count():
    """Get total number of queries"""
    return len(SQL_QUERIES)

def get_queries_by_level_count():
    """Get count of queries by level"""
    counts = {}
    for q in SQL_QUERIES.values():
        level = q.get('level', 'Unknown')
        counts[level] = counts.get(level, 0) + 1
    return counts