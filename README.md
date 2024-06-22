# Vibe-Eval-Smol

Evaluation of small 1.68-8B size models on [reka-vibe-eval](https://github.com/reka-ai/reka-vibe-eval). Reka-flash and Claude-3-haiku included for comparison with medium-size models.

All model generations are in `evals`

## Vibe-Eval Score (%)

| Model                              | hard  | normal | all  | parameters |
|------------------------------------|-------|--------|------|------------|
| Claude-3.5-Sonnet                  | 53.75 | 72.78  | 65.71|            |
| Reka-flash                         | 39.2  | 52.2   | 59.9 | 21B        |
| Claude-3-Haiku-20240307            | 38.5  | 49.8   | 56.4 | 20B        |
| Reka Edge                          | 32.2  | 53.1   | 45.4 | 7B         |
| [Qwen-VL-Chat](https://huggingface.co/Qwen/Qwen-VL-Chat) | 30.87 | 47.19 | 41.2 | 8B         |
| [LLAVA-llama3-8b](https://huggingface.co/xtuner/llava-llama-3-8b) | 31.75 | 45.86 | 40.61 | 8B         |
| [qresearch/llama-3-vision-alpha](https://huggingface.co/qresearch/llama-3-vision-alpha) | 34.69 | 43.49 | 40.26 | 8B         |
| [Bunny-8b-V-Instruct](https://huggingface.co/BAAI/Bunny-Llama-3-8B-V) | 30.25 | 42.31 | 37.83 | 8B         |
| [Llama3-VILA](https://huggingface.co/Efficient-Large-Model/Llama-3-VILA1.5-8B?library=true) | 31 | 41.42 | 37.55 | 8B         |
| [LLava-Phi-3-mini-4k-instruct](https://huggingface.co/MBZUAI/LLaVA-Phi-3-mini-4k-instruct) | 29.75 | 37.13 | 34.39 | 3.8B       |
| [Moondream2](https://huggingface.co/vikhyatk/moondream2) | 24.24 | 38.61 | 33.3 | 1.86B      |
| [Nouse-Hermes2-Vision-Alpha](https://huggingface.co/NousResearch/Nous-Hermes-2-Vision-Alpha) | 25.51 | 25.74 | 25.66 | 7B         |

See this [spreadsheet](https://docs.google.com/spreadsheets/d/1TJmfGOqMyyVaclFz_EsAZozutAvA8bWjal2IC2LVGr8/edit?usp=sharing) for more details.

*NOTE: to the best of my knowledge, Reka-flash, Claude-Haiku, and Llama3-VILA are the only models trained on multiple images*

## Citation

```bibtex
@article{padlewski2024vibeeval,
  title={Vibe-Eval: A hard evaluation suite for measuring progress of multimodal language models},
  author={Piotr Padlewski and Max Bain and Matthew Henderson and Zhongkai Zhu and Nishant Relan and Hai Pham and Donovan Ong and Kaloyan Aleksiev and Aitor Ormazabal and Samuel Phua and Ethan Yeo and Eugenie Lamprecht and Qi Liu and Yuqi Wang and Eric Chen and Deyu Fu and Lei Li and Che Zheng and Cyprien de Masson d'Autume and Dani Yogatama and Mikel Artetxe and Yi Tay},
  journal={arXiv preprint arXiv:2405.02287},
  year={2024}
}
