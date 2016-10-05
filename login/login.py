#自定义登录模块
class loginer:
    #通过头信息伪装成火狐浏览器
    headinfo = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    
    def login(self, session, url, data):
        session.post(url, data, headers = self.headinfo)
        return session