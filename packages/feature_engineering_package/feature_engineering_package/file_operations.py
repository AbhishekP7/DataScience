#Read and write csv files from local storage
import pandas as pd
def local_read_csv_file(filepath):
    dataframe_read = pd.read_csv(filepath)
    print('\n\nREAD SUCESSFULL\nFROM: {}'.format(filepath))
    return dataframe_read

def local_write_as_csv_file(filepath, dataframe_write):
    dataframe_write.to_csv(filepath+'random_forest_classifier_output.csv', index=False)
    
    
#Read and write the trained model from the local storage
def local_write_trained_model(filepath, model):
    file =open(str(filepath)+'/model.pkl', 'wb')
    pickle.dump(model, file)
    file.close()
    print('SAVED THE MODEL SUCESSFULLY TO PATH:\n',filepath)

def local_read_trained_model(filepath):
    file = open(filepath, 'rb')
    obj = pickle.load(file)
    file.close()
    print('MODEL LOADED SUCESSFULLY FROM PATH:\n',filepath)
    return obj
