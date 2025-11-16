FROM rayproject/ray:latest-py311

# Set shell to bash
SHELL ["/bin/bash", "-c"]

# Copy requirements
COPY requirements.txt /tmp/requirements.txt

# Create conda environment
# RUN conda create -n .pytorch_ray python=3.11 -y

# Set environment variables
# ENV PATH=/opt/conda/envs/.pytorch_ray/bin:$PATH
# ENV CONDA_DEFAULT_ENV=.pytorch_ray

# Install PyTorch with CUDA 12.6
RUN conda run pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126

# Install requirements
RUN conda run pip install -r /tmp/requirements.txt


