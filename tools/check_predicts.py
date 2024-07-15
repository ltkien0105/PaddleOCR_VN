from sklearn.metrics import accuracy_score, classification_report

result_pred = []
with open('output/SRN/predicts_srn.txt', 'r', encoding='utf-8') as predicts_file:
    predicts = predicts_file.readlines()
    for predict in predicts:
        file_path, predict_result, _ = predict.split('\t')
        file_path = file_path.split('/')[-1]
        result_pred.append([file_path, predict_result])
    predicts_file.close()

result_pred.sort(key=lambda x: x[0])

result_true = []
with open('train_data/vietnamese/img_crop/crop_label_test.txt', 'r', encoding='utf-8') as crops_file:
    crops = crops_file.readlines()
    for crop in crops:
        file_path, result = crop.split('\t')
        result = result.replace('\n', '')

        result_true.append([file_path, result])
    crops_file.close()

result_true.sort(key=lambda x: x[0])

print(accuracy_score([x[1] for x in result_true], [x[1] for x in result_pred]))
print(classification_report([x[1] for x in result_true], [x[1] for x in result_pred]))