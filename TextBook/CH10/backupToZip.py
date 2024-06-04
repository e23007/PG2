#! python3
# backupToZip.py - ディレクトリ全体を連番付きZIPファイルにコピーする
import zipfile,os

def backup_to_zip(folder):
    #ディレクトリ全体をZIPファイルにバックアップする
    folder=os.path.abspath(folder)#folderを絶対パスにする
    #既存のファイル名からファイル名の連番を決める
    number=1
    while True:
        zip_filename=f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zip_filename):
            break
        number+=1
    #TODO:ZIPファイルを作成する
    print(f'Creating{zip_filename}')
    backup_zip=zipfile.ZipFile(zip_filename,'w')
    #TODO:ディレクトリのツリーを渡り歩いてその中のファイルを圧縮する
    new_base=os.path.basename(folder)+'-'
    for foldername,subfolders,filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        #現在のディレクトリをZIPファイルに追加する
        backup_zip.write(foldername)
        #現在のディレクトリの中の全ファイルをZIPファイルに追加する
        for filename in filenames:
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue#バックアップ用ZIPファイルはバックアップしない
            backup_zip.write(os.path.join(foldername,filename))
    backup_zip.close()
    print('Done')
#OSによって異なる Windowsは backup_to_zip('C:\\delicious')　
backup_to_zip(r'~/PG2/TextBook/CH10/delicious')
