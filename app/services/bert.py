from transformers import BertTokenizer, BertForSequenceClassification
from typing import List
import torch

tokenizer1 = BertTokenizer.from_pretrained('sberbank-ai/ruBert-base', do_lower_case=False)
output_dir = 'app/services/model_save70/'
model = BertForSequenceClassification.from_pretrained(output_dir)
tokenizer = BertTokenizer.from_pretrained(output_dir)
print(list(model.named_parameters()))


def check_nlp(sent: str) -> List:
    encoded_sent = tokenizer.encode_plus(
        sent,  # Sentence to encode.
        add_special_tokens=False,  # Add '[CLS]' and '[SEP]'
        max_length=170,  # Pad & truncate all sentences.
        pad_to_max_length=True,
        return_attention_mask=True,  # Construct attn. masks.
        return_tensors='pt',  # Return pytorch tensors.
        truncation=True
    )
    input_ids = encoded_sent['input_ids']
    attention_masks = encoded_sent['attention_mask']
    #input_ids = torch.cat(input_ids, dim=0)
    #attention_masks = torch.cat(attention_masks, dim=0)
    result = model(input_ids,
                   token_type_ids=None,
                   attention_mask=attention_masks,
                   #labels=b_labels,
                   return_dict=True)
    probs = torch.nn.functional.softmax(result.logits, dim=1)
    return probs.tolist()
