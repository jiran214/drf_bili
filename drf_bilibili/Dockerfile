# 建立 python 3.9环境
FROM python:3.8

# 安装netcat
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get update && apt install -y netcat
#RUN yum install -y netcat
#RUN apt-get update && apt install -y netcat
# 镜像作者
MAINTAINER JiRan

# 设置 python 环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 可选：设置镜像源为国内
RUN pip install -i https://pypi.douban.com/simple/ -U pip
RUN pip config set global.index-url https://pypi.douban.com/simple/
#COPY pip.conf /root/.pip/pip.conf

# 容器内创建 bilibili 文件夹
ENV APP_HOME=/var/www/html/bilibili
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# 将当前目录加入到工作目录中（. 表示当前目录）
ADD . $APP_HOME

# 更新pip版本
RUN #/usr/local/bin/python -m pip install --upgrade pip

# 安装项目依赖
RUN pip install -r requirements.txt

# 移除\r in windows
RUN sed -i 's/\r//' ./start.sh

# 给start.sh可执行权限
RUN chmod 777 ./start.sh

# 数据迁移，并使用uwsgi启动服务
ENTRYPOINT sh ./start.sh