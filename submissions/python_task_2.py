import pandas as pd

def calculate_distance_matrix(df):
    distance_matrix = df.pivot_table(values='distance', index='id_start', columns='id_end', fill_value=0)
    return distance_matrix

def unroll_distance_matrix(df):
    df_reset = df.reset_index()
    unrolled_df = pd.melt(df_reset, id_vars='id_start', var_name='id_end', value_name='distance')
    return unrolled_df

def find_ids_within_ten_percentage_threshold(df, reference_id):
    avg_distances = df.groupby('id_start')['distance'].mean().reset_index()
    reference_avg_distance = avg_distances.loc[avg_distances['id_start'] == reference_id, 'distance'].values[0]
    threshold = 0.1 * reference_avg_distance
    selected_ids = avg_distances[
        (avg_distances['distance'] >= reference_avg_distance - threshold) &
        (avg_distances['distance'] <= reference_avg_distance + threshold)
    ]
    return selected_ids


def main():
    filename1 = r'C:\Users\DELL\Desktop\assigment mapup\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
    df1 = pd.read_csv(filename1)
    filename2 = r'C:\Users\DELL\Desktop\assigment mapup\MapUp-Data-Assessment-F\datasets\dataset-2.csv'
    df2 = pd.read_csv(filename2)
    filename3 = r'C:\Users\DELL\Desktop\assigment mapup\MapUp-Data-Assessment-F\datasets\dataset-3.csv'
    df3 = pd.read_csv(filename3)
    distance_matrix_result = calculate_distance_matrix(df3)
    print("Distance Matrix:")
    print(distance_matrix_result)
    result_matrix = calculate_distance_matrix(df3)
    unrolled_df = unroll_distance_matrix(result_matrix)
    print(unrolled_df)
    result = find_ids_within_ten_percentage_threshold(df3, reference_id=1001400)
    print(result)
    
if __name__ == "__main__":  
    main()