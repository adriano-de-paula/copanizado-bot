import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# ================= CONFIGURAÇÕES SEGURAS =================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
APISPORTS_KEY = os.getenv("APISPORTS_KEY")
# =========================================================

def buscar_jogos_copa():
    """Busca todos os jogos de hoje e filtra os da Copa do Mundo"""
    url = "https://v3.football.api-sports.io/fixtures"
    
    hoje = datetime.now().strftime("%Y-%m-%d")
    
    # Buscamos todos os jogos do dia de hoje usando o fuso de Brasília
    querystring = {
        "date": hoje,
        "timezone": "America/Sao_Paulo"
    }
    
    headers = {
        "x-apisports-key": APISPORTS_KEY
    }
    
    try:
        resposta = requests.get(url, headers=headers, params=querystring)
        dados = resposta.json()
        
        todos_os_jogos = dados.get("response", [])
        print(f"Total de jogos encontrados hoje no mundo: {len(todos_os_jogos)}")
        
        # Filtramos apenas os jogos onde o nome do campeonato contém 'World Cup' ou 'Copa do Mundo'
        jogos_copa = []
        for jogo in todos_os_jogos:
            nome_liga = jogo.get("league", {}).get("name", "")
            if "World Cup" in nome_liga or "Copa do Mundo" in nome_liga:
                jogos_copa.append(jogo)
                
        print(f"Jogos filtrados da Copa: {len(jogos_copa)}")
        return jogos_copa
        
    except Exception as e:
        print(f"Erro ao buscar jogos: {e}")
        return []

def enviar_mensagem_telegram(texto):
    """Envia a mensagem formatada para o Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

# --- FLUXO PRINCIPAL ---
print("Buscando jogos da Copa do Mundo hoje...")
jogos = buscar_jogos_copa()

if not jogos:
    mensagem = "🏆 *Estou Copanizado Bot*\n\nNenhum jogo da Copa do Mundo agendado para a data de hoje."
else:
    mensagem = "🏆 *JOGOS DE HOJE NA COPA DO MUNDO!* ⚽\n\n"
    
    for jogo in jogos:
        time_casa = jogo["teams"]["home"]["name"]
        time_fora = jogo["teams"]["away"]["name"]
        
        # Horário formatado
        data_completa = jogo["fixture"]["date"] 
        horario = data_completa.split("T")[1][:5]
        
        # Placar e Status
        status = jogo["fixture"]["status"]["short"] 
        gols_casa = jogo["goals"]["home"]
        gols_fora = jogo["goals"]["away"]
        
        if status == "NS":
            mensagem += f"• *{time_casa}* vs *{time_fora}*\n⏰ Horário: {horario} (Horário de Brasília)\n\n"
        else:
            gols_casa = gols_casa if gols_casa is not None else 0
            gols_fora = gols_fora if gols_fora is not None else 0
            mensagem += f"• *{time_casa}* {gols_casa} x {gols_fora} *{time_fora}*\n🔄 Status: {status} ({horario})\n\n"

print("Enviando para o Telegram...")
enviar_mensagem_telegram(mensagem)
print("Pronto!")