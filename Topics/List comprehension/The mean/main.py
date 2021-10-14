digits = input()
digits_list = [float(x) for x in digits]
mean = sum(digits_list) / len(digits_list)
print(round(mean, 1))
