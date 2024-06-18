# =============================================================================
# BIBLIOTECAS E MÓDULOS
# =============================================================================

from ftplib import FTP
from pathlib import Path
import dotenv, os

# =============================================================================
# CONSTANTES
# =============================================================================

# -----------------------------------------------------------------------------
# Variáveis de ambiente
# -----------------------------------------------------------------------------

dotenv.load_dotenv()
DIR_DOWNLOAD = os.getenv("DIR_DOWNLOAD")
assert isinstance(DIR_DOWNLOAD, str), "'DIR_DOWNLOAD' NÃO ESTÁ NO ARQUIVO .env!"
DIR_DOWNLOAD = Path(DIR_DOWNLOAD)
DIR_DOWNLOAD.mkdir(parents=True, exist_ok=True)

# =============================================================================
# FUNÇÕES
# =============================================================================


def download_arquivos(ftp: FTP, diretorio_ano: str) -> None:
    def download_arquivo(arquivo_download: str) -> None:
        path_download = diretorio_download / arquivo_download

        if path_download.exists():
            return None

        with open(path_download, "wb") as download_f:
            ftp.retrbinary(f"RETR {arquivo_download}", download_f.write)

        return None

    ftp.cwd(diretorio_ano)

    assert isinstance(DIR_DOWNLOAD, Path)
    diretorio_download = DIR_DOWNLOAD / diretorio_ano
    diretorio_download.mkdir(parents=True, exist_ok=True)

    arquivos_download = (arq for arq in ftp.nlst() if ".7z" in arq)

    for arquivo in arquivos_download:
        download_arquivo(arquivo)

    ftp.cwd("..")

    return None
