def summary(data_train):
    import pandas as pd
    import numpy as np
    from collections import Counter
    max_sale = data_train["SalePrice"].max()
    min_garea = data_train["GarageArea"].min()
    fstq_lotarea = np.percentile(data_train["LotArea"], 25)
    scd_ybuilt = Counter(data_train["YearBuilt"]).most_common(2)[1][0]
    mean_bed = data_train["BedroomAbvGr"].mean()
    return ([max_sale, min_garea, fstq_lotarea, scd_ybuilt, mean_bed])