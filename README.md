#  STATUS DE PRODUÇÃO

## 🔨 FAZENDO

- Código de empilhamento dos dados

## ✅ CONCLUÍDO

- Código de download
- Código de extração dos arquivos

## 📝 A FAZER

### BACKLOG

- Códigos de testes

### 💡 IDEIAS

- **REFAZER DOWNLOAD PARA UM ARQUIVO CORROMPIDO**

Dá para dizer se está corrompido ou não durante a extração do .7z no código de transformação

> 1. Deu erro -> joga nome do arquivo no `log/arquivos_corrompidos.log`
> 2. Ter um código `conserta_corrompidos.py`, algo do tipo que
>   - Faz o download e tenta extrair
>       - SUCESSO: retira a linha do log
>       - FRACASSO: mantém a linha no log

-  **TER UM CÓDIGO QUE VERIFICA SE O DOWNLOAD FOI CONCLUÍDO**

> Checa a cada 5s para ver se o tamanho está mudando
>     - SE SIM: download ainda em andamento
>     - SE NÃO: download terminou
