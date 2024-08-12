### 下载BLIP模型，大概需要20分钟
from modelscope import snapshot_download

model_dir = snapshot_download('goldsj/blip2-opt-2.7b', 
                              cache_dir='/root/autodl-tmp/better_synth_baseline_autoDL/models', 
                              revision='master')