def montar_query(filtros):
    if filtros.get("tipo") == "importacao":
        tabela = "importacao"
    elif filtros.get("tipo") == "exportacao":
        tabela = "exportacao"
    else:
        raise ValueError("Informe se é 'importação' ou 'exportação' no campo 'tipo'.")

    ano = filtros.get("ano")
    mes = filtros.get("mes")

    if ano != "todos" and mes == "todos":
        agrupamento = "mes" 
    elif ano == "todos" and mes == "todos":
        agrupamento = "ano" 
    elif ano != "todos" and mes != "todos":
        agrupamento = "mes"  
    else:
        agrupamento = None

    select = """
        SELECT 
            SUM(t.kg_liquido_expt) as total_kg_liquido,
            SUM(t.vl_fob_expt) AS total_valor_fob,
            COUNT(*) AS total_registros
        """
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

def montar_query_top5(filtros):
    if filtros.get("tipo") == "importacao":
        tabela = "importacao"
    elif filtros.get("tipo") == "exportacao":
        tabela = "exportacao"
    else:
        raise ValueError("Informe se é 'importação' ou 'exportação' no campo 'tipo'.")

    sql = f"""
        SELECT 
            t.co_sh4 AS codigo_ncm,
            sh.no_sh4_por AS nome_produto,
            t.co_ano AS ano,
            t.co_mes AS mes,
            t.valor_agregado AS total_valor_agregado,
            SUM(t.kg_liquido_expt) as total_kg_liquido,
            SUM(t.vl_fob_expt) AS total_valor_fob,
            COUNT(*) AS total_registros
        FROM {tabela} t
        JOIN sh ON sh.co_sh4 = t.co_sh4
        JOIN municipios m ON m.co_mun = t.co_mun
        JOIN pais p ON p.co_pais = t.co_pais
    """

    condicoes = []
    valores = []


    ano = filtros.get("ano")
    if ano is not None and ano != "" and ano != "todos":
        condicoes.append("t.co_ano = %s")
        valores.append(int(ano))

    mes = filtros.get("mes")
    if mes is not None and mes != "" and mes != "todos":
        condicoes.append("t.co_mes = %s")
        valores.append(int(mes))


    if filtros.get("municipio") and filtros["municipio"] != "todos":
        condicoes.append("m.co_mun = %s")
        valores.append(filtros["municipio"])

    if filtros.get("pais") and filtros["pais"] != "todos":
        condicoes.append("(p.co_pais = %s OR p.co_pais_isoa3 = %s OR p.no_pais = %s)")
        valores.extend([filtros["pais"]] * 3)

    if condicoes:
        sql += " WHERE " + " AND ".join(condicoes)

    if filtros.get("metrica") == "valor_FOB":
        metrica = "total_valor_fob"
    elif filtros.get("metrica") == "valor_agregado":
        metrica = "total_valor_agregado"
    elif filtros.get("metrica") == "total_registros":
        metrica = "total_registros"
    elif filtros.get("metrica") == "total_kg_liquido":
        metrica = "total_kg_liquido"
    else:
        raise ValueError("Métrica inválida ou não informada.")

    sql += f""" 
        GROUP BY t.co_sh4, sh.no_sh4_por
        ORDER BY {metrica} DESC
        LIMIT 5
    """

    return sql, valores


