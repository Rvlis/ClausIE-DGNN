import json
import tqdm
import copy
import random

all_res = list()
sentence_set = set()
obj = dict()

def generate_dataset(input_path, output_path_1w, output_path_3w, output_path_9w, type="train"):
    with open(output_path_1w, "w") as wf1:
        with open(output_path_3w, "w") as wf3:
            with open(output_path_9w, "w") as wf9:
                with open(input_path) as rf:
                    for unique_id, sentence in enumerate(rf.readlines()):
                        spans = sentence.split("\t")
                        if(len(spans) < 3): 
                            continue
                        # for item in spans:
                        #     print(item)
                        sentence = spans[0].strip()
                        if sentence and sentence not in sentence_set:
                            # print("sentence:", sentence)
                            if obj:
                                all_res.append(copy.deepcopy(obj))
                            # obj.clear()
                            obj["sentence"] = [sentence]
                            # print("obj.sentence:", obj["sentence"])
                            # input()
                            obj["extraction"] = list()
                            sentence_set.add(sentence)
                        subject = spans[1][spans[1].find("<arg1>")+6: spans[1].find("</arg1>")].strip()
                        predict = spans[1][spans[1].find("<rel>")+5: spans[1].find("</rel>")].strip()
                        object = spans[1][spans[1].find("<arg2>")+6: spans[1].find("</arg2>")].strip()
                        extraction = " ".join([subject, predict, object])
                        confidence = spans[2]
                        obj["extraction"].append([extraction.strip()])

                if type == "train":
                    random.shuffle(all_res)

                json.dump(all_res[:10000], wf1, indent=4)
                json.dump(all_res[:30000], wf3, indent=4)
                json.dump(all_res[:], wf9, indent=4)


generate_dataset("../data/train/4cr_comb_extractions.tsv", "./raw/train_1w.json", "./raw/train_3w.json", "./raw/train_9w.json")





