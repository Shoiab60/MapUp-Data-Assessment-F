import pandas as pd

def generate_car_matrix(df):
    unique_ids = pd.concat([df['id_1'], df['id_2']]).unique()
    car_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids)
    for index, row in df.iterrows():
        car_matrix.at[row['id_1'], row['id_2']] = row['car']
    car_matrix = car_matrix.fillna(car_matrix.T)
    return car_matrix

def get_type_count(df):
    if 'car' not in df.columns:
        raise ValueError("The 'car' column does not exist in the DataFrame.")
    car_type_counts = df['car'].value_counts().to_dict()
    return car_type_counts

def get_bus_indexes(df):
    if 'bus' not in df.columns:
        raise ValueError("The 'bus' column does not exist in the DataFrame.")
    bus_mean = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    return bus_indexes

def filter_routes(df):
    if 'truck' not in df.columns:
        raise ValueError("The 'truck' column does not exist in the DataFrame.")
    route_avg_truck = df.groupby('route')['truck'].mean()
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    return filtered_routes

def multiply_matrix(matrix):
    condition1 = matrix < 5
    condition2 = (matrix >= 5) & (matrix < 10)
    condition3 = matrix >= 10
    modified_matrix = matrix.copy()
    modified_matrix[condition1] *= 2
    modified_matrix[condition2] *= 1.5
    modified_matrix[condition3] *= 1.2
    return modified_matrix

def main():
    filename1 = r'C:\Users\DELL\Desktop\assigment mapup\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
    df1 = pd.read_csv(filename1)
    car_matrix = generate_car_matrix(df1)
    print("Car Matrix:")
    print(car_matrix)
    type_counts = get_type_count(df1)
    print("Car Type Counts:")
    print(type_counts)
    bus_indices = get_bus_indexes(df1)
    print("Indexes where 'bus' values exceed twice the mean:")
    print(bus_indices)
    filtered_routes_list = filter_routes(df1)
    print("Routes with average 'truck' values greater than 7:")
    print(filtered_routes_list)
    result_matrix = multiply_matrix(df1)
    print("Modified Matrix:")
    print(result_matrix)

if __name__ == "__main__":  
    main()
