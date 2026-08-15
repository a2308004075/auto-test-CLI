import itertools

"""
正交表
"""

set1 = ['原车牌和OCR识别一致', '原车牌和OCR识别不一致']
set2 = ['原车牌和上一单车牌号一致', '原车牌和上一单车牌号不一致']



# 使用itertools.product生成所有可能的组合
combinations = list(itertools.product(set1, set2))

# 打印所有组合
for combo in combinations:
    print(combo)
