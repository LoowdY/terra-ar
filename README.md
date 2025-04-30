# 🌍 Visualizador AR da Terra com Python + OpenCV + OpenGL

Este projeto implementa um sistema de **realidade aumentada** que exibe um **modelo 3D da Terra** sobre um marcador **ArUco**, utilizando Python, OpenGL, OpenCV e Pygame.

---

## 📸 Demonstração
- A câmera é usada como fundo em tempo real
- Ao detectar um marcador ArUco, uma esfera 3D texturizada com a Terra é renderizada sobre ele

---

## 🛠️ Requisitos

- Python 3.11 ou superior
- Sistema com suporte a OpenGL
- Webcam

---

## 📦 Instalação

Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Execução

Coloque o arquivo de textura em:  
`textures/Earth_Diffuse.jpg`

E execute:

```bash
python src/main_ar.py
```

---

## 🎯 Marcador ArUco

Use este gerador online: [https://chev.me/arucogen/](https://chev.me/arucogen/)  
Escolha o dicionário `DICT_4X4_50` e imprima um marcador.

---

## 🧩 Estrutura do Projeto

```
terra-ar/
├── src/
│   ├── main_ar.py
│   ├── main.py
│   ├── sphere.py
│   ├── earth_renderer.py
├── textures/
│   └── Earth_Diffuse.jpg
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Autor

Projeto de demonstração para aplicações com Python, RA e gráficos 3D.