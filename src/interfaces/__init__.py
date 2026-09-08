"""
SeedVR2 ComfyUI Nodes
Central registry for all SeedVR2 nodes
"""

from comfy_api.latest import ComfyExtension, io

from .video_upscaler import Starlight26VideoUpscaler
from .dit_model_loader import Starlight26LoadDiTModel
from .vae_model_loader import Starlight26LoadVAEModel


class Starlight26Extension(ComfyExtension):
    """Topaz Starlight 2.6 portable ComfyUI extension."""
    
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        """Return list of all SeedVR2 nodes"""
        return [
            Starlight26VideoUpscaler,
            Starlight26LoadDiTModel,
            Starlight26LoadVAEModel,
        ]


async def comfy_entrypoint() -> ComfyExtension:
    """ComfyUI V3 entry point"""
    return Starlight26Extension()


__all__ = [
    'Starlight26VideoUpscaler',
    'Starlight26LoadDiTModel',
    'Starlight26LoadVAEModel',
    'Starlight26Extension',
    'comfy_entrypoint',
]
