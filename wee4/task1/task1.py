
#串接、擷取公開資料
import urllib.request as request #網路連線載入模組
import json#為了要做json資料解析 載入json模組
import csv #載入csv
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)#網路連線讀取資料  利用json模組處理 json資料格式
#將名稱列表出來
clist=data["result"]["results"]#一個列表 中括號 列表結束
with open("attraction.csv","w",encoding="utf-8",newline="") as file:#寫入檔案
    writer=csv.writer(file)
    for record in clist:#用for迴圈 把資料一個個拉出來
        stitle = record["stitle"]
        longitude = record["longitude"]
        latitude=record["latitude"]
        file_urls = record["file"].split("https")
        first_jpg = "https"+file_urls[1]
        for item in clist:
            address = item["address"]
            middle_chars = address[5:8] # 取得中間的三個字元
        writer.writerow([stitle,middle_chars,longitude,latitude,first_jpg])

#將名稱列表出來
alist=data["result"]["results"]#一個列表 中括號 列表結束
with open("mrt.csv","w",encoding="utf-8",newline="") as archives:#寫入檔案
    writer=csv.writer(archives)

    mrt_dict = {}

    for place in alist:#用for迴圈 把資料一個個拉出來
        mrt = place["MRT"]
        attractions = place["stitle"]

        # 檢查MRT值是否在字典中，如果不在，則創建一個新的鍵值對
        if mrt not in mrt_dict:
            mrt_dict[mrt] = []#MRT字典=[]空物件
        mrt_dict[mrt].append(attractions)#將stitle值添加到對應的MRT值的列表中

    # 找出相同MRT值的stitle值
    for mrt, stitle_list in mrt_dict.items():
        if len(stitle_list) > 1:
            writer.writerow([mrt]+stitle_list)
        



    
    

    
