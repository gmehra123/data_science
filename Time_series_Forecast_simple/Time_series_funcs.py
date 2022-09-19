import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import SimpleExpSmoothing


def seasonal_decompose_data(data):
	"""Returns the plotted seasonal decomposition of a time series. Data has to have a time series index"""
	results=seasonal_decompose(data)
	fig=plt.figure(figsize=(12,12))
	plt.subplot(3,1,1)
	plt.plot(results.trend)
	plt.subplot(3,1,2)
	plt.plot(results.seasonal)
	plt.subplot(3,1,3)
	plt.plot(results.resid)
	return(fig)
	

