#!/usr/bin/env bash
pip install -r requirements.txt
streamlit run app_emas.py --server.port $PORT --server.address 0.0.0.0 --server.enableCORS false
