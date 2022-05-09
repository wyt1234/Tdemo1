#
def sort_list(l1: list, l2: list):
    temp_list_1 = []
    # temp_list_2 = []
    for one in l2:
        if one in l1:
            temp_list_1.append(one)
        # else:
        #     temp_list_2.append(one)
    temp_dic_list = []
    for index, v in enumerate(l1):
        if v in temp_list_1:
            temp_dic = {}
            temp_dic['key'] = v
            temp_dic['sort'] = index
            temp_dic_list.append(temp_dic)
    sorted(temp_dic_list, key=lambda x: x['sort'], reverse=False)
    result_list = [x['key'] for x in temp_dic_list]
    result_list.extend([x for x in l2 if x in l1])
    return result_list


if __name__ == '__main__':
    l1 = ['a', 'd', 'b']
    l2 = ['e', 'b', 'a', 'f']
    assert sort_list(l1, l2) == ['a', 'b', 'e', 'f']
    print('ok')
