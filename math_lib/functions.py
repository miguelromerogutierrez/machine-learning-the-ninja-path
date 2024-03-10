
def mean(lst):
  return sum(lst) / len(lst)

def deviation(lst, mean_value: float, fn = lambda x: x):
  return [fn(float(x) - mean_value) for x in lst]

def sqr_dev(lst, mean_value: float):
  return deviation(lst, mean_value=mean_value, fn=lambda x: x**2)

def variance(lst, mean_value: float):
  return mean(sqr_dev(lst, mean_value))

def covariance(lst1, lst2):
  x_mean = mean(lst1)
  y_mean = mean(lst2)
  x_deviations = deviation(lst1, x_mean)
  y_deviations = deviation(lst2, y_mean)
  return mean([dx*dy for dx, dy in zip(x_deviations, y_deviations)])

def straight_line(x, m, b):
    return m * x + b