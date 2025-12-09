import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import date, timedelta

# --- Configurações Iniciais ---
st.set_page_config(
    page_title="Dashboard de Produtividade",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Variáveis de Meta ---
META_HORAS = 70
META_AGUA_ML = 2000

# --- Dados Simulados ---
def create_simulated_data(total_hours=META_HORAS, num_days=14):
    """Cria um DataFrame simulado para o dashboard."""
    
    start_date = date.today() - timedelta(days=num_days)
    dates = [start_date + timedelta(days=i) for i in range(num_days)]
    
    # Distribuição de horas (totalizando 70)
    daily_hours = np.random.uniform(4.0, 6.0, num_days)
    daily_hours = daily_hours * (total_hours / daily_hours.sum())
    
    data = []
    categories = ['Estudo', 'Extensão', 'Pessoal']
    
    for d, total_h in zip(dates, daily_hours):
        # Distribuição das horas diárias em tarefas
        num_tasks = np.random.randint(2, 5)
        task_hours = np.random.dirichlet(np.ones(num_tasks)) * total_h
        
        # Simulação de consumo de água (ml)
        water_ml = np.random.randint(1500, 3000)
        
        for i in range(num_tasks):
            category = np.random.choice(categories, p=[0.5, 0.3, 0.2])
            task_name = f"Tarefa {category} {i+1}"
            
            data.append({
                'Data': d,
                'Tarefa': task_name,
                'Categoria': category,
                'Horas': task_hours[i],
                'Água (ml)': water_ml
            })
            
    df = pd.DataFrame(data)
    df['Horas'] = df['Horas'].round(2)
    df['Data'] = pd.to_datetime(df['Data'])
    
    # Garantir que o total de horas seja 70 (pequeno ajuste final devido ao arredondamento)
    current_total = df['Horas'].sum()
    df['Horas'] = df['Horas'] * (total_hours / current_total)
    df['Horas'] = df['Horas'].round(2)
    
    # Adicionar coluna de meta de água atingida
    df['Meta Água Atingida'] = df['Água (ml)'] >= META_AGUA_ML
    
    return df

df = create_simulated_data()

# --- Cálculos Principais ---
total_horas_realizadas = df['Horas'].sum()
progresso_horas = min(total_horas_realizadas / META_HORAS, 1.0)
horas_restantes = max(0, META_HORAS - total_horas_realizadas)

# Calcular dias com meta de água atingida
df_agua_diaria = df.groupby('Data')['Meta Água Atingida'].max().reset_index()
dias_meta_agua_atingida = df_agua_diaria['Meta Água Atingida'].sum()
total_dias = len(df_agua_diaria)

# --- Título e Sidebar ---
st.title("📊 Dashboard de Produtividade")
st.sidebar.header("Configurações e Metas")
st.sidebar.metric("Meta de Horas", f"{META_HORAS} horas")
st.sidebar.metric("Meta de Água Diária", f"{META_AGUA_ML / 1000:.1f} Litros")
st.sidebar.info(f"Dados simulados de {df['Data'].min().strftime('%d/%m/%Y')} a {df['Data'].max().strftime('%d/%m/%Y')}")

# --- 1. Visão Geral (KPIs) ---
st.header("Visão Geral do Progresso")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total de Horas Realizadas",
        value=f"{total_horas_realizadas:.2f}h",
        delta=f"{progresso_horas * 100:.1f}% da meta"
    )

with col2:
    st.metric(
        label="Horas Restantes para a Meta",
        value=f"{horas_restantes:.2f}h"
    )

with col3:
    st.metric(
        label="Média Diária de Água",
        value=f"{df.groupby('Data')['Água (ml)'].mean().mean() / 1000:.2f} L"
    )

with col4:
    st.metric(
        label="Dias com Meta de Água Atingida",
        value=f"{dias_meta_agua_atingida} de {total_dias} dias",
        delta=f"{dias_meta_agua_atingida / total_dias * 100:.1f}%"
    )

st.progress(progresso_horas, text=f"Progresso: {total_horas_realizadas:.2f}h de {META_HORAS}h")

# --- 2. Análise de Tempo por Categoria ---
st.header("Distribuição de Horas por Categoria")
df_categoria = df.groupby('Categoria')['Horas'].sum().reset_index()
fig_pie = px.pie(
    df_categoria,
    values='Horas',
    names='Categoria',
    title='Distribuição Percentual das 70 Horas',
    hole=0.3
)
st.plotly_chart(fig_pie, use_container_width=True)

# --- 3. Rastreamento de Água ---
st.header("Rastreamento de Consumo de Água")
df_agua = df.groupby('Data')['Água (ml)'].mean().reset_index()
df_agua['Meta (ml)'] = META_AGUA_ML

fig_agua = px.line(
    df_agua,
    x='Data',
    y='Água (ml)',
    title='Consumo Diário de Água vs. Meta',
    markers=True
)
fig_agua.add_hline(y=META_AGUA_ML, line_dash="dash", line_color="red", annotation_text=f"Meta ({META_AGUA_ML}ml)")
fig_agua.update_layout(yaxis_title="Volume (ml)")
st.plotly_chart(fig_agua, use_container_width=True)

# --- 4. Detalhamento das Tarefas ---
st.header("Detalhamento das Tarefas Realizadas")
st.dataframe(
    df.sort_values(by='Data', ascending=False),
    use_container_width=True,
    column_config={
        "Data": st.column_config.DateColumn("Data", format="DD/MM/YYYY"),
        "Horas": st.column_config.NumberColumn("Horas (h)", format="%.2f"),
        "Água (ml)": st.column_config.NumberColumn("Água (ml)", format="%d"),
        "Meta Água Atingida": st.column_config.CheckboxColumn("Meta Água Atingida", default=False)
    }
)

# --- 5. Campo de Entrada (Demonstração de Funcionalidade) ---
st.header("Registro de Nova Atividade (Demonstração)")
with st.form("registro_atividade"):
    col_a, col_b = st.columns(2)
    with col_a:
        data_registro = st.date_input("Data", date.today())
        tarefa = st.text_input("Tarefa/Atividade")
        categoria = st.selectbox("Categoria", ['Estudo', 'Extensão', 'Pessoal'])
    with col_b:
        # Campos de entrada solicitados pelo usuário
        horas_estudo = st.number_input("Horas de Estudo Dedicadas", min_value=0.0, max_value=24.0, step=0.1)
        agua_ml = st.number_input("Água Consumida no Dia (ml)", min_value=0, step=100)
        
        # O campo de horas total é a soma das horas de estudo e outras horas da tarefa
        horas_total = horas_estudo # Simplificando para a demonstração
        
        meta_agua_atingida_input = st.checkbox("Meta de Água Atingida (>= 2000ml)", value=(agua_ml >= META_AGUA_ML), disabled=True)
    
    submitted = st.form_submit_button("Registrar")
    if submitted:
        st.success(f"Atividade '{tarefa}' registrada com sucesso! (Horas de Estudo: {horas_estudo}h, Água: {agua_ml}ml).")
        st.info("Lembre-se: os dados neste dashboard são simulados e não são persistentes.")

# --- Instruções para Execução ---
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por **MazzarinDev**")
st.sidebar.markdown("---")
st.sidebar.subheader("Instruções para a Faculdade")
st.sidebar.markdown(
    """
    Este dashboard foi criado com Python e Streamlit.
    Para executá-lo localmente, salve o código como `app.py` e execute no terminal:
    `streamlit run app.py`
    """
)
