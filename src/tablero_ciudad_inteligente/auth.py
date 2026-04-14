"""Autenticación básica para proteger el acceso al dashboard."""

from __future__ import annotations

import os

import streamlit as st
from dotenv import load_dotenv
from passlib.context import CryptContext

load_dotenv()
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verificar_password(password_plano: str, password_hash: str) -> bool:
    if not password_hash:
        return True
    try:
        return PWD_CONTEXT.verify(password_plano, password_hash)
    except Exception:
        return False


def render_login() -> bool:
    st.sidebar.subheader("Acceso")
    password_hash = os.getenv("APP_PASSWORD_HASH", "")

    if not password_hash:
        st.sidebar.info("No se configuró contraseña. La app funciona en modo abierto.")
        return True

    if st.session_state.get("autenticado"):
        st.sidebar.success("Sesión iniciada")
        if st.sidebar.button("Cerrar sesión"):
            st.session_state["autenticado"] = False
            st.rerun()
        return True

    password = st.sidebar.text_input("Contraseña", type="password")
    if st.sidebar.button("Entrar"):
        if verificar_password(password, password_hash):
            st.session_state["autenticado"] = True
            st.rerun()
        st.sidebar.error("Contraseña incorrecta")

    st.warning("Este tablero está protegido. Ingresa la contraseña para continuar.")
    return False
