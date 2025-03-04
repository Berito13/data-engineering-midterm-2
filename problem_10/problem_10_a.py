import pandas as pd
import numpy as np
from functools import partial

def transform_data(data, column_mapping=None, date_format=None,
                   numeric_precision=2, missing_values='drop',
                   filters=None):

    df = data.copy()

    # 1. rename
    if column_mapping:
        df.rename(columns=column_mapping, inplace=True)

    # 2. date type
    if date_format:
        date_columns = df.select_dtypes(include=['datetime64']).columns
        for col in date_columns:
            df[col] = df[col].dt.strftime(date_format)

    # 3. round numbers
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].round(numeric_precision)

    # 4. empty
    if missing_values == 'drop':
        df.dropna(inplace=True)
    elif missing_values == 'fill_zero':
        df.fillna(0, inplace=True)
    elif missing_values == 'fill_mean':
        df.fillna(df.mean(), inplace=True)

    # 5. filtering
    if filters:
        for column, value in filters.items():
            df = df[df[column] == value]

    return df

def example_usage():
    data = pd.DataFrame({
        'name': ['John', 'Alice', 'Bob', np.nan],
        'age': [25.678, 30.123, 35.456, 40.789],
        'date': pd.date_range(start='2023-01-01', periods=4),
        'city': ['New York', 'London', 'Paris', 'Tokyo']
    })

    transformed_data = transform_data(
        data,
        column_mapping={'name': 'full_name', 'city': 'location'},
        date_format='%Y-%m-%d',
        numeric_precision=1,
        missing_values='fill_zero',
        filters={'location': 'London'}
    )

    print("origin:")
    print(data)
    print("\ntransformed:")
    print(transformed_data)


if __name__ == "__main__":
    example_usage()