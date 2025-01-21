from tkinter import Tk, Label, PhotoImage

def exibir_imagem_colorida(caminho_imagem):
    # Criar a janela principal
    janela = Tk()
    janela.title("Exibição de Imagem")

    # Carregar a imagem PNG diretamente com Tkinter
    imagem_tk = PhotoImage(file=caminho_imagem)

    # Criar um widget de rótulo para mostrar a imagem
    label = Label(janela, image=imagem_tk)
    label.pack()

def rgb_to_grayscale(r, g, b):
    """Converte valores RGB para tons de cinza usando a fórmula ponderada."""
    return int(0.299 * r + 0.587 * g + 0.114 * b)

def carregar_e_converter_para_cinza(caminho_imagem):
    """Carrega uma imagem PNG e a converte para tons de cinza."""
    # Carregar a imagem original
    img = PhotoImage(file=caminho_imagem)

    # Obter dimensões da imagem
    largura, altura = img.width(), img.height()

    # Criar uma nova imagem para os tons de cinza
    img_cinza = PhotoImage(width=largura, height=altura)

    for x in range(largura):
        for y in range(altura):
            # Obter cor RGB do pixel original
            r, g, b = img.get(x, y)

            # Converter para tons de cinza
            gray = rgb_to_grayscale(r, g, b)

            # Criar o valor em formato hexadecimal
            gray_hex = f"#{gray:02x}{gray:02x}{gray:02x}"

            # Definir o pixel convertido na nova imagem
            img_cinza.put(gray_hex, (x, y))

    return img_cinza

def exibir_imagem_em_cinza(caminho_imagem):
    """Exibe a imagem convertida em tons de cinza."""
    janela = Tk()
    janela.title("Imagem em Tons de Cinza")

    # Converter a imagem para tons de cinza
    img_cinza = carregar_e_converter_para_cinza(caminho_imagem)

    # Criar um rótulo para exibir a imagem
    label = Label(janela, image=img_cinza)
    label.pack()

    # Manter referência à imagem
    label.image = img_cinza

def grayscale_to_black_and_white(gray_value, limiar=128):
    """Converte um valor em tons de cinza para preto ou branco."""
    return 255 if gray_value > limiar else 0

def carregar_e_converter_para_preto_branco(caminho_imagem, limiar=128):
    """Carrega uma imagem PNG, converte para preto e branco."""
    # Carregar a imagem original
    img = PhotoImage(file=caminho_imagem)

    # Obter dimensões da imagem
    largura, altura = img.width(), img.height()

    # Criar uma nova imagem para preto e branco
    img_pb = PhotoImage(width=largura, height=altura)

    for x in range(largura):
        for y in range(altura):
            # Obter a cor RGB do pixel original
            r, g, b = img.get(x, y)  # Agora diretamente obtemos a tupla (r, g, b)

            # Converter para tons de cinza
            gray = rgb_to_grayscale(r, g, b)

            # Converter para preto e branco usando o limiar
            bw_value = grayscale_to_black_and_white(gray, limiar)

            # Criar o valor em formato hexadecimal
            bw_hex = f"#{bw_value:02x}{bw_value:02x}{bw_value:02x}"

            # Definir o pixel convertido na nova imagem
            img_pb.put(bw_hex, (x, y))

    return img_pb

def exibir_imagem_preto_branco(caminho_imagem, limiar=128):
    """Exibe a imagem convertida em preto e branco."""
    janela = Tk()
    janela.title("Imagem Preto e Branco")

    # Converter a imagem para preto e branco
    img_pb = carregar_e_converter_para_preto_branco(caminho_imagem, limiar)

    # Criar um rótulo para exibir a imagem
    label = Label(janela, image=img_pb)
    label.pack(side="left") # Exibe a imagem ao lado da outra

    # Manter referência à imagem
    label.image = img_pb

def exibir_imagem_colorida(janela, caminho_imagem):
    """Exibe a imagem colorida na janela"""
    # Carregar a imagem PNG diretamente com Tkinter
    imagem_tk = PhotoImage(file=caminho_imagem)

    # Criar um widget de rótulo para mostrar a imagem colorida
    label = Label(janela, image=imagem_tk)
    label.pack(side="left")  # Exibe a imagem ao lado da outra

    # Manter referência à imagem para evitar que ela seja destruída
    label.image = imagem_tk

def exibir_imagem_em_cinza(janela, caminho_imagem):
    """Exibe a imagem em tons de cinza na janela"""
    # Converter a imagem para tons de cinza
    img_cinza = carregar_e_converter_para_cinza(caminho_imagem)

    # Criar um rótulo para exibir a imagem em tons de cinza
    label = Label(janela, image=img_cinza)
    label.pack(side="left")  # Exibe a imagem ao lado da outra

    # Manter referência à imagem
    label.image = img_cinza

def exibir_imagem_preto_branco(janela, caminho_imagem, limiar=128):
    """Exibe a imagem convertida em preto e branco na janela"""
    # Converter a imagem para preto e branco
    img_pb = carregar_e_converter_para_preto_branco(caminho_imagem, limiar)

    # Criar um rótulo para exibir a imagem preto e branco
    label = Label(janela, image=img_pb)
    label.pack(side="left")  # Exibe a imagem ao lado da outra

    # Manter referência à imagem
    label.image = img_pb

def exibir_imagens_simultaneamente(caminho_imagem):
    """Exibe as 3 versões da imagem (colorida, cinza, preto e branco) simultaneamente"""
    # Criar a janela principal
    janela = Tk()
    janela.title("Exibição das Imagens")

    # Exibir as 3 versões da imagem
    exibir_imagem_colorida(janela, caminho_imagem)
    exibir_imagem_em_cinza(janela, caminho_imagem)
    exibir_imagem_preto_branco(janela, caminho_imagem)

    # Iniciar o loop da interface gráfica
    janela.mainloop()

# Caminho para a imagem PNG
caminho = "img.png"
exibir_imagens_simultaneamente(caminho)