# OneFormer Cityscapes Swin-Large Semantic Segmentation

본 실습에서는 Hugging Face에서 제공하는  
`shi-labs/oneformer_cityscapes_swin_large` pretrained 모델을 사용하여  
RealSense로 촬영한 실제 도로 영상에 Semantic Segmentation을 적용하였다.

OneFormer는 Semantic, Instance, Panoptic Segmentation을 지원하지만,  
본 실습에서는 Semantic Segmentation 기능만 사용하였다.

---

## 🎯 1. 실습 목표

본 실습의 목표는 Cityscapes 데이터셋으로 학습된 OneFormer Swin-Large 모델을 이용하여  
실제 도로 영상에서 주요 객체를 픽셀 단위로 분할하는 것이다.

주요 인식 대상은 다음과 같다.

- Road
- Sidewalk
- Building
- Vegetation
- Traffic Sign
- Traffic Light
- Person
- Car
- Truck
- Bicycle

최종적으로 모델의 Prediction Mask를 생성하고,  
원본 영상 위에 반투명하게 Overlay하여 Semantic Segmentation 결과 영상을 생성하였다.

---

## 🧠 2. 사용 모델

사용한 모델은 다음과 같다.

```text
shi-labs/oneformer_cityscapes_swin_large

### 참고 자료

- [Hugging Face - OneFormer Cityscapes Swin-Large](https://huggingface.co/shi-labs/oneformer_cityscapes_swin_large)
- [Hugging Face Transformers - OneFormer 공식 문서](https://huggingface.co/docs/transformers/model_doc/oneformer)
- [OneFormer 논문](https://arxiv.org/abs/2211.06220)
- [Cityscapes Dataset](https://www.cityscapes-dataset.com/)

본 실습에서 사용한 모델은 Cityscapes 데이터셋으로 사전 학습된 OneFormer 모델이며,
Backbone으로 Swin-Large를 사용한다.
---

## ⚙️ 3. 개발 환경

실험 환경은 다음과 같다.

| 항목 | 환경 |
|---|---|
| OS | Ubuntu 20.04 |
| Python | 3.8.10 |
| GPU | NVIDIA GeForce RTX 3060 Laptop GPU |
| VRAM | 약 6 GB |
| PyTorch | 2.4.1+cu121 |
| torchvision | 0.19.1+cu121 |
| Transformers | 4.46.3 |
| CUDA | 사용 |

### 환경 확인

Python 버전 확인:

```bash
python3 --version

---

## 🧩 5. OneFormer 모델 불러오기

OneFormer Cityscapes Swin-Large pretrained 모델을 불러온다.

```python
from transformers import (
    OneFormerProcessor,
    OneFormerForUniversalSegmentation
)

MODEL_NAME = "shi-labs/oneformer_cityscapes_swin_large"

processor = OneFormerProcessor.from_pretrained(MODEL_NAME)

model = OneFormerForUniversalSegmentation.from_pretrained(
    MODEL_NAME
)

import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model.to(DEVICE)
model.eval()

print("DEVICE:", DEVICE)

DEVICE: cuda

---

## 🧠 6. Semantic Segmentation Task 설정

OneFormer는 다음 세 가지 Task를 지원한다.

- Semantic Segmentation
- Instance Segmentation
- Panoptic Segmentation

본 실험에서는 Semantic Segmentation만 사용하였다.

입력 전처리 시 다음과 같이 설정한다.

```python
task_inputs=["semantic"]

---

## 🏷️ 7. Cityscapes 19개 클래스

OneFormer Cityscapes 모델은 총 19개의 클래스를 사용한다.

| ID | Class |
|---:|---|
| 0 | road |
| 1 | sidewalk |
| 2 | building |
| 3 | wall |
| 4 | fence |
| 5 | pole |
| 6 | traffic light |
| 7 | traffic sign |
| 8 | vegetation |
| 9 | terrain |
| 10 | sky |
| 11 | person |
| 12 | rider |
| 13 | car |
| 14 | truck |
| 15 | bus |
| 16 | train |
| 17 | motorcycle |
| 18 | bicycle |

모델에 저장된 클래스 정보는 다음 코드로 확인할 수 있다.

```python
print(model.config.id2label)

{
0: 'road',
1: 'sidewalk',
2: 'building',
3: 'wall',
4: 'fence',
5: 'pole',
6: 'traffic light',
7: 'traffic sign',
8: 'vegetation',
9: 'terrain',
10: 'sky',
11: 'person',
12: 'rider',
13: 'car',
14: 'truck',
15: 'bus',
16: 'train',
17: 'motorcycle',
18: 'bicycle'
}

