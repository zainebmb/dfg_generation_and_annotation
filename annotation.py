
def extract_overlap_leak_column(file_name): #get all leakage locations (in the 4rth column)
    column_values = []
    with open(file_name, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) >= 4:
                column_values.append(columns[2])
    return column_values
def extract_preproc_leak_column(file_name): #get all leakage locations (in the 1st column)
    column_values = []
    with open(file_name, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) >= 11:
                column_values.append(columns[2])
                column_values.append(columns[7])
    return column_values

def create_label_file(input_file, preproc_leak_values, overlap_leak_values):
    input_file_name = input_file.split('.')[0]
    label_file_name = input_file_name + '_label.csv'
    
    with open(label_file_name, 'w') as label_file:
       
                first_invo = input_file_name.split("/")[7].split('_')[0]
                second_invo = input_file_name.split("/")[7].split('_')[1]

                # print("1st invo: "+first_invo)
                # print("2st invo: "+second_invo)

                preproc_leak_label = 1 if first_invo in preproc_leak_values or second_invo in preproc_leak_values else 0
                overlap_leak_label = 1 if first_invo in overlap_leak_values or second_invo in overlap_leak_values else 0
                label_file.write(f"{overlap_leak_label}\t{preproc_leak_label}\n")


