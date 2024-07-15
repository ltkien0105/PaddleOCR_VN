import gdown
from pathlib import Path

#Config file
det_sast_config = "1VrkGxjTGeo4XN7CQZOX0zUJVJxHR0l1f"
rec_srn_config = "10NFTNDKrig0wfATqqhLWsuhh655WdVVU"

#Pretrain model
det_sast_model = "1_9oDB2SrO7lGBDyox6VIO-naRtUbz7R9"
rec_srn_model = "1__xHW4ATSpMcvAEJ5mbike1UT9Mt9YY0"

#Dataset
#Vietnamese train data
vietnamese_dataset = "11u4meCSJUplJvf9sj9LV8YY5Cuczx8ld"
private_dataset = "10A_kp20dAo5r60kbp1msn64RR8QR2S9Z"
train_data_1_dataset = "1M8_Yf8JrkH8HC6N5VPu426K8YmzCNCgm"
train_data_2_dataset = "1rwIk-zCRCvHoqaK3FyI5vu_jlJNGKDBJ"

#Best accuracy model
best_accuracy_model = "1_56MPK5SXtEb2Fv0p5zZiLhJL8ZKdPBN"

if not Path('configs/det').exists():
  Path('configs/det').mkdir(parents=True, exist_ok=True)
gdown.download(id=det_sast_config, output='configs/det/SAST.yml')

if not Path('configs/rec').exists():
  Path('configs/rec').mkdir(parents=True, exist_ok=True)
gdown.download(id=rec_srn_config, output='configs/rec/SRN.yml')

if not Path('pretrain_models').exists():
  Path('pretrain_models').mkdir(exist_ok=True)
gdown.download(id=det_sast_model, output='pretrain_models/det_r50_vd_sast_icdar15_v2.0_train.zip')
gdown.download(id=rec_srn_model, output='pretrain_models/rec_r50_vd_srn_train.zip')

if not Path('train_data').exists():
  Path('train_data').mkdir(exist_ok=True)
gdown.download(id=vietnamese_dataset, output='train_data/vietnamese.zip')

if not Path('output/SRN').exists():
  Path('output/SRN').mkdir(parents=True, exist_ok=True)
gdown.download(id=best_accuracy_model, output='output/SRN/best_accuracy.zip')