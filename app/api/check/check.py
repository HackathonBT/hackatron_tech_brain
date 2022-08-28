from copy import copy
from typing import Dict, List
from app.services.bert import check_nlp


def check(list_text: List) -> List:
    text_to_front = []
    all_classes = []
    for check_text in list_text:
        class_prob_ = check_nlp(check_text)
        class_prob = class_prob_[0]
        color, probs = text_with_color(class_prob, all_classes)
        text_to_front.append(row_with_probs(check_text, color, probs))
    unused_classes = get_un_used_class(all_classes)
    if len(unused_classes) == 0:
        text_to_front.append({'row': 'Документ успешно проверен!', 'color': 'lime'})
    else:
        text_to_front.append({'row': f'Документ проверен, нет классификаторов! {str(unused_classes)}', 'color': 'purple'})

    return text_to_front


def row_with_probs(text: str, color: str, probs: Dict) -> Dict:
    text = text + ' ' + str(probs)
    return {'row': text, 'color': color}


def text_with_color(class_prob: list, all_classes: List) -> (str, Dict):
    yellow = {}
    red = {}
    green = {}
    color = 'red'
    res = {}
    max_prob = 0
    for i, prob in enumerate(class_prob):
        b = i+1
        if prob > 0.70:
            color = 'green'
            green[b] = prob
            res = copy(green)
            all_classes.append(i+1)
        elif prob > 0.50 and color != 'green':
            color = 'yellow'
            yellow[b] = prob
            res = copy(yellow)
        elif color != 'green' and color != 'yellow':
            if prob > max_prob:
                max_prob = prob
            red[b] = max_prob
            res = copy(red)

    return color, res


def get_un_used_class(classes_in_doc: list) -> set:
    class_set = set(range(1, 39))
    set_in_doc = set(classes_in_doc)
    return class_set - set_in_doc
