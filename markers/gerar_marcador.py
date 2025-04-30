import cv2
import cv2.aruco as aruco
import os

def gerar_marcador(id=23, tamanho=300, pasta_destino="markers"):
    os.makedirs(pasta_destino, exist_ok=True)
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    marker_image = aruco.generateImageMarker(aruco_dict, id, tamanho)
    nome_arquivo = os.path.join(pasta_destino, f"marker_{id}.png")
    cv2.imwrite(nome_arquivo, marker_image)
    print(f"Marcador salvo em: {nome_arquivo}")

if __name__ == "__main__":
    gerar_marcador()
