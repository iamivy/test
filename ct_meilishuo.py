
#encoding:utf-8

import json
import requests
import os

#对应六个子类目：粗棒针毛衣 中袖连衣裙 破洞牛仔裤 牛津鞋 韩版包 棒球帽
#for keynid in ["4883","4687","3685","4391","4799", "3977"]:

#长袖T,小西装
#for keynid in ["443","445",]:

#for keyword in ["孕妇装"，“粉+包”]
#http://www.meilishuo.com/search?searchKey=%E5%AD%95%E5%A6%87%E8%A3%85&searchType=1&filter=goods&frm=searchsuggestion&suggest_frm=
#http://www.meilishuo.com/search?searchKey=%E9%95%BF%E8%A2%96T&searchType=1&filter=goods&frm=searchsuggestion&suggest_frm=  长袖T

#对应的六大类目 牛仔裤 连衣裙 套装 运动鞋 手表 双肩包
#for keynid in ["2097", "2055", "2825", "3063", "3277", "2211"]:
#for keynid in ["4883","4687","3685","4391","4799", "3977"]:
#小西装，大衣
#["445","2693","2033","449","2613","2027","2045","4883"]:
'''
for keynid in ["445"]:
#for keyword in ["孕妇装"]:
    file=open(keynid, "wb")
    for i in range(0,25):
        #r = requests.get('http://121.40.144.93/index.php?m=search&q='+keyword+'&p='+str(i)+'&n=30')
        
        #r = requests.get('http://www.meilishuo.com/search?searchKey='+keyword+'keyword+&searchType=1&filter=goods&frm=searchsuggestion&suggest_frm=')
        #req="http://www.meilishuo.com/search?searchKey=%E5%AD%95%E5%A6%87%E8%A3%85&searchType=1&filter=goods&frm=searchsuggestion&suggest_frm="

        #req="http://www.meilishuo.com/guang/catalog/dress?cata_id=2000000000000&nid=445&page=0&pstrc=fe_pos%3Awlc_navwords_0_15"
        #req="http://www.meilishuo.com/guang/catalog/dress?cata_id=2000000000000&nid="+keynid+"&page="+str(i)+"&pstrc=fe_pos%3Awlc_navwords_0_15"
        req2="http://www.meilishuo.com/aj/getGoods/catalog?frame="+str(i)+"&page=0&view=1&word=0&cata_id=2000000000000&section=hot&price=all&nid="+keynid+"&pstrc=fe_pos%3Awlc_words_1_2"

        print "请求的网址req:%s"%req
        print "请求的网址req2:%s"%req2

        r = requests.get(req)
        #r = open('shops/0')
        obj = json.loads(r.text)
        #print obj["result"]["twitterId"]
        #for item in obj["result"]["single"]:
        for item in obj["tInfo"]:
            url = "www.meilishuo.com"+ item['url']
            img = item['show_pic']
            #print url + " " + img
            file.write(url+"\t"+img+"\n")
            #print url+"\t"+img+"\n"
            #open('baobeiid', 'ab').write(item["iid"] + ' ' + item["twitterId"]+'\n')

    file.close()
'''


#模拟浏览器的给服务器发送get请求，刷取页面下的所有信息
#上衣：["445","2033","4883","2027","449","2025"] [“2613”,”2045”]
#包包：["2211","2645","2669"]
#裙子：["5047","2549","2055"]  衣裙套装
#裤子：["2097","2087","2107"]
#配饰：["5257","5255","3287"]
#鞋子：["4565","2947","4365"]
#for keynid in ["2613","2045"]: #衬衫 毛衣
'''
for keynid in ["2613","2045","5257","5255","4565","2947","4365","3287","445","2033","4883","2027","449","2025","2211","2645","2669","5047","2549","2055","2097","2087","2107"]:
    file = open('./'+keynid,"wb")
    for pageIndex in range(0,3):
        for frameIndex in range(0,8):
            #上衣类目
            reqUrl="http://www.meilishuo.com/aj/getGoods/catalog?frame="+str(frameIndex)+"&page="+str(pageIndex)+"&view=1&word=0&cata_id=2000000000000&section=hot&price=all&nid="+keynid+\
            "&pstrc=fe_pos%3Awlc_words_1_2"

            #裙子类目
            #reqUrl="http://www.meilishuo.com/aj/getGoods/catalog?frame="+str(frameIndex)+"&page="+str(pageIndex)+"&view=1&word=0&cata_id=2000000000000&section=hot&price=all&nid="+keynid+\
            #"&pstrc=fe_pos%3Awlc_navwords_1_5"

            #裤子类目
            #reqUrl="http://www.meilishuo.com/aj/getGoods/catalog?frame="+str(frameIndex)+"&page="+str(pageIndex)+"&view=1&word=0&cata_id=2000000000000&section=hot&price=all&nid="+keynid+\
            #"&pstrc=fe_pos%3Awlc_words_1_4"
            #"//www.meilishuo.com/aj/getGoods/catalog?frame=1&page=0&view=1&word=0&cata_id=2000000000000&section=hot&price=all&nid=2097&pstrc=fe_pos%3Awlc_words_1_4"

            #鞋子类目
            #reqUrl="http://www.meilishuo.com/aj/getGoods/catalog?frame="+str(frameIndex)+"&page="+str(pageIndex)+"&view=1&word=0&cata_id=6000000000000&section=hot&price=all&nid="+keynid+\
            #"&pstrc=fe_pos%3Awlc_navwords_0_0"


            #包包类目
            #reqUrl="http://www.meilishuo.com/aj/getGoods/catalog?frame="+str(frameIndex)+"&page="+str(pageIndex)+"&view=1&word=0&cata_id=5000000000000&section=hot&price=all&nid="+keynid+\
            #"&pstrc=fe_pos%3Awlc_attr_3"

            #配饰类目
            #reqUrl="http://www.meilishuo.com/aj/getGoods/catalog?frame="+str(frameIndex)+"&page="+str(pageIndex)+"&view=1&word=0&cata_id=5000000000000&section=hot&price=all&nid="+keynid+\
            #"&pstrc=fe_pos%3Awlc_attr_3"

            print "模拟浏览器发送get url:%s"%reqUrl

            res = requests.get(reqUrl)
            resbody = json.loads(res.text)
            totalNum = resbody["totalNum"]
            for item in resbody["tInfo"]:
                shop_url = "www.meilishuo.com"+item['url']
                img_url = item['show_pic']
                file.write(shop_url+"\t"+img_url+"\n")
    file.close()
'''



#榜单内商品数量抓取
file = open("./meilishuo_goods_count.txt","wb")
for keynid in ["2613","2045","5257","5255","4565","2947","4365","3287","445","2033","4883","2027","449","2025","2211",\
               "2645","2669","5047","2549","2055","2097","2087","2107"]:
    reqUrl="http://www.meilishuo.com/aj/getGoods/catalog?frame=1&page=0&view=1&word=0&cata_id=2000000000000&section=hot&price=all&nid="+keynid+\
            "&pstrc=fe_pos%3Awlc_words_1_2"
    print "模拟浏览器发送get url:%s"%reqUrl
    res = requests.get(reqUrl)
    resbody = json.loads(res.text)
    totalNum = resbody["totalNum"]
    print "the totalNum is %s"%totalNum
    file.write("%s:%s\n"%(keynid,totalNum))
file.close()



























