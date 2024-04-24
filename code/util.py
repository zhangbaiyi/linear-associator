def split_dataframe(df, train_ratio):
    # Ensure the ratios < 1
    assert train_ratio < 1, "Ratios must less than 1"
    # Calculate the number of rows for the training set
    train_rows = int(df.shape[0] * train_ratio)

    # Split the dataframe
    train_df = df.iloc[:train_rows]
    test_df = df.iloc[train_rows:]

    return train_df, test_df

def binarize_pred(y_test, y_pred, binary=False):
    # Binarize the pred to -1 and 1
    # then times y_test
    # # bin_arr = np.array(list(map(lambda x: -1 if x>0 else 1, y_pred)))
    # bin_arr = y_pred if binary else np.array(list(map(lambda x: -1 if x<0 else 1, y_pred)))
    y_pred = pd.Series(y_pred, index=y_test.index)
    bin_arr = y_pred if binary else y_pred.apply(lambda x : 1 if x>=0 else -1)
    return bin_arr * y_test


def ff2(df):
    # plot the reutrn result
    return

def ff3(df):
    # plot the signal compare
    return

def sharp_ratio(df):
    return