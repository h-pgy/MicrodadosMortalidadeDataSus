class SIMDownloader:
    '''Baixa arquivos de D.O.  do SIM filtrando para Estado e/ou ano'''

    def __init__(self, sus_downloader=None):

        self.datasus = sus_downloader or DataSusDownloader()

    def go_to_sim(self):

        self.datasus.cwd('/dissemin/publicos/SIM/CID10/DORES')

    def filter_files(self, estado=None, ano=None):

        if estado:
            estado = estado.strip().upper()
            estado = lambda x: x[2:4] == estado
        else:
            estado = lambda x: True
        if ano:
            ano = str(ano).strip()
            ano = lambda x: x[4:8] == ano
        else:
            ano = lambda x: True

        files = self.datasus.listfiles()

        return [file for file in files if estado(file) and ano(file)]

    def download_files(self, file_list, file_dir='SIM_SP'):

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for file in files:
            self.datasus.download(file, file_dir)