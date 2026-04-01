FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

WORKDIR /app

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Dependências Python
RUN pip install --no-cache-dir \
    ultralytics \
    opencv-python-headless \
    torch torchvision \
    numpy

# Copia apenas os scripts (dataset fica nos volumes)
COPY train.py .
COPY detect.py .
COPY data.yaml .
COPY RemapLabel.py .
COPY ColetaDataset.py .

# Comando padrão
CMD ["python", "train.py"]