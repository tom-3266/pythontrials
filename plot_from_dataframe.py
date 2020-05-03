import pandas as pd
import matplotlib.pyplot as plt
car_sales=pd.read_csv("car-sales.csv")
car_sales["Price"]=car_sales["Price"].str.replace('[\$\,\.]','').astype(int)
car_sales["Price"]=car_sales["Price"]/100
car_sales["sale_date"]=pd.date_range('1/1/2020',periods=len(car_sales))
car_sales["total_sale"]=car_sales["Price"].cumsum()
car_sales.plot(x="sale_date",y="total_sale")
plt.show()
car_sales.plot(x="Odometer (KM)",y="total_sale",figsize=(8,5),kind="scatter");
plt.show()
