import os
import subprocess

class DbcDbfConverter:
    '''Converte arquivos .dbf do DataSus para .dbc - tem o R como dependency'''
    
    def __init__(self, r_path = None):
        
        self.r_path = r_path or r'C:\Program Files\R\R-3.6.3\bin\Rscript.exe'

    def __aux_format_paths(self, input_path, output_path, r_path):

        input_path = input_path.replace('\\', '\\\\')
        output_path = output_path.replace('\\', '\\\\')
        format_path = lambda x: r'"{}"'.format(x)

        input_path, output_path, r_path = map(format_path, [input_path, output_path, r_path])

        return input_path, output_path, r_path

    def __aux_gen_script(self, input_path, output_path):

        script = f'''
        #checking for package
        if (!require("read.dbc")) install.packages("read.dbc")

        file.create({output_path})
        # The call return logi = TRUE on success
        if( dbc2dbf(input.file = {input_path}, output.file = {output_path}) ) {{
             print("File decompressed!")
        }}'''

        return script

    def read_dbc_r(self, input_path, output_path, r_path):
        '''All strings must be passed as raw strings!'''

        input_path, output_path, r_path  = self.__aux_format_paths(input_path, output_path, r_path)

        script = self.__aux_gen_script(input_path, output_path)

        with open('script.r', 'w') as f: #cria file temporario de script
            f.write(script)
        path_script = os.path.abspath('script.r')
        path_script = f'"{path_script}"'

        comand = f"{r_path} {path_script}"    
        out = subprocess.run(comand, shell = True, capture_output=True)
        os.remove('script.r')
        
        print(out)
    
    def __call__(self, input_path, output_path):
        
        self.read_dbc_r(input_path, output_path, self.r_path)