import pandas as pd

# data = {
#     "Name": ["Amit", "Rahul", "Priya"],
#     "Age": [25, 28, 22]
# }

# df = pd.DataFrame(data)

# print(df)

# import pandas as pd

# l=[1,2,3,4,5,6,7,8]
# ss = pd.Series(l)
# print(ss.head(4))
# print(ss.tail(4))
# print(ss.sample(4,random_state=42))

# import pandas as pd

# l = [1,2,3]
# Series = pd.Series(l,index=['student1','student2','student3'],name='series hai ye')
# print(Series.name)

# import pandas as pd

# l = [1,2,3]
# Series = pd.Series(l,index=['student1','student2','student3'],name='series hai ye')
# print(Series.is_unique)

# file1 = pd.read_csv('retail_orders.csv')
# print(type(file1))

# file1 = pd.read_csv('retail_orders.csv',index_col="order_id")
# print(file1)

performance = pd.read_csv("employee_performance.csv",index_col='employee_id')[['monthly_salary']].squeeze("columns")
# print(type(performance))

# # file2 = pd.read_csv("employee_performance.csv")
# print(file2['office_city'].value_counts())
# print(file2.count())
# print(performance.sort_values(ascending=False).head(5))
# print(performance.sort_index())
# print(performance.sum())
# print(performance.product())
# print(performance.std())
# print(performance.describe())

# print(performance.quantile(0.25))
# print(performance.loc['EMP006'])
# print(performance.iloc[[1,3,7]])

# coppy = performance.copy()
# coppy.loc['EMP015'] = 95000
# print(coppy.loc['EMP015'])

# coppy.iloc[0:2] = [70000, 72000]
# print(coppy.head(2))

# print(performance)
# print(type(performance))
# print(sorted(performance))
# print(type(sorted(performance)))

# print(list(performance))

# list1 = [[10000,20000,30000,40000,50000],[23,45,23,43,56]]
# dataframe1 = pd.DataFrame(list1,columns=['salary','age','height','weight','score'],index=['emp1','emp2'])
# print(dataframe1)

file1 = pd.read_csv('employee_performance.csv')
# print(file1.dtypes)

# print(file1[['monthly_salary']].sum(axis=0))

# print(file1.rename(columns=['monthly_salary':'new_salary']))

print(file1.loc[['EMP001','EMP002','EMP003']])

print("hello world")
