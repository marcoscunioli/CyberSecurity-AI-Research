import re

def dlp_filter(ai_response):
    """
    Filtro de Prevención de Fuga de Información (DLP).
    Busca patrones de Tarjetas de Crédito o IDs antes de mostrar la respuesta.
    """
    # Patrón simple para detectar números que parecen tarjetas de crédito
    credit_card_pattern = r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
    
    if re.search(credit_card_pattern, ai_response):
        return "[BLOQUEADO] La respuesta contenía información sensible (PII)."
    return ai_response

# Simulación
ai_output = "Claro, los datos de la tarjeta del cliente son 4545-1234-5678-9012"
print(dlp_filter(ai_output))
