# Author:Jay
av_catalog = {
    "欧美":{
        "www.youporn.com":["很多免费的，世界最大的","质量一般"],
        "www.pornhub.com":["很多免费的，也很大","质量比youporn高点"],
        "x-art.com":["质量很高，真的很高","全部收费，屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎么样不清楚","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费，好人一生平安","服务器在国外，慢"]
    },
}
av_catalog["大陆"]["1024"][1] = "可以在国内做镜像"
av_catalog.setdefault("taiwan",{"www.baidu.com":[1,2]})
print(av_catalog)