# set过滤器，实现链接去重
class setfilter(object):
    myfilter = set()
    
    
    # 向过滤器中添加元素
    def add(self, link):
        self.myfilter.add(link)
     
    # 检查是否重复
    def contains(self, link):
        if link in self.myfilter:
            return True
        else:
            return False
        
    # 清空过滤器
    def clear(self,):
        self.myfilter.clear()
