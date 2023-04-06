import wandb
import numpy as np

PROJECT = "another_launch_project"
# ENTITY = "wandb"
ENTITY = None

default_config = dict(lr=0.001,epochs=10)

def train(config):
    run = wandb.init(project=PROJECT, entity=ENTITY, config=config)
    wandb.run.log_code()
    config = wandb.config
    for epoch in range(config.epochs):
        loss = np.random.random()
        run.log({"loss": loss, "epoch": epoch})
    run.finish()

if __name__ == "__main__": train(default_config)
    