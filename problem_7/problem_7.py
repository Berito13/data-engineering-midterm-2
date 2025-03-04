import pandas as pd


def etl_data(source_data, final_data):
    df = pd.read_csv(source_data)
    filtered_df = df[df['revenue'] > 5000]
    grouped_data = filtered_df.groupby('cluster').agg({'revenue': 'mean'})
    grouped_data.to_csv(final_data)
    print(grouped_data)


if __name__ == '__main__':
    source_data = r'C:\Users\Administrator\DataspellProjects\data_engineering_midterm_2\problem_7\data.csv'
    final_data = r'C:\Users\Administrator\DataspellProjects\data_engineering_midterm_2\problem_7\final_data.csv'
    etl_data(source_data, final_data)
