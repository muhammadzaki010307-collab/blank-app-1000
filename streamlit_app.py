import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Kalkulator Senyawa Kimia", layout="wide", page_icon="🧪")

st.title("🧪 Komposer Senyawa Kimia")
st.write("Klik simbol unsur pada tabel di bawah untuk merakit senyawa kimia dan melihat detail massanya!")

# --- 2. DATABASE UNSUR KIMIA DENGAN WARNA GOLONGAN ---
ELEMENT_DATA = {
    "H": {"No": 1, "Ar": 1.008, "color": "#3A96B4"},
    "He": {"No": 2, "Ar": 4.0026, "color": "#9B59B6"},
    "Li": {"No": 3, "Ar": 6.94, "color": "#E74C3C"},
    "Be": {"No": 4, "Ar": 9.0122, "color": "#E67E22"},
    "B": {"No": 5, "Ar": 10.81, "color": "#1ABC9C"},
    "C": {"No": 6, "Ar": 12.011, "color": "#3A96B4"},
    "N": {"No": 7, "Ar": 14.007, "color": "#3A96B4"},
    "O": {"No": 8, "Ar": 15.999, "color": "#3A96B4"},
    "F": {"No": 9, "Ar": 18.998, "color": "#2ECC71"},
    "Ne": {"No": 10, "Ar": 20.180, "color": "#9B59B6"},
    "Na": {"No": 11, "Ar": 22.990, "color": "#E74C3C"},
    "Mg": {"No": 12, "Ar": 24.305, "color": "#E67E22"},
    "Al": {"No": 13, "Ar": 26.982, "color": "#BDC3C7"},
    "Si": {"No": 14, "Ar": 28.085, "color": "#1ABC9C"},
    "P": {"No": 15, "Ar": 30.974, "color": "#3A96B4"},
    "S": {"No": 16, "Ar": 32.06, "color": "#3A96B4"},
    "Cl": {"No": 17, "Ar": 35.45, "color": "#2ECC71"},
    "Ar": {"No": 18, "Ar": 39.948, "color": "#9B59B6"},
    "K": {"No": 19, "Ar": 39.098, "color": "#E74C3C"},
    "Ca": {"No": 20, "Ar": 40.078, "color": "#E67E22"},
    "Sc": {"No": 21, "Ar": 44.956, "color": "#F1C40F"},
    "Ti": {"No": 22, "Ar": 47.867, "color": "#F1C40F"},
    "V": {"No": 23, "Ar": 50.942, "color": "#F1C40F"},
    "Cr": {"No": 24, "Ar": 51.996, "color": "#F1C40F"},
    "Mn": {"No": 25, "Ar": 54.938, "color": "#F1C40F"},
    "Fe": {"No": 26, "Ar": 55.845, "color": "#F1C40F"},
    "Co": {"No": 27, "Ar": 58.933, "color": "#F1C40F"},
    "Ni": {"No": 28, "Ar": 58.693, "color": "#F1C40F"},
    "Cu": {"No": 29, "Ar": 63.546, "color": "#F1C40F"},
    "Zn": {"No": 30, "Ar": 65.38, "color": "#F1C40F"},
    "Ga": {"No": 31, "Ar": 69.723, "color": "#BDC3C7"},
    "Ge": {"No": 32, "Ar": 72.630, "color": "#1ABC9C"},
    "As": {"No": 33, "Ar": 74.922, "color": "#1ABC9C"},
    "Se": {"No": 34, "Ar": 78.971, "color": "#3A96B4"},
    "Br": {"No": 35, "Ar": 79.904, "color": "#2ECC71"},
    "Kr": {"No": 36, "Ar": 83.798, "color": "#9B59B6"},
    "Rb": {"No": 37, "Ar": 85.468, "color": "#E74C3C"},
    "Sr": {"No": 38, "Ar": 87.62, "color": "#E67E22"},
    "Y": {"No": 39, "Ar": 88.906, "color": "#F1C40F"},
    "Zr": {"No": 40, "Ar": 91.224, "color": "#F1C40F"},
    "Nb": {"No": 41, "Ar": 92.906, "color": "#F1C40F"},
    "Mo": {"No": 42, "Ar": 95.95, "color": "#F1C40F"},
    "Tc": {"No": 43, "Ar": 98.0, "color": "#F1C40F"},
    "Ru": {"No": 44, "Ar": 101.07, "color": "#F1C40F"},
    "Rh": {"No": 45, "Ar": 102.91, "color": "#F1C40F"},
    "Pd": {"No": 46, "Ar": 106.42, "color": "#F1C40F"},
    "Ag": {"No": 47, "Ar": 107.87, "color": "#F1C40F"},
    "Cd": {"No": 48, "Ar": 112.41, "color": "#F1C40F"},
    "In": {"No": 49, "Ar": 114.82, "color": "#BDC3C7"},
    "Sn": {"No": 50, "Ar": 118.71, "color": "#BDC3C7"},
    "Sb": {"No": 51, "Ar": 121.76, "color": "#1ABC9C"},
    "Te": {"No": 52, "Ar": 127.60, "color": "#1ABC9C"},
    "I": {"No": 53, "Ar": 126.90, "color": "#2ECC71"},
    "Xe": {"No": 54, "Ar": 131.29, "color": "#9B59B6"},
    "Cs": {"No": 55, "Ar": 132.91, "color": "#E74C3C"},
    "Ba": {"No": 56, "Ar": 137.33, "color": "#E67E22"},
    "La": {"No": 57, "Ar": 138.91, "color": "#9C27B0"},
    "Ce": {"No": 58, "Ar": 140.12, "color": "#9C27B0"},
    "Pr": {"No": 59, "Ar": 140.91, "color": "#9C27B0"},
    "Nd": {"No": 60, "Ar": 144.24, "color": "#9C27B0"},
    "Pm": {"No": 61, "Ar": 145.0, "color": "#9C27B0"},
    "Sm": {"No": 62, "Ar": 150.36, "color": "#9C27B0"},
    "Eu": {"No": 63, "Ar": 151.96, "color": "#9C27B0"},
    "Gd": {"No": 64, "Ar": 157.25, "color": "#9C27B0"},
    "Tb": {"No": 65, "Ar": 158.93, "color": "#9C27B0"},
    "Dy": {"No": 66, "Ar": 162.50, "color": "#9C27B0"},
    "Ho": {"No": 67, "Ar": 164.93, "color": "#9C27B0"},
    "Er": {"No": 68, "Ar": 167.26, "color": "#9C27B0"},
    "Tm": {"No": 69, "Ar": 168.93, "color": "#9C27B0"},
    "Yb": {"No": 70, "Ar": 173.05, "color": "#9C27B0"},
    "Lu": {"No": 71, "Ar": 174.97, "color": "#9C27B0"},
    "Hf": {"No": 72, "Ar": 178.49, "color": "#F1C40F"},
    "Ta": {"No": 73, "Ar": 180.95, "color": "#F1C40F"},
    "W": {"No": 74, "Ar": 183.84, "color": "#F1C40F"},
    "Re": {"No": 75, "Ar": 186.21, "color": "#F1C40F"},
    "Os": {"No": 76, "Ar": 190.23, "color": "#F1C40F"},
    "Ir": {"No": 77, "Ar": 192.22, "color": "#F1C40F"},
    "Pt": {"No": 78, "Ar": 195.08, "color": "#F1C40F"},
    "Au": {"No": 79, "Ar": 196.97, "color": "#F1C40F"},
    "Hg": {"No": 80, "Ar": 200.59, "color": "#F1C40F"},
    "Tl": {"No": 81, "Ar": 204.38, "color": "#BDC3C7"},
    "Pb": {"No": 82, "Ar": 207.2, "color": "#BDC3C7"},
    "Bi": {"No": 83, "Ar": 208.98, "color": "#BDC3C7"},
    "Po": {"No": 84, "Ar": 209.0, "color": "#1ABC9C"},
    "At": {"No": 85, "Ar": 210.0, "color": "#2ECC71"},
    "Rn": {"No": 86, "Ar": 222.0, "color": "#9B59B6"},
    "Fr": {"No": 87, "Ar": 223.0, "color": "#E74C3C"},
    "Ra": {"No": 88, "Ar": 226.0, "color": "#E67E22"},
    "Ac": {"No": 89, "Ar": 227.0, "color": "#E91E63"},
    "Th": {"No": 90, "Ar": 232.04, "color": "#E91E63"},
    "Pa": {"No": 91, "Ar": 231.04, "color": "#E91E63"},
    "U": {"No": 92, "Ar": 238.03, "color": "#E91E63"},
    "Np": {"No": 93, "Ar": 237.0, "color": "#E91E63"},
    "Pu": {"No": 94, "Ar": 244.0, "color": "#E91E63"},
    "Am": {"No": 95, "Ar": 243.0, "color": "#E91E63"},
    "Cm": {"No": 96, "Ar": 247.0, "color": "#E91E63"},
    "Bk": {"No": 97, "Ar": 247.0, "color": "#E91E63"},
    "Cf": {"No": 98, "Ar": 251.0, "color": "#E91E63"},
    "Es": {"No": 99, "Ar": 252.0, "color": "#E91E63"},
    "Fm": {"No": 100, "Ar": 257.0, "color": "#E91E63"},
    "Md": {"No": 101, "Ar": 258.0, "color": "#E91E63"},
    "No": {"No": 102, "Ar": 259.0, "color": "#E91E63"},
    "Lr": {"No": 103, "Ar": 262.0, "color": "#E91E63"},
    "Rf": {"No": 104, "Ar": 267.0, "color": "#F1C40F"},
    "Db": {"No": 105, "Ar": 268.0, "color": "#F1C40F"},
    "Sg": {"No": 106, "Ar": 271.0, "color": "#F1C40F"},
    "Bh": {"No": 107, "Ar": 272.0, "color": "#F1C40F"},
    "Hs": {"No": 108, "Ar": 270.0, "color": "#F1C40F"},
    "Mt": {"No": 109, "Ar": 276.0, "color": "#F1C40F"},
    "Ds": {"No": 110, "Ar": 281.0, "color": "#F1C40F"},
    "Rg": {"No": 111, "Ar": 280.0, "color": "#F1C40F"},
    "Cn": {"No": 112, "Ar": 285.0, "color": "#F1C40F"},
    "Nh": {"No": 113, "Ar": 284.0, "color": "#BDC3C7"},
    "Fl": {"No": 114, "Ar": 289.0, "color": "#BDC3C7"},
    "Mc": {"No": 115, "Ar": 288.0, "color": "#BDC3C7"},
    "Lv": {"No": 116, "Ar": 293.0, "color": "#BDC3C7"},
    "Ts": {"No": 117, "Ar": 294.0, "color": "#2ECC71"},
    "Og": {"No": 118, "Ar": 294.0, "color": "#9B59B6"}
}
# --- GENERATE KELAS CSS DINAMIS DARI WARNA ---
unique_colors = set([data["color"] for data in ELEMENT_DATA.values()])
dynamic_css_classes = "\n".join([f".bg-{c.replace('#', '')} {{ background-color: {c} !important; border-color: {c} !important; }}" for c in unique_colors])

# Suntikkan kelas warna ke dalam Streamlit Global (agar markdown Papan Senyawa berwarna)
st.markdown(f"<style>{dynamic_css_classes}</style>", unsafe_allow_html=True)

# --- 3. STATE MANAGEMENT & EVENT HANDLING ---
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

# Deteksi klik (kompatibel dengan berbagai versi Streamlit)
if hasattr(st, "query_params"):
    params = st.query_params
    if "click_el" in params:
        clicked_element = params["click_el"]
        if clicked_element in ELEMENT_DATA:
            tambah_unsur(clicked_element)
        st.query_params.clear()
        st.rerun()

# --- 4. RENDER TABEL PERIODIK DENGAN KELAS CSS ---
st.subheader("🧩 1. Tabel Periodik Unsur")

grid_structure = [
    ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
]
lan_elements = ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]
akt_elements = ["Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ font-family: system-ui, sans-serif; background-color: transparent; margin: 0; padding: 5px; }}
    .periodic-table {{ display: grid; grid-template-columns: repeat(18, minmax(0, 1fr)); gap: 4px; }}
    .row-space {{ grid-column: span 18; height: 10px; }}
    
    /* Injeksi Kelas Warna ke dalam HTML Iframe */
    {dynamic_css_classes}

    .cell {{ 
        min-height: 42px; display: flex; align-items: center; justify-content: center; 
        border-radius: 6px; text-decoration: none !important; 
        box-shadow: 0px 2px 4px rgba(0,0,0,0.3), inset 0px 1px 1px rgba(255,255,255,0.4);
        transition: all 0.2s ease; cursor: pointer;
    }}
    .cell-label {{ 
        font-size: 12px; font-weight: bold; color: #888; 
        display: flex; align-items: center; justify-content: center; background: transparent; box-shadow: none;
    }}
    .empty {{ background: transparent !important; box-shadow: none; border: none; pointer-events: none; }}
    .el-text {{ color: #FFFFFF !important; font-weight: 800; font-size: 16px; text-shadow: 1px 1px 2px rgba(0,0,0,0.6); }}
    .cell:hover {{ filter: brightness(1.25); transform: translateY(-3px); box-shadow: 0px 5px 8px rgba(0,0,0,0.4); z-index: 10; }}
    .cell:active {{ transform: scale(0.9); }}
</style>
</head>
<body>
<div class="periodic-table">
"""

for row in grid_structure:
    for sym in row:
        if sym == "":
            html_code += '<div class="cell empty"></div>'
        else:
            color_class = f"bg-{ELEMENT_DATA[sym]['color'].replace('#', '')}"
            html_code += f'<a href="?click_el={sym}" target="_top" class="cell {color_class}"><span class="el-text">{sym}</span></a>'

html_code += '<div class="row-space"></div>'
html_code += '<div class="cell cell-label">Lan:</div><div class="cell empty"></div>'
for sym in lan_elements:
    color_class = f"bg-{ELEMENT_DATA[sym]['color'].replace('#', '')}"
    html_code += f'<a href="?click_el={sym}" target="_top" class="cell {color_class}"><span class="el-text">{sym}</span></a>'
html_code += '<div class="cell empty"></div>'

html_code += '<div class="cell cell-label">Akt:</div><div class="cell empty"></div>'
for sym in akt_elements:
    color_class = f"bg-{ELEMENT_DATA[sym]['color'].replace('#', '')}"
    html_code += f'<a href="?click_el={sym}" target="_top" class="cell {color_class}"><span class="el-text">{sym}</span></a>'
html_code += '<div class="cell empty"></div>'

html_code += "</div></body></html>"

# Mengubah tinggi ke 435 untuk menghindari bug cache rendering iframe di Streamlit
components.html(html_code, height=435, scrolling=False)

st.markdown("---")

# --- 5. PAPAN SENYAWAMU ---
st.subheader("🖼️ 2. Papan Senyawa Aktif & Informasi Unsur")

if not st.session_state.puzzle_comp:
    st.info("Papan kosong. Silakan klik unsur kimia di atas untuk memunculkan detail kartu keterangan beserta hitungan massanya.")
else:
    st.markdown("""
        <style>
        .element-card {
            border-radius: 8px; padding: 8px; text-align: center;
            color: #FFFFFF !important; box-shadow: 0px 4px 8px rgba(0,0,0,0.25);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; min-height: 110px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5); margin-bottom: 5px;
        }
        .el-no { font-size: 12px; text-align: left; margin: 0; font-weight: bold; opacity: 0.9; }
        .el-sym { font-size: 32px; font-weight: 900; margin: -4px 0; letter-spacing: -1px; }
        .el-ar { font-size: 11px; font-weight: bold; margin: 2px 0 0 0; background: rgba(0,0,0,0.3); border-radius: 4px; padding: 2px 0; }
        </style>
    """, unsafe_allow_html=True)
    
    total_komponen = len(st.session_state.puzzle_comp)
    papan_kolom = st.columns(max(total_komponen, 8))
    
    rumus_visual = ""
    total_bm = 0.0
    rincian_data = []
    
    for idx, item in enumerate(st.session_state.puzzle_comp):
        unsur = item["unsur"]
        jumlah = item["jumlah"]
        
        no_atom = ELEMENT_DATA[unsur]["No"]
        ar = ELEMENT_DATA[unsur]["Ar"]
        # Ambil kelas warna (hilangkan hash #)
        color_class = f"bg-{ELEMENT_DATA[unsur]['color'].replace('#', '')}"
        
        subtotal = ar * jumlah
        total_bm += subtotal
        
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        rumus_visual += f"{unsur}{str(jumlah).translate(SUB) if jumlah > 1 else ''}"
        
        rincian_data.append({
            "Unsur": unsur,
            "Nomor Atom": no_atom,
            "Massa Atom (Ar)": ar,
            "Jumlah": jumlah,
            "Subtotal Massa (g/mol)": round(subtotal, 4)
        })
        
        with papan_kolom[idx]:
            # Inject Class warna, tidak lagi pakai inline style yang sering di-cut oleh Streamlit
            card_html = f"""
            <div class="element-card {color_class}">
                <div class="el-no">№ {no_atom}</div>
                <div class="el-sym">{unsur}</div>
                <div class="el-ar">Ar: {ar}</div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([1, 1, 1])
            if c1.button("➖", key=f"papan_min_{unsur}_{idx}"):
                if item["jumlah"] > 1:
                    item["jumlah"] -= 1
                else:
                    st.session_state.puzzle_comp.pop(idx)
                st.rerun()
                
            c2.markdown(f"<p style='text-align:center; font-size:16px; font-weight:bold; margin-top:2px;'>{jumlah}</p>", unsafe_allow_html=True)
            
            if c3.button("➕", key=f"papan_plus_{unsur}_{idx}"):
                item["jumlah"] += 1
                st.rerun()

    st.write("")
    res_col1, res_col2 = st.columns([1, 2])
    with res_col1:
        st.success(f"### 🧪 Rumus: **{rumus_visual}**")
        st.metric(label="Berat Molekul Total (Mr)", value=f"{round(total_bm, 4)} g/mol")
        st.button("🗑️ Bersihkan Papan", key="btn_reset", on_click=reset_puzzle, type="primary")
        
    with res_col2:
        st.write("**📋 Kontribusi Massa & Detail Struktur Tabel:**")
        st.dataframe(pd.DataFrame(rincian_data), hide_index=True, use_container_width=True)
