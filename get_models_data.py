import pandas as pd

def get_models_withdata(facts_folder):
    Model_data_file_path = facts_folder + '/Telemetry_ModelPair.csv'
    models = []
    #handle cases where code file does not contain any models
    try: 
        data = pd.read_csv(Model_data_file_path, delimiter='\t', header=None)
        
        for index, row in data.iterrows():
            model = {
                'Model': row[0],
                'training_data': row[1],
                'training_method': row[3].split('.')[1],
                'training_ctx': row[4],
                'eval_data': row[6],
                'eval_method': row[8].split('.')[1],
                'train_and_eval_invo': row[2] + '_' + row[7],
                'eval_ctx': row[9]
            }
            models.append(model)
    except pd.errors.EmptyDataError:
        print("This file does not contain models and will be skipped.") # return empty list if code file doesnt contain models

    return models
# models_with_data= get_models_withdata('C:/Users/zaineb/Desktop/converted_notebooks_withfacts/2021-09-30-nb_619-fact')
# # print(get_models_withdata('C:/Users/zaineb/Desktop/converted_notebooks_withfacts/2021-09-30-nb_619-fact'))
# for m in models_with_data:
#     print (m)