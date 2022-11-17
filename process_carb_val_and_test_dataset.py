def process_carb_dataset(input_path, output_path):
    raw_sentences = set()
    with open(output_path, "w") as wf:
        with open(input_path) as rf:
            triple_num = 0
            for line in rf.readlines():
                items = line.split("\t")
                if len(items) != 4:
                    continue
                raw_sentence = items[0].strip()
                subject = items[2]
                predict = items[1]
                object = items[3]

                raw_sentences.add(raw_sentence)

                wf.write(raw_sentence + "\t" + predict + "\t" + subject + "\t" + object + "\n")
                triple_num += 1

    print("In {}: raws sentence num is {}, triples num is {}".format(output_path, len(raw_sentences), triple_num))


process_carb_dataset("../data/test/carb/extractions.tsv", "../data/test/carb/filtered_test_dataset.tsv")
process_carb_dataset("../data/dev/carb/extractions.tsv", "../data/dev/carb/filtered_dev_dataset.tsv")