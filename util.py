def split_dataframe(df, train_ratio):
    # Ensure the ratios < 1
    assert train_ratio < 1, "Ratios must less than 1"
    # Calculate the number of rows for the training set
    train_rows = int(df.shape[0] * train_ratio)

    # Split the dataframe
    train_df = df.iloc[:train_rows]
    test_df = df.iloc[train_rows:]

    return train_df, test_df