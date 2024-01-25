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

    'Cookie':'shshshfpa=b4dd54a2-9ff2-7053-4bcb-1c555fc7e88e-1625326179; __jdu=1307956879; shshshfpx=b4dd54a2-9ff2-7053-4bcb-1c555fc7e88e-1625326179; areaId=4; TrackID=1taVODM3e_7qfkagxg5anEwiEdpXaYuRXB0hSYdTvAbfnoM_uYucXa-WGGq1pfF8wFTnmK1mpbBDgPeizxZeFddZgxWiGRLQJQ_l7Y9xWWYQgQes_BzKhDN5Bgwrhrt1t; thor=BCE937575660B7998A224851838039428CFD28FB4674C023F928089ACF324398F337126F66458149141D9BF68EE032F7A74A2461C4DE71387DEBE54F3BBABD6C7E5C0CA18B57D37B21A016EA3ECA4C92D864EBD0136EB521082E617F8E25C990574A1CC05FBF925EA71D4B025847FD7E8ECD4BF2FC12A6B3A2A107E5FC8F9E3DB90030E31A1213B5F76DD622DF668F90; flash=2_lMNnqjaSXR1myUO06bKDi7peEpDvzW3w3voXKnPKeA1DUprPzubtmBEhcTPeK4y440_m07BTcHMe2UMGsEaIp5NUg_vEfbO9i7GRjUAbNd5*; pinId=6BT3PIK6VV9p_366V3AjUA; pin=sadasdsad3223; unick=sadasdsad3223; _tp=UAIJZKFYTtVXG2yUDhz9Zg%3D%3D; _pst=sadasdsad3223; user-key=4d44c61c-37f8-4bce-b22b-f4e11e55deaf; ipLoc-djd=4-50951-50965-0; PCSYCityID=CN_500000_500100_0; jsavif=0; cn=5; unpl=JF8EAIlnNSttX0gHUkgFHBMQSFxcW11dSR8Ab2BVVF9eSgRWE1dPRkR7XlVdWBRKFx9vZhRUXVNPVA4bCysSEXtdU11UC3sVCmxkAVNbWkNkBRwBEhEgSF1kX20ISRYFZ2MCXVtQe1U1GwocIiB7WlFZWwFCEgdfZjVVbRMlVUgbABoUGE9aXVhVOEonAA; __jdv=76161171|c.duomai.com|t_16282_382256739|jingfen|62bfb660120941d39216a1370ab9deee|1704858682425; 3AB9D23F7A4B3CSS=jdd03P43I7GOJWTDAAA3CI6MOZT46K2DDLNJFPTZCCHLNFU6KHISGZVGC67SXHWMRUJC7PRCCNGL7G45CJGPWPCK7ZIEKSEAAAAMM6F7PQ7AAAAAACYZ6G2HNH6MGCEX; _gia_d=1; 3AB9D23F7A4B3C9B=P43I7GOJWTDAAA3CI6MOZT46K2DDLNJFPTZCCHLNFU6KHISGZVGC67SXHWMRUJC7PRCCNGL7G45CJGPWPCK7ZIEKSE; token=f3e9927e09c6a305aeb6a5a4007bc136,3,947143; __tk=f7f699ab54d1828a8f3b7a3dac1362a6,3,947143; __jda=181111935.1307956879.1645424126.1704854623.1704858682.16; __jdc=181111935; shshshsID=e529f265290b33746168bac6a89b00b4_3_1704858718901; __jdb=181111935.4.1307956879|16.1704858682; shshshfpb=BApXewRJ38ulAK_qybbWe5_kCdSLkAVlUB2dzZlZn9xJ1Mt1JcNC2',
    'Referer':'https://item.jd.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
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

