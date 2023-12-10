import pandas as pd


def main():
    filename1 = r'C:\Users\DELL\Desktop\assigment mapup\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
    df1 = pd.read_csv(filename1)
    filename2 = r'C:\Users\DELL\Desktop\assigment mapup\MapUp-Data-Assessment-F\datasets\dataset-2.csv'
    df2 = pd.read_csv(filename2)
    filename3 = r'C:\Users\DELL\Desktop\assigment mapup\MapUp-Data-Assessment-F\datasets\dataset-3.csv'
    df3 = pd.read_csv(filename3)


if __name__ == "__main__":  
    main()