# 🏏 Cricbuzz LiveStats

**Real-time Cricket Analytics Platform | SQL-Powered Insights | Interactive Dashboard**

---

## 📌 Project Overview

Cricbuzz LiveStats is a comprehensive cricket analytics platform that combines real-time data fetching, SQL analytics, and an interactive dashboard.

### Key Features

| Feature | Description |
|---|---|
| 📡 **Live Matches** | Real-time match scores and updates |
| 📊 **Top Player Stats** | Leaderboards for runs, wickets, all-rounders |
| 🔍 **SQL Analytics** | 25+ pre-built SQL queries (Beginner to Advanced) |
| 🛠️ **CRUD Operations** | Create, Read, Update, Delete player records |
| 📱 **Interactive Dashboard** | User-friendly Streamlit interface |

---

## 🎯 Problem Statement

Cricket generates massive amounts of data scattered across multiple sources. This platform centralizes cricket data and provides an intuitive interface for analysis.

**Solution:** A web application that fetches live cricket data, stores it in MySQL, and provides interactive analytics.

---

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                       Cricbuzz LiveStats                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│   │  Cricbuzz   │───▶│   Python    │───▶│    MySQL    │         │
│   │     API     │    │ (Requests)  │    │  Database   │         │
│   └─────────────┘    └─────────────┘    └─────────────┘         │
│                                                                   │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                   Streamlit Dashboard                    │   │
│   │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐   │   │
│   │  │   Home   │  │   Live   │  │  Stats   │  │   SQL   │   │   │
│   │  │   Page   │  │ Matches  │  │  Page    │  │Analytics│   │   │
│   │  └──────────┘  └──────────┘  └──────────┘  └─────────┘   │   │
│   │  ┌──────────┐                                            │   │
│   │  │   CRUD   │                                            │   │
│   │  │Operations│                                            │   │
│   │  └──────────┘                                            │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **API Call** → Fetch data from Cricbuzz
2. **Data Extraction** → Parse JSON response
3. **Data Transform** → Clean and structure data
4. **Database Insert** → Store in MySQL tables
5. **Dashboard Display** → Show in Streamlit UI

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.8+** | Backend logic, data processing |
| **Streamlit 1.28+** | Interactive web dashboard |
| **MySQL 8.0+** | Data storage and querying |
| **Requests** | API calls to Cricbuzz |
| **Pandas** | Data manipulation |
| **mysql-connector** | Python–MySQL connection |

---

## 📝 25 SQL Queries

### Beginner Level (8 Queries)

| Q# | Query Name | Description |
|---|---|---|
| Q1 | Players Representing India | List all Indian players with roles and styles |
| Q2 | Recent Matches | Show recent matches sorted by date |
| Q3 | Top ODI Run Scorers | Top 10 run scorers in ODI cricket |
| Q4 | Venues > 25,000 Capacity | Venues with large seating capacity |
| Q5 | Team Wins | Count wins per team |
| Q6 | Players by Role | Distribution of players by role |
| Q7 | Highest Individual Scores | Highest score per format |
| Q8 | Series Started in 2024 | Series launched in 2024 |

### Intermediate Level (8 Queries)

| Q# | Query Name | Description |
|---|---|---|
| Q9 | All-Rounders | Players with 1000+ runs and 50+ wickets |
| Q10 | Last 20 Completed Matches | Recent completed matches with details |
| Q11 | Player Format Comparison | Compare players across formats |
| Q12 | Home vs Away Performance | Win rates at home and away |
| Q13 | Batting Partnerships | Partnerships of 100+ runs |
| Q14 | Bowling at Venues | Bowler performance by venue |
| Q15 | Close Match Performance | Performance in tight matches |
| Q16 | Yearly Performance Analysis | Player performance trends by year |

### Advanced Level (9 Queries)

| Q# | Query Name | Description |
|---|---|---|
| Q17 | Toss Analysis | Impact of winning the toss |
| Q18 | Most Economical Bowlers | Best economy rates in limited-overs |
| Q19 | Most Consistent Batsmen | Players with lowest standard deviation |
| Q20 | Player Format Analysis | Match distribution by format |
| Q21 | Performance Ranking System | Combined batting, bowling, fielding score |
| Q22 | Head-to-Head Analysis | Team vs Team performance |
| Q23 | Recent Player Form | Last 10 performances analysis |
| Q24 | Best Batting Partnerships | Best player combinations |
| Q25 | Career Trajectory Analysis | Quarterly performance trends |

---

## 📂 Project Structure

```
cricbuzz-livestats/
│
├── app.py                          # Main Streamlit Application
│
├── pages/                          # Dashboard Pages
│   ├── 1_🏏_Home.py                # Home Page
│   ├── 2_📡_Live_Matches.py        # Live Matches
│   ├── 3_📊_Top_Player_Stats.py    # Top Player Stats
│   ├── 4_🔍_SQL_Analytics.py       # SQL Analytics
│   └── 5_🛠️_CRUD_Operations.py     # CRUD Operations
│
├── utils/                          # Utility Modules
│   ├── db_connection.py            # Database Connection
│   └── sql_queries.py              # 25 SQL Queries
│
├── cricbuzz-livestats.ipynb        # Jupyter Notebook (Data Pipeline)
│
└── README.md                       # Project Documentation
```

---

## 📊 Database Tables

| Table Name | Purpose |
|---|---|
| `players_india` | Indian players data |
| `matches_recent_q2` | Recent matches |
| `records_stats_q3` | ODI run scorers |
| `venues_capacity_q4` | Venue details |
| `team_wins_q5` | Team wins |
| `q6_player_roles` | Role distribution |
| `q7_highest_scores` | Highest scores |
| `q8_series_2024` | 2024 series |
| `q9_all_rounders` | All-rounders |
| `completed_matches` | Completed matches |
| `q11_player_format_comparison` | Format comparison |
| `team_home_away_performance` | Home/Away stats |
| `batting_partnerships` | Partnerships |
| `bowling_venue_analysis` | Bowling by venue |
| `close_match_performance` | Close match stats |
| `yearly_performance_analysis` | Yearly trends |
| `toss_analysis_q17` | Toss analysis |
| `q18_economical_bowlers` | Economical bowlers |
| `q19_consistent_batsmen` | Consistent batsmen |
| `q20_player_format_analysis` | Format analysis |
| `q21_Performance_ranking` | Performance ranking |
| `q22_head_to_head_analysis` | Head-to-head |
| `q23_player_form_analysis` | Player form |
| `q24_best_partnerships` | Best partnerships |
| `q25_player_career_trajectory` | Career trajectory |

---

## 🔧 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher

### Step 1: Install Dependencies

```bash
pip install streamlit mysql-connector-python pandas requests
```

### Step 2: Setup MySQL Database

```sql
CREATE DATABASE crickbuzz_db;
USE crickbuzz_db;
```

### Step 3: Run the Jupyter Notebook

Execute all cells in `cricbuzz-livestats.ipynb` to create tables and populate data.

### Step 4: Update Database Credentials

Update `utils/db_connection.py`:

```python
MYSQL_CONFIG = {
    'user': 'root',
    'password': 'your_password',
    'host': '127.0.0.1',
    'database': 'crickbuzz_db'
}
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

---

## 🚀 How to Run

```bash
# Navigate to project folder
cd cricbuzz-livestats

# Run the app
streamlit run app.py

# Or using Python module
python -m streamlit run app.py
```

Open your browser and go to: [http://localhost:8501](http://localhost:8501)

---

## 📸 Screenshots

### 🏠 Home Page
https://raw.githubusercontent.com/kuraln96-hu/Project_1/main/screenshots/home.png

### 📡 Live Matches
https://raw.githubusercontent.com/kuraln96-hu/Project_1/main/screenshots/live_matches.png

### 📊 Top Player Stats
https://raw.githubusercontent.com/kuraln96-hu/Project_1/main/screenshots/player_stats.png

### 🔍 SQL Analytics
https://raw.githubusercontent.com/kuraln96-hu/Project_1/main/screenshots/sql_analytics.png

### 🛠️ CRUD Operations
https://raw.githubusercontent.com/kuraln96-hu/Project_1/main/screenshots/crud_operations.png

---

## 📊 Evaluation Metrics

| Sl. No | Metrics | Marks |
|---|---|---|
| 1 | Code Quality / Data Transformations | 10 |
| 2 | Proper Documentation (README/Insights/PPT) | 10 |
| 3 | Code Reusability / Modular Programming | 10 |
| 4 | Presentation | 10 |
| 5 | Task Accomplishment | 10 |
| 6 | 5 Mock Questions | 10 |
| | **Total** | **60** |

---

## 🚀 Future Enhancements

- [ ] WebSocket for real-time score updates
- [ ] Auto-refresh for live matches
- [ ] User authentication and profiles
- [ ] Predictive analytics for match outcomes
- [ ] Player performance forecasting
- [ ] Docker containerization
- [ ] Cloud deployment (AWS/Azure/GCP)

---

## 🙏 Acknowledgments

- **Cricbuzz** for providing the API
- **GUVI** for the learning platform and support
- **Streamlit** for the amazing framework
- **MySQL** for the reliable database

---

## 📧 Contact

| Name | Role |
|---|---|
| Kuraloviya | Developer |
