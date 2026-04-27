def equipaggia_artefatto(guerriero: dict, artefatto: dict) -> str:
    """Logica di equipaggiamento per un personaggio GDR."""

    if guerriero.get("hp", 0) <= 0:
        raise ValueError("Un guerriero caduto non può equipaggiare oggetti.")

    if guerriero["livello"] < artefatto["livello_minimo"]:
        raise ValueError(f"Livello troppo basso. Richiesto: {artefatto['livello_minimo']}")

    if artefatto.get("classe_esclusiva") and guerriero["classe"] != artefatto["classe_esclusiva"]:
        raise PermissionError(f"Questo oggetto è riservato alla classe {artefatto['classe_esclusiva']}.")

    if artefatto.get("maledetto", False) and guerriero["allineamento"] == "buono":
        return "L'artefatto brucia! Equipaggiamento fallito."

    guerriero["equipaggiamento"].append(artefatto["nome"])
    return f"{artefatto['nome']} equipaggiato con successo."