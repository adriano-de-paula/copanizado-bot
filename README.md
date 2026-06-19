# 🏆 Copanizado Bot - Notificador da Copa do Mundo ⚽

O **Copanizado Bot** é uma automação em Python desenvolvida para monitorizar os jogos do dia da Copa do Mundo FIFA 2026 e enviar a agenda de partidas formatada diretamente para um canal ou chat privado do Telegram.

---

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **Requests:** Para consumo de APIs HTTP.
* **Python-dotenv:** Para gestão segura de credenciais através de variáveis de ambiente.
* **API-Football (API-Sports):** Fonte oficial de dados em tempo real sobre os jogos.
* **Telegram Bot API:** Integração e envio automatizado de mensagens.

---

## 🔒 Segurança das Chaves (Boas Práticas)

Este projeto foi estruturado seguindo as melhores práticas de segurança do mercado. Todas as chaves de API e tokens do Telegram ficam armazenados num ficheiro local `.env`, o qual está listado no `.gitignore` para garantir que dados sensíveis nunca fiquem expostos publicamente no GitHub.

---

## 🛠️ Como Executar o Projeto Localmente

1. **Clona o repositório:**
   ```bash
     git clone https://github.com/adriano-de-paula/copanizado-bot.git
   ```
---

2. **Instala as dependências necessárias:**
```bash
py -m pip install requests python-dotenv
```

---

3. **Configura as tuas credenciais:**
Cria um ficheiro chamado `.env` na raiz do projeto e adiciona os teus tokens:
```env
TELEGRAM_TOKEN="O_TEU_TOKEN_DO_TELEGRAM"
TELEGRAM_CHAT_ID="O_TEU_CHAT_ID"
APISPORTS_KEY="A_TUA_CHAVE_DA_API_SPORTS"
```
---

4. **Executa o bot:**
```bash
py notificador_copa.py
```

---

## 🔑 Como Obter as Credenciais

Para colocar o bot a funcionar, precisas de configurar 3 chaves no teu ficheiro `.env`. Segue o passo a passo para obter cada uma:

### 1. Token do Bot (Telegram)
O token autoriza o teu script Python a enviar mensagens em nome do teu bot.
1. No Telegram, pesquisa por **`@BotFather`** (o bot oficial de criação).
2. Envia o comando `/newbot` e escolhe um nome e um utilizador para o teu bot (ex: `Estou Copanizado`).
3. O `@BotFather` vai gerar uma mensagem com o teu **Token de Acesso** (uma sequência longa de letras e números). Copia e guarda esse valor.
4. **Importante:** Procura pelo bot que criaste no Telegram e clica em **"Começar"** (`/start`) para o autorizares a falar contigo.

### 2. Chat ID (Telegram)
O Chat ID identifica a tua conta ou o canal específico para onde o bot deve enviar os alertas.
1. No Telegram, pesquisa por **`@userinfobot`**.
2. Clica em **"Começar"** (`/start`).
3. Ele vai responder imediatamente com o teu `Id` (um número longo de 9 ou 10 dígitos). Copia esse número.

### 3. Chave da API de Futebol (API-Sports)
Esta chave permite que o teu código consuma os dados reais e atualizados da Copa do Mundo.
1. Acede ao painel oficial em [dashboard.api-football.com](https://dashboard.api-football.com/) e cria uma conta gratuita.
2. No menu lateral esquerdo, acede a **Account ➔ My Access**.
3. No canto superior direito da página, verás o campo **API-KEY** com a tua chave secreta. Copia esse código completo.






