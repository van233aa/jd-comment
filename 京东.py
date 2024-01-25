import requests
import parsel
import csv
from wordcloud import WordCloud
import jieba
jieba.setLogLevel(jieba.logging.INFO)

f=open('京东评论.csv','a',encoding='utf-8-sig',newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(['id','location','productColor','productSize','contents'])


headers={

    'Cookie':'................................',
    'Referer':'.........................',
    'User-Agent':..................................................',
}
for page_number in range(10):
    url=f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1704858727534&loginType=3&uuid=181111935.1307956879.1645424126.1704854623.1704858682.16&productId=100042508892&score=0&sortType=5&page={page_number}&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield='
    response = requests.get(url=url)
    travel_data = response.json()
    list = travel_data['comments']
    for i in list:
        id=i['id']
        location=i['location']
        productColor=i['productColor']
        productSize=i['productSize']
        content=i['content']
        print(id,location,productColor,productSize,content)
        csv_writer.writerow([id,location,productColor,productSize,content])

with open('京东评论.csv','r',encoding='utf-8-sig')as f:
    reader=csv.reader(f)
    # header=next(reader)
    column_index=4
    column_data=[row[column_index] for row in reader]


strc="".join(column_data)
txt=jieba.lcut(strc)
newtxt=''.join(txt)

wordcloud=WordCloud(width=2000,
                    height=1080,
                    font_path='msyh.ttc',
                    background_color='white',
                    # stopwords=ea,
                    ).generate(newtxt)
wordcloud.to_file('京东.png')

