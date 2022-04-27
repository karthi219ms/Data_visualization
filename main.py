import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
pd.plotting.register_matplotlib_converters()

file_path="book1.csv"
fifa_data=pd.read_csv(file_path,index_col="Date")
fifa_data.head()
plt.figure(figsize=(16,6))
sns.lineplot(data=fifa_data['ARG'],label='ARG')
plt.show()
def function():
    print(f'Hi')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    function()


