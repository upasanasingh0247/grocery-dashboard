# 🛒 Grocery Sales Dashboard

## Project Overview
This project is an end-to-end data engineering and analytics dashboard that visualizes top-performing retail products. It bridges two disconnected, massive retail datasets (Dunnhumby transactions and BigBasket products) by extracting, cleaning, and merging the data in memory before serving it to an interactive web dashboard. 

## Business Problem Solved
Raw transactional data often lacks human-readable context (e.g., storing a `product_id` instead of a product name), and cross-referencing different database systems natively is not always possible due to schema mismatches. This project solves that by programmatically extracting high-volume sales metrics from a SQLite database, mapping them to a separate product catalog using a custom Pandas merge, and deploying the cleaned data for stakeholder viewing.

## Technology Stack
* **Database:** SQLite3
* **Data Processing:** Python, Pandas
* **Frontend/Visualization:** Streamlit
* **Version Control:** Git, GitHub

## Key Features
* **SQL Aggregation:** Queries over 2.6 million transaction rows to calculate accurate purchase volumes.
* **In-Memory Data Stitching:** Uses Pandas to bridge completely unlinked database tables without modifying the original schema.
* **Interactive Dashboard:** Deploys a lightweight, responsive Streamlit web app with dynamic bar charts and raw data tables.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/grocery-dashboard.git](https://github.com/your-username/grocery-dashboard.git)
   cd grocery-dashboard
