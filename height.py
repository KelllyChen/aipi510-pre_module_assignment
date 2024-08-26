import pandas as pd

#read a CSV file and calculate the average height of the people listed in the file
def calculate_average(file='height.csv'):
    df = pd.read_csv(file)

    #check if the required column exists in the file
    if 'Heights' not in df.columns:
        raise ValueError("There's no column named Heights")
    return df['Heights'].mean()


if __name__=='__main__':
    #calculate the average height using the calculate_average function
    average_height=calculate_average()
    print("Average height of these people is", round(average_height,1))