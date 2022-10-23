import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('euro-daily-hist.csv')
df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 32])

plt.plot(X,Y)
plt.xlabel("Дата")
plt.ylabel("Рублей в 1 евро",)

plt.show()




