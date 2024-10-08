# not writen by me.



# DO NOT MODIFY THIS FILE
# DO NOT EVEN LOOK AT THIS FILE
# 👀
# ...but since you already ARE looking, here's a free 🧁
# please close the file now kthxbye

import classifier

# Test set consists of tuples with list of 16 features and 1 class
data_test = (
    ([1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 4, 1, 0, 1], 1),
    ([1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 4, 1, 0, 1], 1),
    ([1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 2, 1, 0, 0], 1),
    ([0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1], 1),
    ([0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 2, 1, 0, 0], 2),
    ([0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 2, 1, 0, 0], 2),
    ([0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 2, 1, 1, 0], 2),
    ([0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 2, 1, 0, 1], 2),
    ([0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0], 3),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0], 3),
    ([0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 4, 1, 0, 0], 3),
    ([0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0], 4),
    ([0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0], 4),
    ([0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1], 4),
    ([0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1], 4),
    ([0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 4, 0, 0, 0], 5),
    ([0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 4, 1, 0, 0], 5),
    ([0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 6, 0, 0, 0], 6),
    ([0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 6, 0, 0, 0], 6),
    ([1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 6, 0, 0, 0], 6),
    ([0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 6, 0, 0, 0], 7),
    ([0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 6, 0, 0, 0], 7),
    ([0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], 7),
    ([0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 7),
)


def test_classifier():  # 1p
    n_correct_classifications = 0
    for features, class_int in data_test:
        if classifier.classify_animal(*features) == class_int:
            n_correct_classifications += 1
    assert n_correct_classifications > 5
    # everythin below was added by me
    if n_correct_classifications > 5: print("success", n_correct_classifications, "/", len(data_test))
    else: print("not success", n_correct_classifications, "/", len(data_test))


if __name__ == "__main__":
    test_classifier()