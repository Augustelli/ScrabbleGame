import json

with open('game/modelsNew/config.json', 'r') as f:
    config_data = json.load(f)

cantidad_de_fichas_por_letra = config_data['cantidad_de_fichas_por_letra']
puntaje_por_letra = config_data['valores_letras']
coordenadas_multiplicadores = config_data['coordenadas_multiplicadores']
multiplicadores_valores = config_data['multiplicadores_valores']
