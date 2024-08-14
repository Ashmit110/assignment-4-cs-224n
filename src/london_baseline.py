# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0
    

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    argp = argparse.ArgumentParser()
    argp.add_argument('--eval_corpus_path', default=None)
    args = argp.parse_args()
    
    from dataset import NameDataset
    data=open(args.eval_corpus_path,'r',encoding='utf-8').read()
    data = list(data.encode('utf-8').decode('ascii', errors='ignore').split('\n'))
    
    print("length of dataset is ",len(data)-1)
    predictions=['London' for i in range(len(data)-1)]
    
    pass
    total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
    ### END YOUR CODE ###
    accuracy=(correct/total)*100
    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
