# data-analysis-google-creators-

📊 Marketing Campaign Performance Analysis

This project analyzes digital advertising campaign data to evaluate performance across creatives, platforms, age groups, interests, and influencer usage. It uses Pandas for data manipulation and Matplotlib for visualization.

The script loads campaign data from an Excel file, calculates key marketing metrics (CVR, CPA, cost, sales), and produces both tabular summaries and bar charts for easy insights.

🚀 Features

✅ Data validation for required columns

📈 Performance analysis by:

Creative
Platform
Age group
Interest category
Influencer vs non-influencer creatives

💰 Key metrics calculated:

Conversion Rate (CVR %)
Cost Per Acquisition (CPA)
Total cost
Total sales

📊 Automatic bar chart visualizations for selected metrics

🧠 Metrics Explained
Users: Number of users exposed
Sales: Total purchases
Cost: Total ad delivery cost
CVR (%): (Sales / Users) * 100
CPA: Cost / Sales

📂 Expected Data Format

The Excel file must contain the following columns:

Column Name	Description
USER_ID	Unique user identifier
CREATIVE_NAME	Name of the ad creative
CREATIVE_HAS_INFLUENCER	1 = Influencer, 0 = No influencer
AGE	User age
INTEREST_CATEGORY	User interest category
CITY	User city
PLATFORM_SHOWN_ON	Platform where ad was shown
AD_DELIVERY_COST	Cost of ad delivery
PURCHASE_PHONE	Purchase indicator (1/0)

If any required columns are missing, the script will raise an error.

🛠️ Installation

Clone the repository and install dependencies:

pip install pandas matplotlib openpyxl

▶️ How to Run

Place your Excel file in the project directory

Update the filename if needed inside main():

df = load_data("Digdata Google Next Step Dataset.xlsx")

Run the script:

python main.py

📊 Output

Printed performance tables in the console

Bar charts showing:

Conversion Rate by Creative

Cost Per Acquisition by Platform

Charts are automatically sorted for readability and include value labels.

🧩 Project Structure
├── main.py
├── Digdata Google Next Step Dataset.xlsx
├── README.md

🔮 Possible Extensions

Export results to CSV or Excel

Add time-based performance trends

Build a dashboard using Streamlit or Dash

Add statistical significance testing

📄 License

This project is open-source and free to use for learning and analysis purposes.
