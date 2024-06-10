"""
pyecharts 模块
"""

# 导入 pyecharts 模块中的 折线图 Line 对象
from pyecharts.charts import Line

# 创建 折线图 对象
line = Line()
def function1(rows):
    # 设置 x 轴数据
    line.add_xaxis(rows)


def function2(subject, data):
    # # 设置 y 轴数据
    line.add_yaxis(subject, data)
    # print(subject)
    # print(data)
def creat():
    # 生成图表
    line.render("cui.html")

