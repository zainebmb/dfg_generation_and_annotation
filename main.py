import utils
import Overlap_preproc_leak_dfg
import get_models_data
import annotation
import os

facts_folders=utils.get_files_queue(utils.directory_path)
if facts_folders:
    for folder in facts_folders:
        print("working on "+ folder)
        models_with_data = get_models_data.get_models_withdata(folder)
        if models_with_data:
            Overlap_preproc_leak_dfg.create_model_subgraphs(folder,models_with_data)


            models_graph_path=folder+'/models_graphs'
            file_names = os.listdir(models_graph_path)

            input_files = [file for file in file_names if os.path.isfile(os.path.join(models_graph_path, file)) and "label" not in file]  # only files (not directories) and file should not be recreated


            invos_with_preproc_leak = annotation.extract_preproc_leak_column(folder+'/Telemetry_FinalPreProcessingLeak.csv')
            invos_with_overlap_leak = annotation.extract_overlap_leak_column(folder+'/FinalOverlapLeak.csv')
            for input_file in input_files:
                annotation.create_label_file(models_graph_path+'/'+input_file, invos_with_preproc_leak, invos_with_overlap_leak)
        else:
            pass


