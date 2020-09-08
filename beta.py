import alpha

matriz_granos_derivable = alpha.crear_matriz_carga_derivable('Matrices/Matrices Grupo Granos.xlsx','Total Toneladas Granos 2014','GRANOS')
matriz_mineria_derivable = alpha.crear_matriz_carga_derivable('Matrices/Matrices Grupo Mineria.xlsx', 'Total Toneladas Mineria 2014','MINERIA')
matriz_semiterminados_derivable = alpha.crear_matriz_carga_derivable('Matrices/Matrices Grupo Semiterminados.xlsx', 'Total Semiterminados 2014','SEMITERMINADOS')
matriz_industrializados_derivable = alpha.crear_matriz_carga_derivable('Matrices/Matrices Grupo Industrializados.xlsx', 'Total Industrializados 2014','INDUSTRIALIZADOS')
matriz_regionales_derivable = alpha.crear_matriz_carga_derivable('Matrices/Matrices Grupo Regionales.xlsx', 'Matriz Total Regionales 2014','MINERIA')

matriz_derivable = matriz_granos_derivable + matriz_mineria_derivable + matriz_semiterminados_derivable + matriz_industrializados_derivable + matriz_regionales_derivable

alpha.trans_matriz_a_xlsx(matriz_derivable, 'Matrices/Derivabilidad2.xlsx')