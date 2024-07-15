import gdown
from pathlib import Path

#Config file
det_sast_config = "1VrkGxjTGeo4XN7CQZOX0zUJVJxHR0l1f"
rec_srn_config = "10NFTNDKrig0wfATqqhLWsuhh655WdVVU"

#Pretrain model
det_sast_model = "1_9oDB2SrO7lGBDyox6VIO-naRtUbz7R9"
rec_srn_model = "1__xHW4ATSpMcvAEJ5mbike1UT9Mt9YY0"

#Vietnamese train data
vietnamese_data = "11u4meCSJUplJvf9sj9LV8YY5Cuczx8ld"

#Best accuracy model
best_accuracy_model = "1pSg5NQ2uVVpnS903uT2icKHxv2UJDNWJ"

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
gdown.download(id=vietnamese_data, output='train_data/vietnamese.zip')

if not Path('output/SRN').exists():
  Path('output/SRN').mkdir(parents=True, exist_ok=True)
gdown.download(id=best_accuracy_model, output='output/SRN/best_accuracy.zip')