# =============================================================================
# BIBLIOTECAS E MÓDULOS
# =============================================================================

import dotenv, os
from ftplib import FTP
from src.download import download_arquivos
from src.transforma import extrai_arquivos

# =============================================================================
# CONSTANTES
# =============================================================================

# -----------------------------------------------------------------------------
# Variáveis de ambiente
# -----------------------------------------------------------------------------

dotenv.load_dotenv()
FTP_GOV_RAIZ = os.getenv("FTP_GOV_RAIZ")
FTP_RAIS = os.getenv("FTP_RAIS")

# =============================================================================
# FUNÇÕES
# =============================================================================

# -----------------------------------------------------------------------------
# Download
# -----------------------------------------------------------------------------


def fluxo_download() -> None:
    assert isinstance(FTP_GOV_RAIZ, str), "'FTP_GOV_RAIZ' NÃO ESTÁ NO ARQUIVO .env!"
    ftp = FTP(FTP_GOV_RAIZ)
    ftp.login()
    assert isinstance(FTP_RAIS, str), "'FTP_RAIS' NÃO ESTÁ NO ARQUIVO .env!"
    ftp.cwd(FTP_RAIS)
    diretorios_anos = (dir for dir in ftp.nlst())
    for diretorio in diretorios_anos:
        download_arquivos(ftp, diretorio)
    ftp.quit()
    return None


# =============================================================================
# CÓDIGO
# =============================================================================


def main() -> None:
    fluxo_download()
    extrai_arquivos()
    return None


if __name__ == "__main__":
    main()
