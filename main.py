from collections import deque

import requests

from extracter.myextracter import myextracter
from filter.setfilter import setfilter
from handler.myhandler import myhandler

#初始化组件：队列，过滤器，链接提取器，页面处理器
queue = deque()
myfilter = setfilter()
handler = myhandler()
extracter = myextracter()

#初始化状态
init_url = "https://mm.taobao.com/"
queue.append(init_url)
myfilter.add(init_url)



file_path = 'E:/mm/'
count = 0
i = 1;
s = requests.session()

while queue:
    url = queue.popleft()
    print('已经抓取：' + str(count) + '个，正在抓取-->' + url)
    count += 1
    #下载网页准备处理
    try:
        r = s.get(url, timeout = 2)
        r.encoding = 'UTF-8'
    except:
        continue
    
    urls = extracter.extract_urls(r.text, 'a', 'href')
    for x in urls:
        if 'mm.taobao.com' in x  and myfilter.contains(x) == False:
            queue.append("https:" + x)
            myfilter.add("https:" + x)
    
    
    links = extracter.extract_urls(r.text, 'img', 'src')
    for x in links:
        print("正在保存图片" + str(i) + "-->https:" + x)
        try:
            handler.save_file_binary(file_path +str(i) +".jpg", s.get("https:" + x, timeout = 2).content)
            i += 1
        except:
            continue
