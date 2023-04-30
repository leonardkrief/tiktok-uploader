"""
TikTok Uploader Initialization
"""
import toml
from os.path import abspath, join, dirname
from .upload import upload_video, upload_videos

src_dir = abspath(dirname(__file__))
config = toml.load(join(src_dir, 'config.toml'))

__all__ = ['upload_video', 'upload_videos', 'config']
