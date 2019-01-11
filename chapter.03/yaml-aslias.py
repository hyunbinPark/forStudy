import yaml

# 문자열로 YAML 정의 
yaml_str = """
# 정의 
color_def:
    - &color1 "#FF0000"
    - &color2 "#00FF00"
    - &color3 "#0000FF"
# 별칭 테스트
color:
    title: *color1
    body: *color2
    link: *color3
"""
# YAML 데이터 분석 
data = yaml.load(yaml_str)

# 별칭 확인 
print("title = ",data["color"]["title"])
print("body = ",data["color"]["body"])
print("link = ",data["color"]["link"])