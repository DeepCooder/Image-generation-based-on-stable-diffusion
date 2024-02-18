import torch
from clip import CLIP
from encoder import VAE_Encoder
from decoder import VAE_Decoder
from diffusion import Diffusion

import model_converter




def preload_models_from_standard_weights(ckpt_path, device):
    state_dict = model_converter.load_from_standard_weights(ckpt_path, device)

    encoder = VAE_Encoder().to(device=device, dtype=torch.float16)
    encoder.load_state_dict(state_dict['encoder'], strict=True)


    decoder = VAE_Decoder().to(device=device, dtype=torch.float16)
    decoder.load_state_dict(state_dict['decoder'], strict=True)

    diffusion = Diffusion().to(device=device, dtype=torch.float16)
    diffusion.load_state_dict(state_dict['diffusion'], strict=True)

    clip = CLIP().to(device=device, dtype=torch.float16)
    clip.load_state_dict(state_dict['clip'], strict=True)

    return {
            'clip': clip,
            'encoder': encoder,
            'decoder': decoder,
            'diffusion': diffusion,
        }
