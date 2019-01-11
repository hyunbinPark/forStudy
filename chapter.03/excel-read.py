import openpyxl

# 엑셀 파일 열기 
filename = "stat_104102.xlsx"
book = openpyxl.load_workbook(filename)

# 맨 앞의 시트 추출 
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출 
data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[9].value
    ])
# 필요없는 줄 제거  (헤더, 연도 , 계 )

del data[0]
del data[0]
del data[0]
del data[0]
del data[-1]
del data[-1]

# 데이터 인구 순 정렬 
print(data)
data = sorted(data, key=lambda x:x[1])

#하위 5위 출력 
for i, a in enumerate(data):
    if (i >= 5) : break
    a[1] = a[1].replace(',','')
    print(i+1, a[0], int(a[1]))