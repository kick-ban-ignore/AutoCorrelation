# AutoCorrelation
AutoCorrelation is a web application that makes data import, cleaning, filtering and visualisation a breeze.

This project is a Python web application that allows importing data from a CSV file into a SQLite database and then performing a correlation analysis between two columns. The application is written in Python 3.8 and uses the libraries pandas, sqlite3, matplotlib and streamlit.

# Installation

The libraries can be installed with pip:


    pip install pandas sqlite3 matplotlib streamlit

# Use

Open the CSV file you want to import into the database in a text editor or spreadsheet.
Save the file under any name and select the CSV format.
Start the Python script with

    python streamlit AutoCorrelation.py
 
Enter the path to the CSV file when prompted.
The data is automatically imported into an SQLite database.
You can filter the data with SQL by using the buttons and a correlation analysis between two columns is performed.
The results of the analysis are displayed in a plot.