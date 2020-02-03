import numpy as np
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pandas.read_csv('./data/data_lon_lat/1/video_3.csv')
data = np.array(data)

lat = data[:,1:2]

# print(lat.shape)

ecdf = sm.distributions.ECDF(lat)
x = np.linspace(0, 360)
y = ecdf(x)
plt.ylim((0, 1.0))
plt.plot(x, y)
plt.xlabel('xxx')
plt.ylabel('yyy')
# plt.title('ECDF ' + params_name, fontdict=font)
plt.legend(loc='upper right', shadow=True)
plt.show()