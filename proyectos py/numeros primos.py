import numpy as np
import seaborn as sns
import pandas as pd

n = 2000

x = np.arange(n)

y1 = np.sqrt(x)

y2 = x

df = pd.DataFrame({"O(√n)":y1,"O(n)":y2})

sns.set_theme()

sns.lineplot(data = df)