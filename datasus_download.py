import os
from dbc_converter import DbcDbfConverter
from ftplib import FTP

class DataSusDownloader:
    '''Realiza download de dados do DataSus por FTP'''

    
    def __init__(self, converter = None):
        
        self.converter = converter or DbcDbfConverter()
        self.ftp = FTP('ftp.datasus.gov.br')
        self.__init_ftp()
        
    def __init_ftp(self):
        
        self.ftp.connect()
        self.ftp.login()
        
    def dir_(self):
        
        return self.ftp.dir()
    
    def cwd(self, dir_):
        
        self.ftp.cwd(dir_)
    
    def listfiles(self):
        
        return self.ftp.nlst()
    
    def pwd(self):
        
        print(self.ftp.pwd())
    
    def _solve_fpath(self, file_directory, fname):
        
        if file_directory:
            if not os.path.exists(file_directory):
                os.makedirs(file_directory)
            save_path = os.path.join(file_directory, fname)
        else:
            save_path = fname
            
        return save_path
    
    def _return_content(self, save_path):
        
        with open(out_name, 'rb') as out_f:
                content = out_f.read()
        return content
        
    def _convert_dbc(self, save_path):
        
        self.converter(os.path.abspath(save_path), 
                        os.path.abspath(save_path.replace('.dbc', '.dbf')))
        
    def _save_dbc_ftp(self, save_path, fname_in_ftp):
        
        out_f = open(save_path, 'wb')
        self.ftp.retrbinary('RETR {}'.format(fname_in_ftp), 
                            out_f.write)
        out_f.close()
        
        
    def download(self, fname, file_directory, return_content = False, converter = True, delete_dbc = True):
        
        save_path = self._solve_fpath(file_directory, fname)
        
        self._save_dbc_ftp(save_path, fname)
        
        if converter: self._convert_dbc(save_path)
            
        if return_content: self._return_content(save_path)
            
        if delete_dbc: os.remove(save_path)
            
        