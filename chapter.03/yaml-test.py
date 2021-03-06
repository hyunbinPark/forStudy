import yaml 

# YAML 정의    
yaml_str = """
Date : 2019-01-11
PriceList:
    -
        item_id: 1000
        name : Banana
        color : yellow
        price : 800
    
    -
        item_id: 1001
        name : Orange
        color : orange
        price : 1400
    
    -
        item_id: 1002
        name : Apple
        color : red
        price : 2400
"""
# YAML 분석하기 
data = yaml.load(yaml_str)
 
# 이름 & 가격 출력

for item in data['PriceList']:
        print(item["name"], item["price"])