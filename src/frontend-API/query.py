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
            SUM(t.vl_fob_expt) AS total_valor_fob,
            SUM(t.kg_liquido_expt) AS total_kg_liquido,
            (SUM(t.vl_fob_expt) / NULLIF(SUM(t.kg_liquido_expt), 0)) AS valor_por_kg,
            COUNT(*) AS total_registros
        FROM {tabela} t
        JOIN sh ON sh.co_sh4 = t.co_sh4
        JOIN municipios m ON m.co_mun = t.co_mun
        JOIN pais p ON p.co_pais = t.co_pais
    """

    condicoes = []
    valores = []

    if (ano := filtros.get("ano")) and ano != "todos":
        condicoes.append(f"t.co_ano = {ano}")

    if (mes := filtros.get("mes")) and mes != "todos":
        condicoes.append(f"t.co_mes = {mes}")

    if (municipio := filtros.get("municipio")) and municipio != "todos":
        condicoes.append(f"m.co_mun = {municipio}")

    if (pais := filtros.get("pais")) and pais != "todos":
        condicoes.append(f"(p.co_pais = {pais} OR p.co_pais_isoa3 = '{pais}' OR p.no_pais = '{pais}')")

    if condicoes:
        sql += " WHERE " + " AND ".join(condicoes)

    sql += " GROUP BY t.co_sh4, sh.no_sh4_por HAVING SUM(t.kg_liquido_expt) > 0 "

    # Critério de ordenação
    criterio = filtros.get("metrica", "valor_agregado")  
    if criterio == "valor_agregado":
        ordem = "valor_por_kg DESC"
    elif criterio == "valor_FOB":
        ordem = "total_valor_fob DESC"
    elif criterio == "total_registros":
        ordem = "total_registros DESC"
    elif criterio == "total_kg_liquido":
        ordem = "total_kg_liquido DESC"
    else:
        raise ValueError("Critério inválido. Use: valor_agregado, valor_fob, quantidade ou kg.")

    sql += f" ORDER BY {ordem} LIMIT 5"

    return sql, valores

