import pandas as pd
import numpy as np
from functools import partial
from problem_10_a import transform_data  # Assuming previous function is imported

def create_specialized_processors():

    finance_processor = partial(
        transform_data,
        column_mapping={
            'revenue': 'total_revenue',
            'expenses': 'total_expenses',
            'profit': 'net_profit'
        },
        date_format='%Y-%m-%d',
        numeric_precision=2,
        missing_values='fill_zero'
    )

    marketing_processor = partial(
        transform_data,
        column_mapping={
            'campaign_name': 'promo_name',
            'clicks': 'total_clicks',
            'conversions': 'conversion_rate'
        },
        numeric_precision=0,
        missing_values='drop',
        filters=lambda df: df[df.select_dtypes(include=[np.number]).columns] > 0
    )

    scientific_processor = partial(
        transform_data,
        numeric_precision=4,
        missing_values='fill_mean',
        date_format='%s'
    )

    return finance_processor, marketing_processor, scientific_processor

def example_usage():
    finance_data = {}
    marketing_data = {}
    scientific_data = {}

    finance_processor, marketing_processor, scientific_processor = create_specialized_processors()


    print(finance_processor(finance_data))

    print(marketing_processor(marketing_data))

    print(scientific_processor(scientific_data))

if __name__ == "__main__":
    example_usage()