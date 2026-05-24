import streamlit as st
import pandas as pd

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Kalkulator Bobot Molekul", layout="wide", page_icon="🧪")

st.title("🧪 Kalkulator Bobot Molekul & Komposer Senyawa")
st.write("Klik simbol unsur pada tabel untuk merakit senyawa kimia dan menghitung Massa Molekul Relatif (Mr) secara real-time!")

# --- 2. DATABASE UNSUR KIMIA LENGKAP (118 UNSUR) ---
ELEMENT_DATA = {
    "H": {"No": 1, "Ar": 1.008, "color": "#3A96B4", "row": 0, "col": 0},
    "He": {"No": 2, "Ar": 4.0026, "color": "#9B59B6", "row": 0, "col": 17},
    "Li": {"No": 3, "Ar": 6.94, "color": "#E74C3C", "row": 1, "col": 0},
    "Be": {"No": 4, "Ar": 9.0122, "color": "#E67E22", "row": 1, "col": 1},
    "B": {"No": 5, "Ar": 10.81, "color": "#1ABC9C", "row": 1, "col": 12},
    "C": {"No": 6, "Ar": 12.011, "color": "#3A96B4", "row": 1, "col": 13},
    "N": {"No": 7, "Ar": 14.007, "color": "#3A96B4", "row": 1, "col": 14},
    "O": {"No": 8, "Ar": 15.999, "color": "#3A96B4", "row": 1, "col": 15},
    "F": {"No": 9, "Ar": 18.998, "color": "#2ECC71", "row": 1, "col": 16},
    "Ne": {"No": 10, "Ar": 20.180, "color": "#9B59B6", "row": 1, "col": 17},
    "Na": {"No": 11, "Ar": 22.990, "color": "#E74C3C", "row": 2, "col": 0},
    "Mg": {"No": 12, "Ar": 24.305, "color": "#E67E22", "row": 2, "col": 1},
    "Al": {"No": 13, "Ar": 26.982, "color": "#BDC3C7", "row": 2, "col": 12},
    "Si": {"No": 14, "Ar": 28.085, "color": "#1ABC9C", "row": 2, "col": 13},
    "P": {"No": 15, "Ar": 30.974, "color": "#3A96B4", "row": 2, "col": 14},
    "S": {"No": 16, "Ar": 32.06, "color": "#3A96B4", "row": 2, "col": 15},
    "Cl": {"No": 17, "Ar": 35.45, "color": "#2ECC71", "row": 2, "col": 16},
    "Ar": {"No": 18, "Ar": 39.948, "color": "#9B59B6", "row": 2, "col": 17},
    "K": {"No": 19, "Ar": 39.098, "color": "#E74C3C", "row": 3, "col": 0},
    "Ca": {"No": 20, "Ar": 40.078, "color": "#E67E22", "row": 3, "col": 1},
    "Sc": {"No": 21, "Ar": 44.956, "color": "#F1C40F", "row": 3, "col": 2},
    "Ti": {"No": 22, "Ar": 47.867, "color": "#F1C40F", "row": 3, "col": 3},
    "V": {"No": 23, "Ar": 50.942, "color": "#F1C40F", "row": 3, "col": 4},
    "Cr": {"No": 24, "Ar": 51.996, "color": "#F1C40F", "row": 3, "col": 5},
    "Mn": {"No": 25, "Ar": 54.938, "color": "#F1C40F", "row": 3, "col": 6},
    "Fe": {"No": 26, "Ar": 55.845, "color": "#F1C40F", "row": 3, "col": 7},
    "Co": {"No": 27, "Ar": 58.933, "color": "#F1C40F", "row": 3, "col": 8},
    "Ni": {"No": 28, "Ar": 58.693, "color": "#F1C40F", "row": 3, "col": 9},
    "Cu": {"No": 29, "Ar": 63.546, "color": "#F1C40F", "row": 3, "col": 10},
    "Zn": {"No": 30, "Ar": 65.38, "color": "#F1C40F", "row": 3, "col": 11},
    "Ga": {"No": 31, "Ar": 69.723, "color": "#BDC3C7", "row": 3, "col": 12},
    "Ge": {"No": 32, "Ar": 72.630, "color": "#1ABC9C", "row": 3, "col": 13},
    "As": {"No": 33, "Ar": 74.922, "color": "#1ABC9C", "row": 3, "col": 14},
    "Se": {"No": 34, "Ar": 78.971, "color": "#3A96B4", "row": 3, "col": 15},
    "Br": {"No": 35, "Ar": 79.904, "color": "#2ECC71", "row": 3, "col": 16},
    "Kr": {"No": 36, "Ar": 83.798, "color": "#9B59B6", "row": 3, "col": 17},
    "Rb": {"No": 37, "Ar": 85.468, "color": "#E74C3C", "row": 4, "col": 0},
    "Sr": {"No": 38, "Ar": 87.62, "color": "#E67E22", "row": 4, "col": 1},
    "Y": {"No": 39, "Ar": 88.906, "color": "#F1C40F", "row": 4, "col": 2},
    "Zr": {"No": 40, "Ar": 91.224, "color": "#F1C40F", "row": 4, "col": 3},
    "Nb": {"No": 41, "Ar": 92.906, "color": "#F1C40F", "row": 4, "col": 4},
    "Mo": {"No": 42, "Ar": 95.95, "color": "#F1C40F", "row": 4, "col": 5},
    "Tc": {"No": 43, "Ar": 98.0, "color": "#F1C40F", "row": 4, "col": 6},
    "Ru": {"No": 44, "Ar": 101.07, "color": "#F1C40F", "row": 4, "col": 7},
    "Rh": {"No": 45, "Ar": 102.91, "color": "#F1C40F", "row": 4, "col": 8},
    "Pd": {"No": 46, "Ar": 106.42, "color": "#F1C40F", "row": 4, "col": 9},
    "Ag": {"No": 47, "Ar": 107.87, "color": "#F1C40F", "row": 4, "col": 10},
    "Cd": {"No": 48, "Ar": 112.41, "color": "#F1C40F", "row": 4, "col": 11},
    "In": {"No": 49, "Ar": 114.82, "color": "#BDC3C7", "row": 4, "col": 12},
    "Sn": {"No": 50, "Ar": 118.71, "color": "#BDC3C7", "row": 4, "col": 13},
    "Sb": {"No": 51, "Ar": 121.76, "color": "#1ABC9C", "row": 4, "col": 14},
    "Te": {"No": 52, "Ar": 127.60, "color": "#1ABC9C", "row": 4, "col": 15},
    "I": {"No": 53, "Ar": 126.90, "color": "#2ECC71", "row": 4, "col": 16},
    "Xe": {"No": 54, "Ar": 131.29, "color": "#9B59B6", "row": 4, "col": 17},
    "Cs": {"No": 55, "Ar": 132.91, "color": "#E74C3C", "row": 5, "col": 0},
    "Ba": {"No": 56, "Ar": 137.33, "color": "#E67E22", "row": 5, "col": 1},
    "Hf": {"No": 72, "Ar": 178.49, "color": "#F1C40F", "row": 5, "col": 3},
    "Ta": {"No": 73, "Ar": 180.95, "color": "#F1C40F", "row": 5, "col": 4},
    "W": {"No": 74, "Ar": 183.84, "color": "#F1C40F", "row": 5, "col": 5},
    "Re": {"No": 75, "Ar": 186.21, "color": "#F1C40F", "row": 5, "col": 6},
    "Os": {"No": 76, "Ar": 190.23, "color": "#F1C40F", "row": 5, "col": 7},
    "Ir": {"No": 77, "Ar": 192.22, "color": "#F1C40F", "row": 5, "col": 8},
    "Pt": {"No": 78, "Ar": 195.08, "color": "#F1C40F", "row": 5, "col": 9},
    "Au": {"No": 79, "Ar": 196.97, "color": "#F1C40F", "row": 5, "col": 10},
    "Hg": {"No": 80, "Ar": 200.59, "color": "#F1C40F", "row": 5, "col": 11},
    "Tl": {"No": 81, "Ar": 204.38, "color": "#BDC3C7", "row": 5, "col": 12},
    "Pb": {"No": 82, "Ar": 207.2, "color": "#BDC3C7", "row": 5, "col": 13},
    "Bi": {"No": 83, "Ar": 208.98, "color": "#BDC3C7", "row": 5, "col": 14},
    "Po": {"No": 84, "Ar": 209.0, "color": "#1ABC9C", "row": 5, "col": 15},
    "At": {"No": 85, "Ar": 210.0, "color": "#2ECC71", "row": 5, "col": 16},
    "Rn": {"No": 86, "Ar": 222.0, "color": "#9B59B6", "row": 5, "col": 17},
    "Fr": {"No": 87, "Ar": 223.0, "color": "#E74C3C", "row": 6, "col": 0},
    "Ra": {"No": 88, "Ar": 226.0, "color": "#E67E22", "row": 6, "col": 1},
    "Rf": {"No": 104, "Ar": 267.0, "color": "#F1C40F", "row": 6, "col": 3},
    "Db": {"No": 105, "Ar": 268.0, "color": "#F1C40F", "row": 6, "col": 4},
    "Sg": {"No": 106, "Ar": 271.0, "color": "#F1C40F", "row": 6, "col": 5},
    "Bh": {"No": 107, "Ar": 272.0, "color": "#F1C40F", "row": 6, "col": 6},
    "Hs": {"No": 108, "Ar": 270.0, "color": "#F1C40F", "row": 6, "col": 7},
    "Mt": {"No": 109, "Ar": 276.0, "color": "#F1C40F", "row": 6, "col": 8},
    "Ds": {"No": 110, "Ar": 281.0, "color": "#F1C40F", "row": 6, "col": 9},
    "Rg": {"No": 111, "Ar": 280.0, "color": "#F1C40F", "row": 6, "col": 10},
    "Cn": {"No": 112, "Ar": 285.0, "color": "#F1C40F", "row": 6, "col": 11},
    "Nh": {"No": 113, "Ar": 284.0, "color": "#BDC3C7", "row": 6, "col": 12},
    "Fl": {"No": 114, "Ar": 289.0, "color": "#BDC3C7", "row": 6, "col": 13},
    "Mc": {"No": 115, "Ar": 288.0, "color": "#BDC3C7", "row": 6, "col": 14},
    "Lv": {"No": 116, "Ar": 293.0, "color": "#BDC3C7", "row": 6, "col": 15},
    "Ts": {"No": 117, "Ar": 294.0, "color": "#2ECC71", "row": 6, "col": 16},
    "Og": {"No": 118, "Ar": 294.0, "color": "#9B59B6", "row": 6, "col": 17},
    
    # Lanthanides (Row 7, di-offset kolomnya)
    "La": {"No": 57, "Ar": 138.91, "color": "#9C27B0", "row": 7, "col": 2},
    "Ce": {"No": 58, "Ar": 140.12, "color": "#9C27B0", "row": 7, "col": 3},
    "Pr": {"No": 59, "Ar": 140.91, "color": "#9C27B0", "row": 7, "col": 4},
    "Nd": {"No": 60, "Ar": 144.24, "color": "#9C27B0", "row": 7, "col": 5},
    "Pm": {"No": 61, "Ar": 145.0, "color": "#9C27B0", "row": 7, "col": 6},
    "Sm": {"No": 62, "Ar": 150.36, "color": "#9C27B0", "row": 7, "col": 7},
    "Eu": {"No": 63, "Ar": 151.96, "color": "#9C27B0", "row": 7, "col": 8},
    "Gd": {"No": 64, "Ar": 157.25, "color": "#9C27B0", "row": 7, "col": 9},
    "Tb": {"No": 65, "Ar": 158.93, "color": "#9C27B0", "row": 7, "col": 10},
    "Dy": {"No": 66, "Ar": 162.50, "color": "#9C27B0", "row": 7, "col": 11},
    "Ho": {"No": 67, "Ar": 164.93, "color": "#9C27B0", "row": 7, "col": 12},
    "Er": {"No": 68, "Ar": 167.26, "color": "#9C27B0", "row": 7, "col": 13},
    "Tm": {"No": 69, "Ar": 168.93, "color": "#9C27B0", "row": 7, "col": 14},
    "Yb": {"No": 70, "Ar": 173.05, "color": "#9C27B0", "row": 7, "col": 15},
    "Lu": {"No": 71, "Ar": 174.97, "color": "#9C27B0", "row": 7, "col": 16},
    
    # Actinides (Row 8, di-offset kolomnya)
    "Ac": {"No": 89, "Ar": 227.0, "color": "#E91E63", "row": 8, "col": 2},
    "Th": {"No": 90, "Ar": 232.04, "color": "#E91E63", "row": 8, "col": 3},
    "Pa": {"No": 91, "Ar": 231.04, "color": "#E91E63", "row": 8, "col": 4},
    "U": {"No": 92, "Ar": 238.03, "color": "#E91E63", "row": 8, "col": 5},
    "Np": {"No": 93, "Ar": 237.0, "color": "#E91E63", "row": 8, "col": 6},
    "Pu": {"No": 94, "Ar": 244.0, "color": "#E91E63", "row": 8, "col": 7},
    "Am": {"No": 95, "Ar": 243.0, "color": "#E91E63", "row": 8, "col": 8},
    "Cm": {"No": 96, "Ar": 247.0, "color": "#E91E63", "row": 8, "col": 9},
    "Bk": {"No": 97, "Ar": 247.0, "color": "#E91E63", "row": 8, "col": 10},
    "Cf": {"No": 98, "Ar": 251.0, "color": "#E91E63", "row": 8, "col": 11},
    "Es": {"No": 99, "Ar": 252.0, "color": "#E91E63", "row": 8, "col": 12},
    "Fm": {"No": 100, "Ar": 257.0, "color": "#E91E63", "row": 8, "col": 13},
    "Md": {"No": 101, "Ar": 258.0, "color": "#E91E63", "row": 8, "col": 14},
    "No": {"No": 102, "Ar": 259.0, "color": "#E91E63", "row": 8, "col": 15},
    "Lr": {"No": 103, "Ar": 262.0, "color": "#E91E63", "row": 8, "col": 16}
}

# --- 3. SUNTIKKAN STYLING WARNA TOMBOL CUSTOM ---
# Ini digunakan agar tombol di Streamlit memiliki warna bawaan golongan unsur masing-masing
button_styles = ""
for sym, info in ELEMENT_DATA.items():
    button_styles += f"""
    div[data-testid="stActionButtonElement"] > button[key="btn_{sym}"], 
    div.stButton > button[key="btn_{sym}"] {{
        background-color: {info['color']} !important;
        color: white !important;
        font-weight: bold !important;
        border: 1px solid rgba(0,0,0,0.2) !important;
        height: 48px !important;
        width: 100% !important;
        padding: 0px !important;
        font-size: 14px !important;
    }}
    """
st.markdown(f"<style>{button_styles}</style>", unsafe_allow_html=True)

# --- 4. STATE MANAGEMENT (PAPAN SENYAWA) ---
if "puzzle_comp" not in st.session_state:
    st.session_state.puzzle_comp = []

def tambah_unsur(unsur):
    for item in st.session_state.puzzle_comp:
        if item["unsur"] == unsur:
            item["jumlah"] += 1
            return
    st.session_state.puzzle_comp.append({"unsur": unsur, "jumlah": 1})

def reset_puzzle():
    st.session_state.puzzle_comp = []

# --- 5. RENDER TABEL PERIODIK (18 KOLOM AKURAT) ---
st.subheader("🧩 1. Tabel Periodik Unsur")

# Urutan rendering grid baris demi baris (0 s.d 8)
for r in range(9):
    # Buat spasi pemisah vertikal sebelum deret lantanida/aktinida
    if r == 7:
        st.write("")
    
    cols = st.columns(18)
    
    # Filter unsur apa saja yang ada di baris aktif ini
    row_elements = {k: v for k, v in ELEMENT_DATA.items() if v["row"] == r}
    
    # Mengisi kolom lantanida / aktinida dengan label teks pembantu
    if r == 7:
        cols[0].markdown("<p style='font-size:12px; font-weight:bold; padding-top:12px; color:#888;'>Lan:</p>", unsafe_allow_html=True)
    elif r == 8:
        cols[0].markdown("<p style='font-size:12px; font-weight:bold; padding-top:12px; color:#888;'>Akt:</p>", unsafe_allow_html=True)
        
    for c in range(18):
        # Cari jika ada unsur yang menduduki koordinat Baris r dan Kolom c ini
        match_sym = None
        for sym, info in row_elements.items():
            if info["col"] == c:
                match_sym = sym
                break
        
        if match_sym:
            # Render tombol asli Streamlit. Tidak memicu refresh halaman global!
            if cols[c].button(match_sym, key=f"btn_{match_sym}"):
                tambah_unsur(match_sym)
                st.rerun()

st.markdown("---")

# --- 6. PAPAN SENYAWAMU & KALKULATOR BOBOT MOLEKUL ---
st.subheader("🖼️ 2. Papan Senyawa Aktif & Hitungan Bobot Molekul")

if not st.session_state.puzzle_comp:
    st.info("Papan kosong. Silakan klik simbol unsur kimia di atas untuk merakit senyawa dan menghitung massanya.")
else:
    # Styling kartu visual di papan senyawa aktif
    st.markdown("""
        <style>
        .element-card {
            border-radius: 8px; padding: 8px; text-align: center;
            color: #FFFFFF !important; box-shadow: 0px 4px 6px rgba(0,0,0,0.15);
            font-family: sans-serif; min-height: 90px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.4); margin-bottom: 5px;
        }
        .el-no { font-size: 11px; text-align: left; margin: 0; opacity: 0.8; }
        .el-sym { font-size: 26px; font-weight: bold; margin: -2px 0; }
        .el-ar { font-size: 11px; margin-top: 2px; background: rgba(0,0,0,0.2); border-radius: 4px; }
        </style>
