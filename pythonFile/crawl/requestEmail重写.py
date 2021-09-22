import requests
import time
import json
from lxml import etree


class emailE:

    def __init__(self):
        self.loginUrl = "https://m.exmail.qq.com/cgi-bin/login"
        # 这个postdata 可能需要更新
        self.postData = {"uin": "tanpeng@cbiconsulting.com",
                         "pwd": "122579tP", "mss": "1", "btlogin": "登录", "f": "xhtml"}
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        self.session = requests.session()
        # 下面这个url需要更新
        self.afterLoginUrl = "https://m.exmail.qq.com/cgi-bin/today?sid=vUY7xzz1bUB7JAtUodzQN-Ch,4,c6QngzDP02og."
        self.domain = "https://m.exmail.qq.com"

    def getHtml(self, url):
        htmlRow = self.session.get(url, headers=self.headers)
        htmlStr = htmlRow.content.decode()
        return etree.HTML(htmlStr)

    def getContent(self, inboxPageHtml):
        divList = inboxPageHtml.xpath(("//div[@class='readmail_list']/div"))
        mailList = []
        for div in divList:
            # print(div)
            itemDic = {}
            urlMail = self.domain + \
                div.xpath(".//a[@class='maillist_listItemRight']/@href")[0]
            html = self.getHtml(urlMail)
            itemDic["发件人 + 标题"] = html.xpath("//div[@class='readmail_item_from func_ellipsis']/text()")[
                0] + " + " + html.xpath("//h3[@class='readmail_item_head_titleText']/text()")[0]
            itemDic["附件url"] = [self.domain + i for i in html.xpath("//a[@class='readmail_attach_listItem_name']/@href")] if html.xpath(
                "//a[@class='readmail_attach_listItem_name']/@href") else "no attach"
            if itemDic["附件url"] != "no attach":
                urlList = []
                for url in itemDic["附件url"]:
                    # print(url)
                    urlList.append(self.domain+self.getHtml(url).xpath("//a[text()='下载附件']/@href")[
                                   0] if self.getHtml(url).xpath("//a[text()='下载附件']/@href") else "no re")
                itemDic["附件downurl"] = urlList

            mailList.append(itemDic)
        return mailList

    def save_content_list(self, content_list):  # 保存数据
        file_path = "tp_.txt"
        # print(content_list)
        with open(file_path, "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
        print("保存成功")

    def run(self):
        # 登录
        ss = self.session
        ss.post(self.loginUrl, data=self.postData, headers=self.headers)

        # 用 登录后的session 使用get 请求 登录之后的url 获取登录后的主界面
        mainHtml = self.getHtml(self.afterLoginUrl)

        # 进入收件箱
        # 获取收件箱url
        inboxUrl = mainHtml.xpath("//a[@accesskey ='i']/@href")[0]
        # 进入收件箱
        inboxPageHtml = self.getHtml(inboxUrl)
     
        # 获取每一页url
        while True:
            print(inboxPageHtml.xpath(
                "//span[@class='qm_page_item qm_page_item_Mid']/text()"))

            # 对每一页 的每一封邮件 获取content
            mailList = self.getContent(inboxPageHtml=inboxPageHtml)
            # 保存到txt文件
            self.save_content_list(mailList)
            # 没有 "下一页" 标签就推出
            if not inboxPageHtml.xpath("//a[@title='下一页']/@href"):
                break
            # 否则 更新 inboxPageHtml
            urlPage = self.domain + \
                inboxPageHtml.xpath("//a[@title='下一页']/@href")[0]
            inboxPageHtml = self.getHtml(urlPage)


if __name__ == '__main__':
    emailECrwal = emailE()
    emailECrwal.run()
