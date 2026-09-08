# ComfyUI-Starlight26-RunningHub

Repository: <https://github.com/284951641/ComfyUI-LHStarlight26>

Topaz Starlight 2.6 portable ComfyUI adapter prepared for RunningHub.

## Nodes

- `星光2.6｜加载 DiT 模型`
- `星光2.6｜加载专用 VAE（柔和度）`
- `星光2.6｜视频超分`

The adapter uses the recovered Starlight 2.6 3B NaDiT architecture, the original
positive/negative embeddings, the Starlight temporal window `(1,3,3)`, one-step
distilled sampling, and the original default chunk/tile parameters.

## Required private model files

Weights are intentionally not included in this small node package. Upload the
following files separately and keep the filenames unchanged:

1. `starlight26_dit_3b_bf16.safetensors`
2. `starlight26_vae_bf16.safetensors`

Optional VAE decoder variants:

- `starlight26_vae_softness2_bf16.safetensors`
- `starlight26_vae_softness3_bf16.safetensors`

The loader searches ComfyUI's `SEEDVR2`, `diffusion_models`, `unet`, `vae`, and
`checkpoints` registered model paths. This allows RunningHub private model uploads
to be selected without copying multi-gigabyte files.

## Default parameters recovered from Starlight 2.6

- seed: `32`
- attention: `sdpa`
- CFG: `1.0`
- diffusion steps: `1`
- frame batch: `121`
- temporal overlap: `21`
- maximum output: `3840x2160`
- VAE encode tiles: `640`, overlap `80`
- VAE decode tiles: `480`, overlap `60`
- color correction: `wavelet`

## Scope

The weight payload and model architecture are complete and byte-audited. This is
a Linux/ComfyUI reimplementation of the runnable pipeline, not a redistribution
of the proprietary Windows `topaz_engine.zip` runtime. Online RunningHub execution
must still be verified after the node, workflow, and private model files are installed.
