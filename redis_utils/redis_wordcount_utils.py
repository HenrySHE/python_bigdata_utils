import redis  # 导入redis包
import time
import jieba

# 与本地redis进行链接，地址为：localhost，默认端口号为6379 (87 Server)
pool = redis.ConnectionPool(host='localhost', port=6777)
r = redis.Redis(connection_pool=pool)

"""
另一种连接方法(不用connection pool), 
"""


# # 存储值
# r.hset("wc:job:test.txt_2021_07_29", "wow", "100")

# # 查询所有值:
# res_list = r.hkeys("wc:job:test.txt_2021_07_29")
# for item in res_list:
#     print(item.decode("utf-8"))
#     print(r.hget("wc:job:test.txt_2021_07_29", item.decode("utf-8")).decode("utf-8"))

file_name = '../resources/跑车型.txt'
jobs_hash = "wc:jobs"
job_prefix = "wc:job:"
job_name = file_name.replace(".txt", "") + time.strftime(
        "_%Y_%m_%d", time.localtime())


if not r.hexists(jobs_hash, job_name):
    # 先创建任务
    r.hset(jobs_hash, job_name, 0)
    # 开始读取文件, 写入词频
    with open(file_name, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line_list = jieba.lcut(line)
            for item in line_list:
                if len(item) <= 1:
                    continue
                r.zincrby(job_prefix + job_name, 1, item)

    # 更新任务状态
    r.hincrby(jobs_hash, job_name, 1)
    print('DONE!')
else:
    print('Job already Exist')


# # 用Hash的形式存储(弊端是没有排序, 取出来之后还要进行二次排序)
# if not r.hexists(jobs_hash, job_name):
#     # 先创建任务
#     r.hset(jobs_hash, job_name, 0)
#     # 开始读取文件, 写入词频
#     with open(file_name, "r", encoding='utf-8') as f:
#         for line in f:
#             line = line.strip()
#             line_list = jieba.lcut(line)
#             for item in line_list:
#                 if len(item) <= 1:
#                     continue
#                 r.hincrby(job_prefix + job_name, item, 1)
#
#     # 更新任务状态
#     r.hincrby(jobs_hash, job_name, 1)
#     print('DONE!')
# else:
#     print('Job already Exist')

# 导出结果, 统计词频
r.close()

