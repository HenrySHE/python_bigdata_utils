from pyhive import hive
import jieba

if __name__ == "__main__":
    connection = hive.connect(
        # 89 Server
        host='localhost',  # host on which the database is running
        database='default',  # name of the database to connect to
    )

    cursor = connection.cursor()
    # cursor.execute('SELECT * FROM pokes')
    # customers = list(cursor.fetchall())
    # print('We have {} customers'.format(len(customers)))  # This is data science!

    with open("跑车型.txt", 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line_list = jieba.lcut(line)
            data = " ".join(line_list)
            query = "INSERT INTO default.word_count_data (file_id, content) " \
                "VALUES ('test.txt_2021_08_02', '%s')" % data
            cursor.execute(query)

    cursor.close()
    connection.close()
