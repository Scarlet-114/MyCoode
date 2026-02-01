import pandas as pd

# 1. 通过 List 创建 (默认索引 0, 1, 2...)
ser_obj = pd.Series([10, 20, 30])

print(ser_obj) #打印输出会带类型

# 2. 通过 Dict 创建 (Key 变成索引)
year_data = {2001: 17.8, 2002: 20.1}

ser_obj2 = pd.Series(year_data)

print(ser_obj2)
# 结果:
# 2001  17.8
# 2002  20.1
# dtype: float64

# 3. 核心属性
print(ser_obj.index)  # 获取索引
print(ser_obj.values) # 获取数据 (返回 ndarray)