# recent_months = 4  # 最近几周的弹幕
# author:
# contact:
# datetime:
# software: PyCharm

"""
 文件说明：
 打印工程目录文件，参考链接：
 https://blog.csdn.net/albertsh/article/details/77886876
 """

import os
import os.path


def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")
    # print("当前文件路径是{}，包含文件有{}。".format(path, os.listdir(path)))

    for item in os.listdir(path):
        if item in ['__init__', '__pycache__']:
            continue

        print("| " * depth + "+--" + item)

        if item in ['.git', '.idea', '__pycache__', 'static', 'media', 'migrations', 'logs', 'log']:
            continue

        new_item = path + '/' + item
        if os.path.isdir(new_item):
            dfs_showdir(new_item, depth + 1)


if __name__ == '__main__':
    dfs_showdir('.', 0)

"""             
+--.sqlenv
+--apps 
| +--kol --up主搜索页面/详情页面
| | +--admin.py --后台管理
| | +--apps.py
| | +--filters.py --过滤组件
| | +--migrations --数据库
| | +--models.py --模型
| | +--ser.py --序列化器
| | +--tests.py 
| | +--urls.py --应用路由
| | +--views.py --类视图
| +--note --视频搜索/详情页面
| +--operation --用户收藏
| +--users --up主搜索页面/详情页面

+--bilibili                   
| +--asgi.py
| +--celery.py --celery初始化
| +--media --静态资源
| +--settings
| | +--base.py --django基础配置
| | +--celeryConf.py --celery配置
| | +--dev.py
| | +--drfConf.py --drf扩展配置
| | +--log.py --日志配置
| | +--prod.py
| +--urls.py --总路由
| +--wsgi.py

+--crawl --爬虫											
| +--items.py --scrapy djangoItem类
| +--log --日志
| | +--2022107.log
| +--middlewares.py --爬虫/下载中间件
| +--pipelines.py --管道:数据处理/更新/持久化存储
| +--process.py --数据存储更新策略
| +--settings.py --scrapy配置
| +--spiders --爬虫parse
| | +--get_danmu_comment.py --弹幕评论
| | +--get_kol.py --up主的最新信息
| | +--get_mid.py --获取up主
| | +--get_note.py --up主的最近视频

+--Dockerfile --docker配置
+--logs --django日志
| +--admin_error.log
| +--admin_info.log
| +--admin_operation.log
| +--admin_query.log

+--manage.py
+--requirements.txt --环境
+--scrapy.cfg --启动配置
+--start.py
+--start.sh --docker依赖脚本
+--static --静态资源
+--templates
+--utils --公共基类
| +--exception.py
| +--model.py
| +--rendererresponse.py
+--uwsgi.ini
"""
