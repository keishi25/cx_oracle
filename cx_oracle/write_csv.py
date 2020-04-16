import csv


def write_csv(filename, inputlist):
    """
    csv出力
    :param csv出力のファイル名、入力する配列の値
    """
    # Windowsでは、自動改行しないために、newlineの記述が必須
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(inputlist)


if __name__ == '__main__':
    file_name = 'sample.csv'
    input_list = ["a", "b", "c"]
    write_csv(file_name, input_list)

