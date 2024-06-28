import os
from PIL import Image
import PIL

for i in range(3, 46+1):
    def resize_images(input_folder, output_folder, target_size=(600, 600)):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in os.listdir(input_folder):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)

                image = Image.open(input_path)
                
                resized_image = image.resize(target_size, PIL.Image.Resampling.LANCZOS)

                resized_image.save(output_path)
                print(f"Imagem {filename} redimensionada e salva em {output_folder}")

    input_folder = f"C:/Users/ti3/OneDrive/Área de Trabalho/autoPython/Nova pasta/imagens_raspadas{i}"

    output_folder = f"C:/Users/ti3/OneDrive/Área de Trabalho/autoPython/600x600_{i}"

    resize_images(input_folder, output_folder)
