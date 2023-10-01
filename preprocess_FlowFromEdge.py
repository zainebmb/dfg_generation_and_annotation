
def process_FFE(input_file_path, output_file_path):
    """this method do the following
    when the same edge has has more than 1 flow type:
    Data+any other type ( equiv/normal)=> Data 
    Data more than one time=> get the edge types of all the instances of the same edgein a list 
    normal=> normal
    """
    with open(input_file_path, 'r') as file:
        lines = [line.strip().split('\t') for line in file]

    edges_dict = {}

    result_lines = []
    for line in lines:
        from_node = line[0]
        to_node = line[2]
        flow_type = line[4]
        edge_label = line[6]

        key = (from_node, to_node)
        # if  flow type is Data
        if flow_type == 'data':
            if key in edges_dict:
                if edge_label not in edges_dict[key]:
                    edges_dict[key].append(edge_label)
            else:
             edges_dict[key] = [edge_label]
        # if Flow type is anything except Data
        else:
            if key not in edges_dict:
                result_lines.append([line[0],"[, ]",line[2], "[, ]", line[4], line[6]])

    # store unique data flow edges
    for key, edge_labels in edges_dict.items():
        result_lines.append([key[0], "[, ]", key[1], "[, ]", "data", ",".join(edge_labels)])

    # Writiingg the results
    with open(output_file_path, 'w') as file:
        for line in result_lines:
            file.write('\t'.join(line) + '\n')

    return output_file_path


# if __name__=='__main__':
    # input_file_path = utils.notebook + '/FlowFromEdge.csv'
    # output_file_path = 'output_file2.csv'
    # result = process_FFE(input_file_path, output_file_path)