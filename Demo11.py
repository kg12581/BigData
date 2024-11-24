import re
import urllib.error
import urllib.request
import xlwt
from bs4 import BeautifulSoup

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datelist = get_date(baseurl)
    save_path = ".\\douban.xls"
    save_date(datelist, save_path)

def get_date(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = ask_url(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            # 提取电影详情链接
            link = re.findall(find_link, item)[0]
            data.append(link)
            # 提取电影图片链接
            img = re.findall(find_img, item)[0]
            data.append(img)
            # 提取电影名称
            title = re.findall(find_title, item)[0]
            data.append(title)
            # 提取电影评分
            rating = re.findall(find_rating, item)[0]
            data.append(rating)
            # 提取评价人数
            judge = re.findall(find_judge, item)[0]
            data.append(judge)
            # 提取电影简介
            inq = re.findall(find_inq, item)
            if len(inq)!= 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append("")
            datalist.append(data)
    return datalist

def ask_url(url):
    head = {"user-agent": "mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.97 safari/537.36"}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def save_date(datelist, savepath):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('电影', cell_overwrite_ok=True)
    col = ("电影详情", "图片", "影片", "评分", "评价数", "概况")
    for i in range(0, 6):
        worksheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datelist[i]
        for j in range(0, 6):
            worksheet.write(i + 1, j, data[j])
    workbook.save(savepath)

# 编译正则表达式，用于提取数据
find_link = re.compile(r'<a href="(.*?)">')
find_img = re.compile(r'<img.*src="(.*?)"', re.S)
find_title = re.compile(r'<span class="title">(.*)</span>')
find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
find_judge = re.compile(r'<span>(\d*)人评价</span>')
find_inq = re.compile(r'<span class="inq">(.*)</span>')

if __name__ == '__main__':
    main()
    print("爬取完毕")