# Cricket-Match-Data-Analysis
This project automates cricket match data analysis using Selenium for web scraping, SQL for data storage, Python for processing &amp; EDA, and Power BI for visualization. It extracts insights on player performance, team stats, and match outcomes, making it valuable for sports analytics and decision-making. 🚀

# Cricket Match Data Analysis

## Project Overview
This project aims to scrape, process, analyze, and visualize cricket match data available at Cricsheet. Using **Selenium**, we extract JSON files of different match types (**ODI, T20, Test**), store the data in **SQL tables**, and create a **Power BI dashboard** to analyze key performance metrics. The project also includes **Exploratory Data Analysis (EDA)** using Python and **20 SQL queries** to uncover insights such as top-performing players, team statistics, and match outcomes.

## Skills Takeaway
- **Web Scraping using Selenium** - Automate data extraction from Cricsheet.
- **Data Processing with Python** - Work with JSON files and transform data using Pandas.
- **Database Management with SQL** - Create tables, insert data, and optimize queries.
- **Data Analysis** - Extract insights from cricket data using SQL queries.
- **Visualization with Power BI** - Create interactive dashboards for analysis.
- **Data Preprocessing** - Clean and structure raw JSON data.
- **Automation** - Streamline data collection using Selenium.

## Domain
**Sports Analytics / Data Analysis**

## Business Use Cases
- **Player Performance Analysis**: Compare players' performances across formats.
- **Team Insights**: Analyze team statistics and win/loss trends.
- **Match Outcomes**: Identify victory margins, winning patterns, and strategies.
- **Strategic Decision-Making**: Help analysts and coaches make informed decisions.
- **Fan Engagement**: Provide interactive dashboards for cricket enthusiasts.

---

## Project Approach
### **1. Data Scraping Using Selenium**
- Automate navigation to [Cricsheet](https://cricsheet.org/matches/).
- Scrape JSON files for **Test, ODI, T20, and IPL** matches.
- Store the downloaded files locally for further processing.

### **2. Data Transformation**
- Parse JSON files using **Pandas**.
- Create separate **DataFrames** for different match formats.

### **3. Database Management**
- Create an **SQL database** (MySQL/SQLite).
- Design separate tables: `test_matches`, `odi_matches`, `t20_matches`.
- Insert cleaned data into respective tables using **SQLAlchemy**.

### **4. SQL Queries for Data Analysis**
Write **20 SQL queries** to extract insights, including:
- Top 10 batsmen by total runs in ODIs.
- Leading wicket-takers in T20 matches.
- Team with the highest win percentage in Tests.
- Total number of centuries across match formats.
- Matches with the narrowest margin of victory.

### **5. Exploratory Data Analysis (EDA) using Python**
- Generate **10 visualizations** using **Matplotlib, Seaborn, and Plotly**.
- Present insights via graphs and summary statistics.

### **6. Power BI Dashboard**
- Connect **Power BI** to the SQL database.
- Create an interactive dashboard featuring:
  - **Player performance trends (batting, bowling).**
  - **Match outcomes by teams.**
  - **Win/loss analysis across different formats.**
  - **Comparative statistics of teams and players.**

---

## Results & Deliverables
✅ **Automated Scraping**: JSON files downloaded from Cricsheet.
✅ **Structured SQL Database**: Organized tables for different match types.
✅ **SQL Queries**: Insightful analysis on player and team performance.
✅ **EDA Visualizations**: Graphical analysis of key match statistics.
✅ **Power BI Dashboard**: Interactive and data-driven visual storytelling.
✅ **Project Documentation**: Detailed methodology and code explanation.

---

## Project Evaluation Metrics
- **Accuracy of Data**: Validate scraped and structured data.
- **SQL Queries**: Assess efficiency and relevance of the queries.
- **Power BI Dashboard**: Check completeness and visual appeal.
- **Project Execution**: Ensure seamless integration of Selenium, SQL, and Power BI.
- **Insights & Presentation**: Evaluate quality and clarity of findings.

---

## Tech Stack & Tools Used
- **Python** (Pandas, Selenium, Matplotlib, Seaborn, Plotly)
- **SQL** (MySQL/SQLite, SQLAlchemy)
- **Power BI**
- **Git & GitHub** (Version Control)
- **Jupyter Notebook**
- **Cricsheet JSON Data**

---

## Dataset Details
- **Source**: [Cricsheet Match Data](https://cricsheet.org/downloads/)
- **Format**: JSON files for individual cricket matches.
- **Variables**: Player statistics (runs, wickets), match results, teams, overs, deliveries.
- **Preprocessing Steps**:
  - Load JSON files into Python.
  - Normalize and flatten nested data.
  - Clean and structure data for SQL storage.

---

## How to Run This Project
### **1. Clone the Repository**
```bash
git clone https://github.com/your-github-username/Cricket-Match-Data-Analysis.git
cd Cricket-Match-Data-Analysis
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Selenium Scraper**
```bash
python scrape_cricket_data.py
```

### **4. Process JSON Data**
```bash
python process_data.py
```

### **5. Insert Data into SQL Database**
```bash
python insert_data.py
```

### **6. Run SQL Queries for Analysis**
```bash
python analyze_data.py
```

### **7. Perform EDA & Generate Visualizations**
```bash
python eda_visualizations.py
```

### **8. Open Power BI Dashboard**
- Load the `.pbix` file in **Power BI Desktop**.

---

## Project Guidelines
✔ **Follow coding best practices** (modular, commented, readable code).
✔ **Use GitHub for version control** (commit regularly).
✔ **Validate & clean data** before processing.
✔ **Write optimized SQL queries** for performance.
✔ **Ensure clear & insightful visualizations** in Power BI.

---

## Timeline
📅 **Estimated Completion**: 1 Week

---

## References
- **Cricsheet Dataset**: [https://cricsheet.org](https://cricsheet.org)
- **Power BI Guide**: Steps to create free Power BI account
- **EDA Guide**: Exploratory Data Analysis tutorial

---

## Contributors
👤 **Hana** - Data Science Enthusiast
📧 **(mailto:-hanarabeek2603@gmail.com)**

---

## License
This project is licensed under the **MIT License**

