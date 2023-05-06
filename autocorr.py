import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import streamlit as st

###
### Dieser Code liest eine CSV-Datei in einen Pandas DataFrame ein, führt einige Datenaufbereitungen durch 
### und visualisiert die Daten mithilfe von Matplotlib. Das Ergebnis wird dann in eine Webanwendung in Streamlit 
### eingebettet.
###

# Seitentitel
st.title("Datenanalyse und Visualisierung")

# CSV-Datei in DataFrame importieren
data = pd.read_csv('Dummy_Data_4.csv', sep=None)

# Spalten für horizontale Darstellung erstellen
#col1, col2 = st.columns(2)

# Data check
st.subheader("Daten Vorschau")
st.write(data.head(5))

# Zusammenfassung der Daten anzeigen
st.subheader("Zusammenfassung der Daten")
st.write(f"Die Daten enthalten {data.shape[0]} Zeilen und {data.shape[1]} Spalten.")
st.write(data.describe())

# Data Cleaning
df = data
df = df.dropna()

# Datenbankverbindung herstellen
conn = sqlite3.connect('database.db')

# Daten in die Tabelle schreiben
data.to_sql('database', conn, if_exists='replace')

# Verbindung zur Datenbank schließen
conn.close()

# Neue Datenbankabfrage
# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('database.db')

# SQL-Abfrage ausführen und Ergebnis in Dataframe speichern
df = pd.read_sql_query("SELECT Open, High FROM database", conn)

# Verbindung zur Datenbank schließen
conn.close()

# Data Manipulation & Berechnung
# Dataframe df erstellen

# Spaltennamen erstellen
column1, column2 = df.columns[0], df.columns[1]

# Überprüfen, ob alle Elemente in type_names integer oder float sind
def check_for_corr_and_print(df):
    type_names = df.dtypes.values

    for t in type_names:
        if t not in ['int', 'float', 'float64']:
            # Grafik erstellen
            st.subheader("Datenvisualisierung")
            st.write("Die Daten können nicht visualisiert werden, weil sie nicht numerisch sind.")
            return
        else:
            #print("Alle Datentypen sind integer oder float")
            # Korrelation berechnen
            corr = df.iloc[:,0].corr(df.iloc[:,1])
            st.subheader("Korrelation")
            st.write(f"Die Korrelation zwischen {column1} und {column2} beträgt {corr}.")
            # Grafik erstellen mit Korrelation
            st.subheader("Datenvisualisierung")
            plt.scatter(df.iloc[:,0], df.iloc[:,1]) # iloc[Rows, Columns]
            plt.title(column2 + ' in Abhängigkeit von ' + column1 + ' mit Korrelation von ' + str(corr))
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.xticks(rotation=60) 
            st.pyplot(plt)
            return

# Funktion aufrufen
check_for_corr_and_print(df)
