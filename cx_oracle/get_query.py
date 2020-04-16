import os


def get_query(file_name):
    """
    SQLクエリの外部参照を行う
    """
    path = os.getcwd() + '/sql_query/' + file_name
    # with open(path, 'r', encoding='sjis') as f:
    with open(path, 'r', ) as f:
        query = f.read()
    return query


if __name__ == "__main__":
    query_file = "sample.sql"
    out = get_query(query_file)
    print(out)