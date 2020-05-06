#script para baixar todos arquivos de SP


def download_all_sp(sim_downloader, file_dir='SIM_SP'):
    sim_downloader.go_to_sim()
    files_sp = sim_downloader.filter_files(estado='sp')
    sim_downloader.download_files(files_sp, file_dir)

if __name__ == "__main__":

    from sim_download import SIMDownloader

    sim_downloader = SIMDownloader()

    download_all_sp(sim_downloader)