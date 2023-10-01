# notebook="C:/Users/zaineb/Desktop/1162_w_edge_type_fact"
# notebook="C:/Users/zaineb/Desktop/2021-09-09-nb_498-fact"
# notebook="C:/Users/zaineb/Desktop/1290_w_edge_type_fact"
# notebook="C:/Users/zaineb/Desktop/new_1162_w_edge_type_fact"
# notebook="C:/Users/zaineb/Desktop/testoversampler_fact"

import os
# directory_path = 'C:/Users/zaineb/Desktop/facts'
directory_path = 'C:/Users/zaineb/Desktop/converted_notebooks_withfacts'
def get_files_queue(directory_path):
    files_queue = []

    try:
        files = os.listdir(directory_path)
    except OSError as e:
        print(f"Error reading directory: {e}")
        return None

    for file in files:
        files_queue.append(directory_path+'/'+file)

    return files_queue


