def montar_query(filtros):
    if filtros.get("tipo") == "importação":
        tabela = "importação"
    elif filtros.get("tipo") == "exportação":
        tabela = "exportação"
    else:
        raise ValueError("Informe se é 'importação' ou 'exportação' no campo 'tipo'.")

    sql = f"SELECT * FROM {tabela} "
    sql += "JOIN municipios m ON m.co_mun = " + tabela + ".co_mun "
    sql += "JOIN pais p ON p.co_pais = " + tabela + ".co_pais "
    sql += "JOIN sh ON sh.co_ncm = " + tabela + ".co_ncm "

    condicoes = []
    valores = []

    if "ano" in filtros:
        condicoes.append(f"{tabela}.co_ano = %s")
        valores.append(filtros["ano"])

    if "mes" in filtros:
        condicoes.append(f"{tabela}.co_mes = %s")
        valores.append(filtros["mes"])

    if "municipio" in filtros:
        condicoes.append("m.nome_mun = %s")
        valores.append(filtros["municipio"])

    if "ncm" in filtros:
        condicoes.append(f"{tabela}.co_ncm = %s")
        valores.append(filtros["ncm"])

    if "pais" in filtros:
        condicoes.append("(p.co_pais = %s OR p.co_pais_iso3 = %s OR p.no_pais_isoa = %s)")
        valores.extend([filtros["pais"]] * 3)  

    if condicoes:
        sql += "WHERE " + " AND ".join(condicoes)

    return sql, valores

filtros = {
    "tipo": "exportação",
    "ano": 2023,
    "municipio": "São Paulo",
    "ncm": 10019010,
    "pais": "BRA"
}

query, params = montar_query(filtros)

print("SQL:", query)
print("Parâmetros:", params)

