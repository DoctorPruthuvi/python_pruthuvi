import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Titanic:

    def __init__(self):
        self.train_st =None
        self.test_st =None
        Titanic.main(self)
  
    def main(self):
        Titanic.lad_data(self)
        Titanic.clean_data(self)


    def lad_data(self):
        self.train_st = pd.read_csv("titanic/train.csv")
        self.test_st = pd.read_csv("titanic/test.csv")

    def clean_data(self):
        #print the table descrition
        print(self.train_st.describe)

        #print the survived count
        print(self.train_st['Survived'].value_counts())

        #visualize the count of servivals
        sns.countplot(self.train_st['Survived'])
        plt.show()



if __name__ == "__main__":
    Titanic()