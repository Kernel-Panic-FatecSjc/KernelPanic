def montar_query(filtros):
    if filtros.get("tipo") == "importação":
        tabela = "importacao"
    elif filtros.get("tipo") == "exportação":
        tabela = "exportacao"
    else:
        raise ValueError("Informe se é 'importação' ou 'exportação' no campo 'tipo'.")

    ano = filtros.get("ano")
    mes = filtros.get("mes")

    # Lógica de agrupamento
    if ano == "todos" and mes == "todos":
        agrupamento = "ano"
    elif ano != "todos" and mes == "todos":
        agrupamento = "mes"
    else:
        agrupamento = None

    select = "SELECT SUM(t.vl_fob_expt) AS total_valor_fob"
    if agrupamento == "ano":
        select += ", t.co_ano AS ano"
    elif agrupamento == "mes":
        select += ", t.co_mes AS mes"

    sql = f"""
        {select}
        FROM {tabela} t
        JOIN municipios m ON m.co_mun = t.co_mun
        JOIN pais p ON p.co_pais = t.co_pais
        JOIN sh ON sh.co_sh4 = t.co_sh4
    """

    condicoes = []
    valores = []

    if ano and ano != "todos":
        condicoes.append("t.co_ano = %s")
        valores.append(ano)

    if mes and mes != "todos":
        condicoes.append("t.co_mes = %s")
        valores.append(mes)

    if filtros.get("municipio") and filtros["municipio"] != "todos":
        condicoes.append("m.co_mun = %s")
        valores.append(filtros["municipio"])

    if filtros.get("ncm") and filtros["ncm"] != "todos":
        condicoes.append("t.co_sh4 = %s")
        valores.append(filtros["ncm"])

    if filtros.get("pais") and filtros["pais"] != "todos":
        condicoes.append("(p.co_pais = %s OR p.co_pais_isoa3 = %s OR p.no_pais = %s)")
        valores.extend([filtros["pais"]] * 3)

    if condicoes:
        sql += " WHERE " + " AND ".join(condicoes)

    if agrupamento == "ano":
        sql += " GROUP BY t.co_ano ORDER BY t.co_ano"
    elif agrupamento == "mes":
        sql += " GROUP BY t.co_mes ORDER BY t.co_mes"

    return sql, valores