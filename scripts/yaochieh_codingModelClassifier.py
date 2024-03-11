
import math
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc


modelCodons = ['TTT', 'TTC', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA',
               'CTG', 'ATT', 'ATC', 'ATA', 'ATG', 'GTT', 'GTC',
               'GTA', 'GTG', 'TCT', 'TCC', 'TCA', 'TCG', 'AGT',
               'AGC', 'CCT', 'CCC', 'CCA', 'CCG', 'ACT', 'ACC',
               'ACA', 'ACG', 'GCT', 'GCC', 'GCA', 'GCG', 'TAT',
               'TAC', 'CAT', 'CAC', 'CAA', 'CAG', 'AAT', 'AAC',
               'AAA', 'AAG', 'GAT', 'GAC', 'GAA', 'GAG', 'TGT',
               'TGC', 'CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG',
               'GGT', 'GGC', 'GGA', 'GGG', 'TGG', 'TAA', 'TAG',
               'TGA']


def scoreModels():
    codingMatrix = getProbs("../data/codingModel.tab")
    noncodingMatrix = getProbs("../data/noncodingModel.tab")

    id2ancestorSeq = getSeq("../data/pathgon_ancestor.fa")
    id2spaciiSeq = getSeq("../data/pathgon_mut.fa")

    allID = list(id2ancestorSeq.keys())
    results = []
    for ID in allID:
        cScore = 0
        nScore = 0

        ancestorSeq = id2ancestorSeq[ID]
        spaciiSeq = id2spaciiSeq[ID]

        assert len(ancestorSeq) == len(spaciiSeq)
        assert len(ancestorSeq) % 3 == 0

        for i in range(0, len(ancestorSeq), 3):
            ancestorCodon = ancestorSeq[i:i+3]
            spaciiCodon = spaciiSeq[i:i+3]

            cProb = codingMatrix[modelCodons.index(
                ancestorCodon)][modelCodons.index(spaciiCodon)]
            nProb = noncodingMatrix[modelCodons.index(
                ancestorCodon)][modelCodons.index(spaciiCodon)]

            cScore += math.log(cProb)
            nScore += math.log(nProb)

        # if cScore > nScore:
        #     print(ID + "is coding " + str(cScore)+" " + str(nScore))
        # else:
        #     print(ID + "is NOT coding " + str(cScore)+" " + str(nScore))
        # Instead of printing, store the results in the list with the true class (coding or not coding)
        true_class = 'c' if 'c' in ID else 'n'
        results.append((true_class, cScore, nScore))
    return results


def getProbs(f1):
    f = open(f1)
    pMatrix = []
    for line in f:
        tmp = line.rstrip().split("\t")
        tmp = [float(i) for i in tmp]
        pMatrix.append(tmp)
    return pMatrix


def getSeq(filename):
    f = open(filename)
    id2seq = {}
    currkey = ""
    for line in f:
        if line.find(">") == 0:
            currkey = (line[1:].split("|")[0])
            id2seq[currkey] = ""
        else:
            id2seq[currkey] = id2seq[currkey] + line.rstrip()
    f.close()
    return id2seq


if __name__ == "__main__":
    # Convert the results to a format suitable for ROC curve calculation
    # 0 is c-> n meaning prediction fails, 1 is n-> n meaning prediction success
    results = scoreModels()
    y_true = [1 if true_class == 'c' else 0 for true_class, _, _ in results]
    y_scores = [cScore-nScore for _, cScore, nScore in results]
    fpr, tpr, _ = roc_curve(y_true, y_scores)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2,
             label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC curve')
    plt.legend(loc="lower right")
    plt.show()
