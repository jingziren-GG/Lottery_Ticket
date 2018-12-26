from .settings import MY_USER_AGENT
import random


# 随机进行提取请求头
class MyUserAgentMiddleware(object):
    # 每一个请求都会走这个方法
    def process_request(self,request,spider):
        UA = random.choice(MY_USER_AGENT)
        if UA:
            try:
                print(UA)
            except IOError:
                pass
            # 修改请求头
            request.headers.setdefault("User-Agent",UA)