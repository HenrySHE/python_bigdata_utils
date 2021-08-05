# Python BDT Utils
> Python Bigdata utils

## Hive
1. Hive connection
    - `hive_utils/hive_conn_util.py` is used to implement a wordcount application, using Jieba to cut the sentences 
    as list and save into hive, then using hive MapReduce to calculate the word and 
    its frequency
    - WordCount Query: 
       ```sql
       SELECT word, COUNT(*) as cnt 
           FROM word_count_data 
           LATERAL VIEW explode(split(content, ' ')) lTable as word
           WHERE file_id = 'test.txt_2021_08_02' 
           GROUP BY word 
           ORDER BY cnt DESC;
       ```

## Redis
1. Redis Basic Connection
    - `redis_utils/redis_wordcount_utils.py` and `redis_utils/redis_wordcount_search.py` shows basic `redis` usage,
    including how to connect to redis server, insert data (Hash, ZSets ect.), and also shows how to get data from redis. 
2. Redis Message Broker
    - `redis_message_broker.py` shows how to use `redis` package to publish messages
     and subscribe messages 
3. Redis Queue (RQ)
    - `redis_utils/redis_queue_rq/redis_queue_util.py` gives some basic function to use `RQ`.
    