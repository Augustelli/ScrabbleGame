import json

with open('modelsNew/config.json', 'r') as f:
    config_data = json.load(f)

cantidad_letras = config_data['cantidad_letras']
cantidad_fichas = config_data['cantidad_letras']
cantidad_de_fichas_por_letra = config_data['cantidad_de_fichas_por_letra']
puntaje_por_letra = config_data['valores_letras']
cantidad_fichar_jugador = config_data['cantidad_fichas_jugador']
coordenadas_multiplicadores = config_data['coordenadas_multiplicadores']
colores_multiplicadores = config_data['colores_multiplicadores']
multiplicadores_valores = config_data['multiplicadores_valores']
cantidad_multiplicadores = config_data['cantidad_multiplicadores']
