import requests
import time 
import json
from lxml import etree

session = requests.session()

#登录之后查看
post_url = "https://m.exmail.qq.com/cgi-bin/login"
post_data = {"uin": "tanpeng@cbiconsulting.com", "pwd":"122579tP","mss":"1","btlogin":"登录","f":"xhtml"}
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

#登录
session.post(post_url,data=post_data,headers=headers)

#用上面的session get 登录之后页面
htmlRow= session.get("https://m.exmail.qq.com/cgi-bin/today?sid=8wiTyTK0lLmPb0AfodzQN-Ch,4,c6QngzDKCFfo.",headers=headers)#这个url需要更新？
htmlStr = htmlRow.content.decode()

html = etree.HTML(htmlStr)
inboxUrl = html.xpath("//a[@accesskey ='i']/@href")[0]
# print(inboxUrl)

#收件箱 url 请求
htmlRow = session.get(inboxUrl,headers=headers)
htmlStr = htmlRow.content.decode()
html = etree.HTML(htmlStr)

i=0
while i<3:
    url = "https://m.exmail.qq.com" + html.xpath("//a[@title='下一页']/@href")[0]
    print(html.xpath("//span[@class='qm_page_item qm_page_item_Mid']/text()"))
    htmlRow = session.get(url,headers=headers)
    htmlStr = htmlRow.content.decode()
    html = etree.HTML(htmlStr)
    i = i+1
#获取这一页的 每封邮件的url地址
# divList =html.xpath("//div[@class='readmail_list']/div")
# mailList = []
# for div in divList:
#     itemDic ={}
#     url ="https://m.exmail.qq.com" + div.xpath(".//a[@class='maillist_listItemRight']/@href")[0]
#     # print(url)
#     # class readmail_attach_listItem_name 附件
#     htmlRow = session.get(url,headers=headers)
#     htmlStr = htmlRow.content.decode()
#     html = etree.HTML(htmlStr)
#     itemDic["发件人 + 标题"]=html.xpath("//div[@class='readmail_item_from func_ellipsis']/text()")[0] + "+" \
#         + html.xpath("//h3[@class='readmail_item_head_titleText']/text()")[0]
#     itemDic["附件url"] ="https://m.exmail.qq.com" + html.xpath("//a[@class='readmail_attach_listItem_name']/@href")[0] \
#         if html.xpath("//a[@class='readmail_attach_listItem_name']/@href") else "no attach"

#     mailList.append(itemDic)
# print(r.status_code)
# print(mailList)
#
# with open("企业mail.html","w",encoding="utf-8") as f:
#     f.write(r.content.decode())