import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 702381553
alpha = 0.02


def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    p = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='two-sided')
    return p[1] < alpha
