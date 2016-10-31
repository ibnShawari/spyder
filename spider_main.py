# coding=utf8
# ibnShawari@gmail.com
import html_downloader
import html_outputer
import html_paser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.Urlmanager()
        self.downloader = html_downloader.Htmldownloader()
        self.parser = html_paser.Htmlparser()
        self.outputer = html_outputer.Htmloutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            # 获取待爬取的URL
            try:
                new_url = self.urls.get_new_url()
                print("craw %d: %s" % (count, new_url))
                # 启动下载器下载页面
                html_cont = self.downloader.download(new_url)
                # 启动解析器
                new_urls, new_data = self.parser.pase(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 5:
                    break
                count += 1
            except:
                print("craw failed")

        self.outputer.output_html()

if __name__== "__main__":
    # 入口URL
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)