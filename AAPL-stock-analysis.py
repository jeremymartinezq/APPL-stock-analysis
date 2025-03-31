# Summary: This script processes the AAPL stock data from a CSV file using pandas,
#          and provides various outputs as specified in the assignment.

import pandas as pd

# Load the CSV file
file_path = 'AAPL.csv'  # Ensure the CSV is in the same directory
data = pd.read_csv(file_path)

# Function to process data and print required outputs
def process_data(data):
    # 1. Print out the shape of the data in the csv file
    print("1. Shape of the data:")
    print(data.shape)  # (rows, columns)

    # 2. Print the list of the name of the columns (header fields)
    print("\n2. List of column names:")
    print(data.columns.tolist())

    # 3. Print out the first 5 data in the file
    print("\n3. First 5 rows of the data:")
    print(data.head())

    # 4. Print out the last 3 data in the file
    print("\n4. Last 3 rows of the data:")
    print(data.tail(3))

    # 5. Print out the minimum value in the Low column
    print("\n5. Minimum value in 'Low' column:")
    print(data['Low'].min())

    # 6. Write the first 5 data into a dictionary and print the dictionary out
    first_five_dict = data.head().to_dict(orient='records')
    print("\n6. First 5 rows as a dictionary:")
    print(first_five_dict)

    # 7. Function to calculate the average closing price over the entire dataset
    avg_close = average_closing_price(data)
    print("\n7. Average Closing Price:")
    print(avg_close)

def average_closing_price(data):
    avg_close = data['Close'].mean()
    return avg_close

# Driver code
if __name__ == '__main__':
    process_data(data)
