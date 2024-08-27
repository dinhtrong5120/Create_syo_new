import ast


def check_list_sap_xep(link_text, new_list):
    # Đọc dữ liệu từ tệp
    with open(link_text, 'r') as file:
        data = file.read()

    # Chuyển đổi chuỗi thành danh sách
    list_in_db = ast.literal_eval(data)
    list_sap_xep = []

    # Thêm các phần tử từ A vào result
    for item in new_list:
        list_sap_xep.append(item)

    # Duyệt qua từng phần tử của B và chèn vào result nếu chưa có
    for item in list_in_db:
        if item not in list_sap_xep:
            # Tìm vị trí để chèn phần tử
            for i in range(len(list_sap_xep)):
                if (i == len(list_sap_xep) - 1) or (
                        list_sap_xep[i + 1] in list_in_db and list_in_db.index(list_sap_xep[i + 1]) > list_in_db.index(
                    item)):
                    list_sap_xep.insert(i + 1, item)
                    break

    # Ghi đè lại vào tệp
    with open(link_text, 'w') as file:
        file.write(str(list_sap_xep))


if __name__ == '__main__':
    new_list = ['UNKNOW_device', 'LIGHTING']
    check_list_sap_xep('../db/your_file.txt', new_list)

    # print(list_sap_xep)
