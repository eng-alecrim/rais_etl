from ftplib import FTP
from src.download import *

def main() -> None:

    ftp = FTP(FTP_GOV_RAIZ)
    ftp.login()
    ftp.cwd(FTP_RAIS)
    diretorios_anos = (dir for dir in ftp.nlst())
    for diretorio in diretorios_anos:
        download_arquivos(ftp,diretorio)
    ftp.quit()

    return None

if __name__ == "__main__":
    main()
