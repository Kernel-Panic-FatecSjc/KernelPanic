def montar_query(filtros):
    if filtros.get("tipo") == "importação":
        tabela = "importacao"
    elif filtros.get("tipo") == "exportação":
        tabela = "exportacao"
    else:
        raise ValueError("Informe se é 'importação' ou 'exportação' no campo 'tipo'.")

    # Verifica se vai agrupar por mês
    agrupar_por_mes = "mes" not in filtros

    select_base = """
        SELECT 
            SUM(t.valor_agregado) AS total_valor_agregado,
            SUM(t.kg_liquido_expt) AS total_kg_liquido,
            SUM(t.vl_fob_expt) AS total_valor_fob,
            COUNT(*) AS total_registros
    """
    if agrupar_por_mes:
        select_base += ", t.co_mes AS mes"

    sql = f"""
        {select_base}
        FROM {tabela} t
        JOIN municipios m ON m.co_mun = t.co_mun
        JOIN pais p ON p.co_pais = t.co_pais
        JOIN sh ON sh.co_sh4 = t.co_sh4
    """

    condicoes = []
    valores = []

    if "ano" in filtros:
        condicoes.append("t.co_ano = %s")
        valores.append(filtros["ano"])

    if "mes" in filtros:
        condicoes.append("t.co_mes = %s")
        valores.append(filtros["mes"])

    if "municipio" in filtros:
        condicoes.append("m.co_mun = %s") 
        valores.append(filtros["municipio"])

    if "ncm" in filtros:
        condicoes.append("t.co_sh4 = %s")
        valores.append(filtros["ncm"])

    if "pais" in filtros:
        condicoes.append("(p.co_pais = %s OR p.co_pais_isoa3 = %s OR p.no_pais = %s)")
        valores.extend([filtros["pais"]] * 3)

    if condicoes:
        sql += " WHERE " + " AND ".join(condicoes)

    if agrupar_por_mes:
        sql += " GROUP BY t.co_mes ORDER BY t.co_mes"

    return sql, valores