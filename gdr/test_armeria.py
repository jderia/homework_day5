import pytest
from armeria import equipaggia_artefatto
@pytest.mark.parametrize("hp", [0, -1, -100])
def test_guerriero_caduto(hp):
    guerriero = {
        "hp": hp,
        "livello": 10,
        "classe": "guerriero",
        "allineamento": "neutro",
        "equipaggiamento": [],
    }
    artefatto = {
        "nome": "Spada",
        "livello_minimo": 5,
    }
    with pytest.raises(ValueError):
        equipaggia_artefatto(guerriero, artefatto)
@pytest.mark.parametrize("livello_guerriero, livello_minimo", [
(1,5),(4,5)])
def test_livello_troppo_basso(livello_guerriero, livello_minimo):
    guerriero = {
        "hp":100,
        "livello": livello_guerriero,
        "classe": "guerriero",
        "allineamento": "neutro",
        "equipaggiamento": [],
    }
    artefatto = {
        "nome": "Spada",
        "livello_minimo": livello_minimo,
    }
    with pytest.raises(ValueError):
            equipaggia_artefatto(guerriero, artefatto)

@pytest.mark.parametrize("classe_guerriero, classe_esclusiva", [
     ("mago", "guerriero"),
     ("ladro", "mago"),
])
def test_classe_esclusiva_sbagliata(classe_guerriero, classe_esclusiva):
     guerriero = {
          "hp": 100,
          "livello": 10,
          "classe": classe_guerriero,
          "allineamento": "neutro",
          "equipaggiamento":[],
     }
     artefatto = {
          "nome": "Spada",
          "livello_minimo": 1,
          "classe_esclusiva": classe_esclusiva,
     }
     with pytest.raises(PermissionError):
          equipaggia_artefatto(guerriero,artefatto)

def test_artefatto_maledetto():
     guerriero = {
          "hp": 100,
          "livello": 10,
          "classe": "guerriero",
          "allineamento": "buono",
          "equipaggiamento": [],
     }
     artefatto = {
          "nome": "Spada Oscura",
          "livello_minimo": 1,
          "maledetto": True,
     }
     risultato = equipaggia_artefatto(guerriero, artefatto)
     assert risultato == "L'artefatto brucia! Equipaggiamento fallito."

def test_happy_path():
    guerriero = {
          "hp": 100,
          "livello": 10,
          "classe": "guerriero",
          "allineamento": "neutro",
          "equipaggiamento":[],
     }
    artefatto = {
         "nome": "Spada",
         "livello_minimo": 1,
    }
    risultato = equipaggia_artefatto(guerriero, artefatto)
    assert risultato == "Spada equipaggiato con successo."

     
     