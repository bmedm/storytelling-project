def organice(df,column,old_w,new_w):
    """
     Esta función cambia los datos 
     de las filas
     df=DataFrame 
     column= Columna a la que pertenezca el item
     old_w= palabra que quieras cambiar
     new_w= palabra nueva que necesites

    """
    lista=list(df[column].item())
    for i in lista:
        ind=[i[0]]
        r1=re.findall(old_w,str(i[1]))
        if r1:
            df[column][ind]=new_w
    return df.head(5)


def datacol (df,column,dato):
    """
    obtener dataframe 
    para un grupo de datos concreto de alguna
    columna concreta
    """
    columna=df[df[column]==dato]
    return columna

def agruparcount (df,group,column):
    """
    agrupar por columna con el método groupby
    y muestra gráfica de líneas
    """
    return df.groupby(group).agg({column:["count"]})
   

def agruparmean(df,group,column):
    return df.groupby(group).agg({column:["mean"]})
    



def barplot(df,column):
    """
    countplot para crear 
    un gráfico de barras que muestra los sucesos
    de cada value_count
    """
    plt.subplots(figsize=(20,5))
    sns.countplot(column,data=df,palette="BuGn_r",edgecolor=sns.color_palette('cubehelix',9))
    
    
def barline(df,col1,col2):
    """
    Mediante pandas.crosstab en seaborn
    creamos un grafico de líneas para saber 
    cuantos sucesos tenemos de cada combinación
    """
    return sns.crosstab(df[col1],df[col2]).plot(color=sns.color_palette('husl',10))
   


def top5(df,col):
    """
    Mediante value_counts
    """
    top5= df[df[col].isin(df[col].value_counts()[0:6].index)]
    return top5
