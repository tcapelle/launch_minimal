FROM pytorch/pytorch:latest

RUN python3 -m pip  install "timm==0.6.12" wandb tqdm

CMD ["/bin/bash"]
