
# coding: utf-8

# In[1]:


def iNeedNet(dict_node_weight, dict_line_weight, directed, dict_node_partition, path_ucinet, path_gephi_node, path_gephi_line):
    dict_name_id = {}
    dict_id_name = {}
    _id = 1
    # 第一遍遍历赋予id
    for name in dict_node_weight.keys():
        dict_name_id[name] = _id
        dict_id_name[_id] = name
        _id += 1
    # 写入gephi
    ## 写入node文件
    f = open((path_gephi_node), 'w')
    f.write('Id,Label,partition,weighted degree\r\n')
    for _id in dict_id_name:
        if dict_node_partition == False:
            s = str(_id) + ',' + dict_id_name[_id] + ',0,' + str(dict_node_weight[dict_id_name[_id]]) + '\r\n'
#             if isinstance(s, unicode): s = s
            f.write(s)
        else:
            s = str(_id) + ',' + dict_id_name[_id] + ',' + str(dict_node_partition[dict_id_name[_id]]) + ',' +                     str(dict_node_weight[dict_id_name[_id]]) + '\r\n'
#             if isinstance(s, unicode): s = s
            f.write(s)
    f.close()
    ## 写入line文件
    f = open((path_gephi_line), 'w')
    f.write('Source,Target,Type,label,timeset,weight\r\n')
    for line in dict_line_weight:
        direct = 'Directed' if directed else 'unDirected'
        node0 = line.split(',')[0]
        node1 = line.split(',')[1]
        if node0 in dict_name_id and node1 in dict_name_id:
            f.write(str(dict_name_id[node0]) + ',' + str(dict_name_id[node1]) + ',' + direct + ',,,' + str(dict_line_weight[line]) + '\r\n')
    f.close()
    # 写入.net
    f = open((path_ucinet), 'w')
    f.write('*Vertices ' + str(len(dict_id_name)) + '\r\n')
    for _id in dict_id_name.keys():
        s = str(_id) + ' "' + dict_id_name[_id] + '"\r\n'
#         if isinstance(s, unicode): s = s
        f.write(s)
    if directed:
        f.write('*Arcs\r\n')
    else:
        f.write('*Edges\r\n')
    for line in dict_line_weight:
        node0 = line.split(',')[0]
        node1 = line.split(',')[1]
        if node0 in dict_name_id and node1 in dict_name_id:
            f.write(str(dict_name_id[node0]) + ',' + str(dict_name_id[node1]) + ' ' + str(dict_line_weight[line]) + '\r\n')
    f.close()

