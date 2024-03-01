import pandas as pd
import matplotlib.pyplot as plt

def load_dataset(file_path):
    return pd.read_csv(file_path)

def analyze_data(sales_data):
    total_sales = sales_data['SalesAmount'].sum()
    average_sales_per_day = sales_data.groupby('Date')['SalesAmount'].sum().mean()
    best_selling_products = sales_data.groupby('Product')['SalesAmount'].sum().nlargest(5)
    sales_trends = sales_data.groupby(pd.to_datetime(sales_data['Date']).dt.to_period('M'))['SalesAmount'].sum()
    return total_sales, average_sales_per_day, best_selling_products, sales_trends

def display_results(total_sales, average_sales_per_day, best_selling_products, sales_trends):
    print("Total sales:", total_sales)
    print("Average sales per day:", average_sales_per_day)
    print("\nTop 5 best-selling products:")
    print(best_selling_products)
    
    # Plot sales trends
    plt.figure(figsize=(10, 6))
    sales_trends.plot(kind='line', marker='o')
    plt.title('Sales Trends Over Time')
    plt.xlabel('Month')
    plt.ylabel('Sales Amount')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    file_path = 'sales_dataset.csv'  # Change this to your dataset file path
    sales_data = load_dataset(file_path)
    total_sales, average_sales_per_day, best_selling_products, sales_trends = analyze_data(sales_data)
    display_results(total_sales, average_sales_per_day, best_selling_products, sales_trends)

if __name__ == "__main__":
    main()
