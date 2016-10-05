#redis过滤器，实现链接去重，待实现

class redisfilter:
    #服务器信息
    server = "127.0.0.1"
    port = "6379"
    
    #向过滤器中添加元素
    def add(self, link):
        pass
     
    #检查是否重复
    def contains(self, link):
        pass
        
    #清空过滤器
    def clear(self):
        pass