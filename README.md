# MicrodadosMortalidadeDataSus


Ferramenta desenvolvida para extração dos dados do SIM (Sistema de Informações sobre Mortalidade) do DataSus.

Essa ferramenta faz uso do FTP  do DataSus para extrair os dados em .dbf e, utilizando um pacote desenvolvido para o R, converte esses arquivos para .dbc.

Também estão presentes ferramentas para conversão dos .dbcs para .csvs.

Adicionamos um python notebook que faz a leitura e seleção dos arquivos para uso da PMSP (filtrando os óbitos para municipio de São Paulo).

## Dependencies:
* linguagem R instalada no PC
