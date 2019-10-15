import re
from utilities.DirectoryGrab import DirGrab
import pandas as pd
import os

'''
Method: TransOPPathOperations_V1:
Description: FIle management method for cross platform python developement
Author: Alex Mensen-Johnson
Returns: a folder path to the AllStateFilesPath within the Fall2019 python
'''
def TransOPPathOperations():
    print('running TransOperations...')
    try:
        dirname = os.path.dirname(__file__)
        os.chdir(dirname)
    except OSError:
        print('couldnt change directory name')
    dirpath = os.getcwd()
    stringlist = dirpath.split('/')
    stringlist.pop((len(stringlist)-1))
    stringlist.append('documents')
    stringlist.append('AllStateFiles')
    filepath = ''
    if os.name == 'nt':
        for string in stringlist:
            filepath = '{}{}\{}'.format(filepath,string,'')
    else:
        for string in stringlist:
            filepath = '{}{}/'.format(filepath,string)
    filepath = filepath[0:-1]
    return filepath

'''
Method: FilterbyWord_v1
Author: Alex Mensen-Johnson
Params: filter word = the filter word, df1 = data frame 1,columnName = the column containing targert values
Description: in takes a filter word, a column name and a dataframe and pulls
all values from that column that contain a matching string to the filterword.


'''
def FilterbyWord(filterWord = None,df1 = None, columnName = None) -> pd.DataFrame:
    if filter is None:
        raise Exception('Filter parameter not passed')
    if df1 is None:
        raise Exception('Dataframe parameter not passed')
    if columnName is None:
        raise Exception('Column name parameter not passed')
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
Method: Work_v1
Author: Alex Mensen-Johnson
Params: filter word: target word for filtering, path = AllStateFiles Directory
Description: Method for executing filterByWord across multiple excel files
'''
def work(filter_word = 'math',path = TransOPPathOperations() ):
    print('running work....')
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
'''
Method: KeyWordMaker_v1
Author: Alex Mensen-Johnson
Params: file_name: file name for 7 text files to be stored inside the distinct
names directory
'''
def KeyWordMaker(file_name = 'your_file_path.txt'):
    path = TransOPPathOperations()
    grabber = DirGrab(path)
    grabber.grabByExtension('.xls',False)
    file_list = grabber.getter()
    descript_list = []
    uniquelist = []
    keywordlist = []
    txtfile = ''

    if os.name == 'nt':
        ensure_dir('{}\distinctNames'.format(path))
        txtfile = '\distinctNames\OtherSpecify'
    else:
        ensure_dir('{}/distinctNames'.format(path))
        txtfile = '/distinctNames/OtherSpecify'
    year = 2012
    for xls in file_list:
        descript_list = []
        uniquelist = []
        big_excel = pd.ExcelFile(xls)
        df1 = pd.read_excel(big_excel,4)
        descript_list = df1['OtherSpecify'].tolist()
        full_file = '{}{}{}.txt'.format(path,txtfile,str(year))
        year = year + 1
        for descript in descript_list:
            if descript not in uniquelist:
                uniquelist.append(descript)

        file = open(full_file,'w+')
        for value in uniquelist:
            file.write(str(value) + '\n')
        file.close()
        print(full_file)


'''
Method: ensure_dir_v1
Author: Alex Mensen-Johnson, Open Source
Params: file_path: target directory to be created
Description: Force creates target directory if the directory doesnt already exist
'''
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

#hardcode Variables
PATH = TransOPPathOperations()
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

    # work(path='/Users/idky/PycharmProjects/Fall2019/documents/AllStateFiles')
    # KeyWordMaker()
    TransOPPathOperations()
if __name__ == "__main__":
    __main__()