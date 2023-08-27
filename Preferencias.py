preferencias = {
    "Deportes": {
        "Futbol":["Liga MX","MLS","Premiere League", "Champions League"],
        "Basquetbol":["NBA","WNBA","Euroliga","Liga ACB","NCAA"],
        "Americano":["NFL","LFA","ONEFA"]
    },
    "Ferias":{
        "Libros":["Fantasia","Romance","Ficcion","Misterio","Memoria","Autoayuda"],
        "Vinos":["Tinto","Blanco","Rosado","Espumoso","Generoso"],
        "Estatales":["FNSM","FENAZA","Guelaguetza"]
    },
    "Musica":{
        "Conciertos":["Rock","Sinfonica","Pop","Balada","Opera"],
        "Festivales":["Pal`Norte","Corona Capital","Tomorrowland"],
        "Bailes":["Banda","Norteño","Sierreño"]
    }
}
def imprimir (nombre: str, categoria: str):
    for evento, cat in preferencias.items():
        if evento == nombre:
            for cat, subcat in preferencias[nombre].items():
                if cat == categoria:
                    return ("{}: {}: {}".format(evento, categoria,list(subcat)))
