import re
from utilities.DirectoryGrab import DirGrab
import pandas as pd
import os


def FilterbyWord(filterWord = None,df1 = None, columnName = None) -> pd.DataFrame:
    if filter is None:
        raise Exception('Filter parameter not passed')
    if df1 is None:
        raise Exception('Dataframe paramater not passed')
    if columnName is None:
        raise Exception('Column name paramater not passed')
    lister = df1[columnName].tolist()
    unique_list = []
    for x in lister:
        if x not in unique_list and isinstance(x, str):
            unique_list.append(x)
    filter_list = []
    for each in unique_list:
        if re.match(r"[\S]*{}[\S]*".format(filterWord), each.lower()):
            filter_list.append(each)
    # print(filter_list)
    # print(df1.head())
    df_list = []
    for each in filter_list:
        temp_df = df1.loc[df1[columnName] == each]
        temp_df = temp_df.reset_index(drop=True)
        df_list.append(temp_df)
    vertical_stack = pd.concat(df_list,axis=0,ignore_index=True)
    return vertical_stack

    '''
    intended for executing the same operation across multiple identical excel files
    '''
def work(filter_word = 'math',path = '/Users/idky/PycharmProjects/Fall2019/documents/AllStateFiles', ):
    grabber = DirGrab(path)
    grabber.grabByExtension(".xls", False)
    lista = grabber.getter()
    count = 2012
    for each in lista:
        xls = pd.ExcelFile(each)
        df1 = pd.read_excel(xls,4)
        filtered_df = FilterbyWord(filterWord=filter_word,df1=df1,columnName='OtherSpecify')
        save_folder = '{}/alteredFiles/{}/'.format(path,filter_word)
        ensure_dir(save_folder)
        save_file = "{}/alteredFiles/{}/AllState_{}_{}.xlsx".format(path,filter_word,filter_word,count)
        count = count + 1
        filtered_df.to_excel(save_file)
    return None

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def __main__():
    '''
    path = "/Users/idky/PycharmProjects/Fall2019/documents/AllStateFiles/"
    grabber = DirGrab(path)
    grabber.grabByExtension(".xls",False)
    lista = grabber.getter()
    StateFile = "/Users/idky/PycharmProjects/Fall2019/documents/AllStateFiles/AllStates-2018.xls"  # FilePath
    xls = pd.ExcelFile(StateFile)  # read excel sheet into program
    df1 = pd.read_excel(xls, 4)  # read sheet 6 from excel sheet
    filtered_df = FilterbyWord(filterWord='math',df1=df1,columnName='OtherSpecify')
    save_file = "/Users/idky/PycharmProjects/Fall2019/documents/AllStateFiles/alteredFiles/AllState2018altered.xlsx"
    filtered_df.to_excel(save_file)
    '''
    work(path='/Users/idky/PycharmProjects/Fall2019/documents/AllStateFiles')

if __name__ == "__main__":
    __main__()