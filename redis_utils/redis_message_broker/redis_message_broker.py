import redis  # 导入redis包
import time, threading


# 与本地redis进行链接，87 Server, 或者localhost, 端口号为6379
r = redis.StrictRedis(host='localhost', port=6777)


def publisher(n):
    # 函数在开始执行时会先休眠，让订阅者有足够的时间来连接服务器并监听消息
    time.sleep(1)
    r.publish('Msg1', 'hello')
    r.publish('Msg1', 'hi')
    r.publish('Msg1', 'how are you')
    # 在发送消息之后进行短暂的休眠，让消息可以一条接一条地出现
    time.sleep(1)
    # for i in range(n):
    #     r.publish('Msg1', i)
    #     # 在发送消息之后进行短暂的休眠，让消息可以一条接一条地出现
    #     time.sleep(1)


def run_pubsub():
    # 启动发送者线程，并让它发送三条消息
    # threading.Thread(target=publisher, args=(3,)).start()
    # 创建订阅对象，并对它订阅给定的频道
    pubsub=r.pubsub()
    pubsub.subscribe(['Msg1'])
    count=0
    # 通过遍历函数pubsub.listen()的执行结果来监听订阅消息
    for item in pubsub.listen():
        # 打印接收到的每条消息
        print(item)
        count += 1
        # if count == 4:
        #     pubsub.unsubscribe()
        # if count == 5:
        #     break


if __name__ == '__main__':
    # publisher(10)
    run_pubsub()