import requests


r = requests.get("https://api.github.com/users/ziqing27")

# 响应状态码
print(r.status_code)
# 200
r.status_code == requests.codes.ok

# 请求url
r.url

# 请求方式
r.request

# 响应头
print(r.headers)

r.headers['content-type']
# 'application/json; charset=utf8'

# 请求头
r.request.headers

# html的编码
r.encoding
# 'utf-8'
r.apparent_encoding

# requests.utils.get_encodings_from_content()
# requests.utils.get_encoding_from_headers()
# requests.utils.get_unicode_from_response()

# 返回的内容
print(r.text)  # 字符串
print(r.content)  # 二进制响应内容
r.json()  # JSON 响应内容

# 定制请求头
url = 'http://www.merklechina.cn/'
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.8',
           'Referer': 'http://www.merklechina.cn/industry-solutions/%E9%93%B6%E8%A1%8C%E9%87%91%E8%9E%8D',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
           }
"""
Accept
    作用：浏览器端可以接受的媒体类型
    例如：Accept: text/html, 代表浏览器可以接受服务器回发的类型为"text/html", 也就是我们常说的html文档,
    如果服务器无法返回“text/html”类型的数据, 服务器应该返回一个406错误(non acceptable)
    
    通配符 * 代表任意类型, 例如  Accept: */*  代表浏览器可以处理所有类型,(一般浏览器发给服务器都会包含这个)

Accept-Encoding
    作用：浏览器申明自己接收的编码方法，通常指定压缩方法，是否支持压缩，支持什么压缩方法（gzip，deflate）

Accept-Language
    作用：浏览器申明自己接收的语言
    语言跟字符集的区别：中文是语言，中文有多种字符集，比如big5，gb2312，gbk等等
    例如：Accept-Language: en-us

Connection
    例如：Connection: keep-alive, 当一个网页打开完成后，客户端和服务器之间用于传输HTTP数据的TCP连接不会关闭，
    如果客户端再次访问这个服务器上的网页，会继续使用这一条已经建立的连接
    
    例如：Connection: close, 代表一个Request完成后，客户端和服务器之间用于传输HTTP数据的TCP连接会关闭，
    当客户端再次发送Request，需要重新建立TCP连接。

Host（发送请求时，该报头域是必需的）
    作用: 请求报头域主要用于指定被请求资源的Internet主机和端口号，它通常从HTTP URL中提取出来的
    例如: 我们在浏览器中输入：http://www.merklechina.cn/, 浏览器发送的请求消息中，就会包含Host请求报头域，
    如：Host：www.merkleinc.cn
    此处使用缺省端口号80，若指定了端口号，则变成：Host：指定端口号

Referer
    当浏览器向web服务器发送请求的时候，一般会带上Referer，告诉服务器我是从哪个页面链接过来的，
    服务器基于此可以获得一些信息用于处理，一般用于网站流量统计。

Content-Type: application/json; charset=UTF-8 
    浏览器接收的内容类型、字符

User-Agent
    作用：告诉HTTP服务器，客户端使用的操作系统和浏览器的名称和版本.
    我们上网登陆论坛的时候，往往会看到一些欢迎信息，其中列出了你的操作系统的名称和版本，你所使用的浏览器的名称和版本，
    这往往让很多人感到很神奇，实际上，服务器应用程序就是从User-Agent这个请求报头域中获取到这些信息
    User-Agent请求报头域允许客户端将它的操作系统、浏览器和其它属性告诉服务器。
    
    例如： User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; CIBA; .NET CLR 2.0.50727; 
    .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; InfoPath.2; .NET4.0E)

Cookie
    Cookie是用来存储一些用户信息以便让服务器辨别用户身份的（大多数需要登录的网站上面会比较常见），
    比如cookie会存储一些用户的用户名和密码，当用户登录后就会在客户端产生一个cookie来存储相关信息，
    这样浏览器通过读取cookie的信息去服务器上验证并通过后会判定你是合法用户，从而允许查看相应网页。
    当然cookie里面的数据不仅仅是上述范围，还有很多信息可以存储是cookie里面，比如sessionid等。

"""
r = requests.get(url, headers=headers)
print(r.status_code)

# 超时处理
# r = requests.get("https://www.bipt.edu.cn/", timeout=(3.05, 27))
# r = requests.get("https://www.bipt.edu.cn/", timeout=(1, 3))
# print(r.status_code)


# 异常处理
try:
    r = requests.get("https://www.merkleinc.com/", timeout=(1, 3))
    print('no error', r.status_code)
except requests.exceptions.ReadTimeout as ReadTimeout:
    print('ReadTimeout!')
finally:
    print('finish')





# 身份认证
# user = 'darren.li.027@gmail.com'
user = 'Darren-Li'
pwd = '1111'

requests.get('https://github.com/login', auth=(user, pwd))
r = requests.get('https://github.com/Darren-Li/ECharts')
r.status_code
print(r.text)
