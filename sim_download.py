from datasus_download import DataSusDownloader
import os

class SIMDownloader:
    '''Baixa arquivos de D.O.  do SIM filtrando para Estado e/ou ano'''

    def __init__(self, sus_downloader=None):

        self.datasus = sus_downloader or DataSusDownloader()

    def go_to_sim(self):

        self.datasus.cwd('/dissemin/publicos/SIM/CID10/DORES')

    def filter_files(self, estado=None, ano=None):

        files = self.datasus.listfiles()

        if estado:
            estado = estado.upper()
            files = [file for file in files if file[2:4] == estado]

        if ano:
            ano = str(ano)
            files = [file for file in files if file[4:8] == ano]

        return files

    def download_files(self, file_list, file_dir):

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for file in file_list:
            self.datasus.download(file, file_dir)