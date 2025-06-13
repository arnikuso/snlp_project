import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

model = joblib.load('text_classifier.pkl')

def load_data(file_path, tag_map):
    texts = []
    labels = []
    for line in open(file_path, encoding='utf-8'):
        line = line.strip()
        for tag, label in tag_map.items():
            if line.startswith(tag):
                texts.append(line[len(tag):].strip())
                labels.append(label)
                break
    return texts, labels



val_file = 'validation.txt'
gpt_file = 'gpt.txt'


val_tag_map = {'<01> ': 1, '<02> ': 2}
gpt_tag_map = {'<1> ': 1, '<2> ': 2}


val_texts, val_labels = load_data(val_file, val_tag_map)
gpt_texts, gpt_labels = load_data(gpt_file, gpt_tag_map)

val_preds = model.predict(val_texts)
gpt_preds = model.predict(gpt_texts)


print("=== VALIDATION SET ===")
print("Accuracy:", accuracy_score(val_labels, val_preds))
print(confusion_matrix(val_labels, val_preds))
print(classification_report(val_labels, val_preds))

print("\n=== GPT-GENERATED SET ===")
print("Accuracy:", accuracy_score(gpt_labels, gpt_preds))
print(confusion_matrix(gpt_labels, gpt_preds))
print(classification_report(gpt_labels, gpt_preds))
