#!/bin/bash

# Script Wrapper para Execução do Dashboard de Produtividade (Streamlit)

echo "Iniciando a instalação das dependências..."
pip3 install streamlit pandas plotly numpy

echo "Iniciando o Dashboard de Produtividade..."
streamlit run app.py
