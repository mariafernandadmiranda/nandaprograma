import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

def gerar_imagem_e_mostrar():  
    print("Olá! Euvou gerar imagens baseado em IA.")
    try:
        nome_usuario = input("Por favor, digite seu nome: ")
    print("\nMuito prazer, {nome_usuario}!")
   
    while True:
        try:
            prompt = input("[{nome_usuario}], por favor, me diga qual imagem você quer gerar (ex: 'um gato voando'): ")
            if prompt.strip():
                break
            else:
                print("A descrição da imagem não pode ser vazia. Tente novamente.")

    print("Preparando para gerar a imagem. Isso pode levar alguns minutos...")
  
ajuda do gemini!!!!

    # 4. Configuração e Geração da Imagem (O núcleo do código)
    model_id = "runwayml/stable-diffusion-v1-5"

    try:
        # Tenta usar a GPU (cuda) se disponível, senão usa a CPU (mais lento)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Carrega o pipeline e move para o dispositivo (GPU ou CPU)
        pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device == "cuda" else torch.float32)
        pipeline = pipeline.to(device)

      
        imagem = pipeline(prompt).images[0]

 
        print(" Imagem gerada com sucesso!")

        # Abre a imagem no visualizador padrão do sistema
        imagem.show()

if __name__ == "__main__":
    gerar_imagem_e_mostrar()
