# =============================================================================
# BIBLIOTECAS E MÓDULOS
# =============================================================================

import dotenv, os
from pathlib import Path
import py7zr

# =============================================================================
# CONSTANTES
# =============================================================================

# -----------------------------------------------------------------------------
# Variáveis de ambiente
# -----------------------------------------------------------------------------

dotenv.load_dotenv()
DIR_DOWNLOAD = os.getenv("DIR_DOWNLOAD")
assert isinstance(DIR_DOWNLOAD, str)
DIR_DOWNLOAD = Path(DIR_DOWNLOAD)

# =============================================================================
# FUNÇÕES
# =============================================================================


def extrai_arquivo_7z(file_path, output_dir):
    with py7zr.SevenZipFile(file_path, mode="r") as z:
        z.extractall(path=output_dir)


def ja_foi_extraido(diretorio: Path, nome_arquivo: str) -> bool:
    if len(list(diretorio.rglob(f"*{nome_arquivo}*"))) > 0:
        return True
    return False


def extrai_arquivos() -> None:
    assert isinstance(DIR_DOWNLOAD, Path)
    arquivos_7z = DIR_DOWNLOAD.rglob("*.7z")

    for arq in arquivos_7z:
        print(f"> Extraindo {arq.name} . . .")
        diretorio_destino = Path(str(arq.parent).replace("zip", "txt"))
        diretorio_destino.mkdir(parents=True, exist_ok=True)

        if ja_foi_extraido(diretorio_destino, str(arq.stem)):
            print("\t> Já foi extraído!\n")
            continue

        print(f"\t> {arq.parent} -> {diretorio_destino}")

        try:
            extrai_arquivo_7z(arq, diretorio_destino)
        except:
            print(f"\t> {arq} ESTÁ CORROMPIDO!")
            continue

        print("\t> Concluído!\n")
    return None
