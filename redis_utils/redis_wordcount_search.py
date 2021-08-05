import redis  # 导入redis包
import time
import jieba

# 与本地redis进行链接，地址为：localhost，默认端口号为6379 (87 Server)
pool = redis.ConnectionPool(host='localhost', port=6777)
r = redis.Redis(connection_pool=pool)

# # 存储值
# r.hset("wc:job:test.txt_2021_07_29", "wow", "100")


file_name = '../resources/跑车型.txt'
jobs_hash = "wc:jobs"
job_prefix = "wc:job:"
job_name = file_name.replace(".txt", "") + time.strftime(
        "_%Y_%m_%d", time.localtime())

# # 查询所有值: (hash)
# res_list = r.hkeys(job_prefix + job_name)
# word_count_list = []
# for item in res_list:
#     # print(item.decode("utf-8"))
#     # print(r.hget(job_prefix + job_name, item.decode("utf-8")).decode("utf-8"))
#     word_count_list.append((item.decode('utf-8'), int(r.hget(job_prefix + job_name, item.decode("utf-8")).decode("utf-8"))))
#
# sorted_list = sorted(word_count_list, key=lambda x: x[1], reverse=True)
# print(sorted_list)


# # 遍历Hash的键值对
# res_dic = r.hgetall("wc:jobs")
# for key in res_dic:
#     print(key.decode('utf-8'))
#     print(str(res_dic[key].decode('utf-8')) == "1")


# 查询所有值: (ZSets)
res_list = r.zrevrange(job_prefix + job_name, 0, 99, True)
for item in res_list:
    key_raw, value_raw = item
    key = key_raw.decode('utf-8')
    value = int(value_raw)
    print(key, value)

# 导出结果, 统计词频
r.close()