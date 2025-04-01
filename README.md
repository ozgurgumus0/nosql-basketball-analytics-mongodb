# 📊 NoSQL Analytics with MongoDB – Advanced Data Modeling Project

This project showcases the use of **MongoDB** for building a flexible, scalable NoSQL data model to analyze complex, event-based datasets. Designed as part of the *Advanced Data Management and Decision Support Systems* course, it highlights how MongoDB’s aggregation framework and schema flexibility can power real-time analytical queries over structured and semi-structured data.

---

## 🚀 Project Overview

We modeled and analyzed a rich dataset based on an event-heavy domain (a professional basketball game) to explore advanced MongoDB features such as:

- NoSQL document-based schema design
- Complex aggregation pipelines
- Cross-collection joins with `$lookup`
- Real-time style data analysis and querying
- Python-based data simulation for semi-synthetic enrichment

The project uses **Game 1 of the NBA Finals 2024** as a scenario to simulate real-world challenges in building a NoSQL solution for high-volume, multi-entity event tracking.

---

## 🧱 Data Model (Collections)

| Collection          | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `games`             | Metadata for the game (teams, date, score, location)                        |
| `teams`             | Team-level stats: points, assists, rebounds, etc.                           |
| `players`           | Player metadata: name, position, team                                       |
| `box_score`         | Player performance stats (points, fouls, TS%, etc.)                         |
| `heat_map`          | Simulated data: time spent by players in court zones                        |
| `passes`            | Pass logs between players with timestamps and quarters                      |
| `possessions`       | All game events involving players (rebounds, fouls, assists, etc.)          |
| `team_possessions`  | Ball possession intervals per team, calculated with Python logic            |

---

## 🔍 Sample Aggregation Queries

### ✅ Highest Scoring Player

Finds the player with the most points in a given game by joining `box_score` and `players`, sorting by points, and returning top result.

### ✅ Fouls by Each Player

Joins player metadata with foul counts from `box_score`, then sorts in descending order.

### ✅ Court Zone Heatmap for a Player

Uses the `heat_map` collection to show which zones a player spent most time in. Data is generated using Python logic and weighted averages based on player position.

### ✅ Pass Count Between Two Players

Counts how many passes occurred between two specific players using the `passes` collection and MongoDB grouping.

### ✅ Team Ball Possession Timeline

Returns possession intervals for a specific team using the `team_possessions` collection.

---

## ⚙️ Technologies Used

- **MongoDB** (NoSQL database)
- **MongoDB Compass** (GUI for data exploration)
- **Python** (for generating synthetic data and processing)
- **JSON** (for document modeling)

---

## 🧠 Key Learning Outcomes

- Designing normalized and semi-denormalized schemas for NoSQL
- Using MongoDB’s aggregation pipeline for advanced analytics
- Combining real and synthetic data to simulate a real-world domain
- Performing temporal, statistical, and behavioral analysis in a NoSQL environment

---

## 📄 Project Report

See [`Report.pdf`](./Report.pdf) for complete documentation, technical decisions, query logic, and example outputs.

---

## 👥 Contributors

- **Ozgur Gumus**  

Supervised by:  
Andrea Maurino, Federico Cabitza, Andrea Campagner  
Università degli Studi di Milano, 2023

---

> This project is a strong example of using NoSQL systems like MongoDB for complex data analysis, making it applicable to use cases in IoT, sports analytics, user behavior tracking, and more.
