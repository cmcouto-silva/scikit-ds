from typing import Union, Optional, List

import numpy as np
import pandas as pd


def compute_missing(df: pd.DataFrame, show_only_missing: bool = True, format_pct: bool = True):
    df_missing = (
        df.isna().sum()
        .sort_values(ascending=False)
        .to_frame('missing_count')
        .assign(missing_pct = lambda x: x / len(df))
        .rename_axis('feature')
    )
    
    if show_only_missing:
        df_missing = df_missing.query('missing_count>0')
    
    if format_pct:
        df_missing = df_missing.style.format('{:.2%}', subset='missing_pct')
    
    return df_missing


def compute_counts(
    data: Union[pd.DataFrame, pd.Series, np.ndarray], 
    col: Optional[str] = None, 
    by: Optional[Union[str, List[str]]] = None
) -> pd.DataFrame:
    """
    Compute the absolute and relative frequency counts

    Parameters
    ----------
    data : Union[pd.DataFrame, pd.Series, np.ndarray]
        The input data. This can be a pandas DataFrame, Series, or a numpy array.
    col : Optional[str], optional
        The column name in the DataFrame for which to compute the counts. This parameter 
        is not used if the input data is a Series or numpy array. By default None.
    by : Optional[Union[str, List[str]]], optional
        The column name or list of column names to group the DataFrame by before computing counts. 
        This parameter is only used if the input data is a DataFrame. By default None.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the absolute ('abs_count') and relative ('rel_count') frequency 
        counts of the values in the specified column or the entire data set if 'col' is None.

    Raises
    ------
    AssertionError
        If the input data is not a DataFrame, Series, or numpy array.
        If 'col' is None when input data is a DataFrame.
    """

    # Check if input data is either a dataframe, series, or numpy array
    assert type(data) in (pd.DataFrame, pd.Series, np.ndarray)
    
    # Compute counts for dataframe
    if isinstance(data, pd.DataFrame):
        assert col is not None, 'The `col` parameter should not be None when the input data is a dataframe'
        if by:
            grp = data.groupby(by)
            abs_count = grp[col].value_counts(normalize=False).to_frame('abs_count')
            rel_count = grp[col].value_counts(normalize=True).to_frame('rel_count')
        else:
            abs_count = data[col].value_counts(normalize=False).to_frame('abs_count')
            rel_count = data[col].value_counts(normalize=True).to_frame('rel_count')
    # Compute counts for series or numpy array
    else:
        data = pd.Series(data) if not isinstance(data, pd.Series) else data
        abs_count = data.value_counts(normalize=False).to_frame('abs_count')
        rel_count = data.value_counts(normalize=True).to_frame('rel_count')
    
    # Aggregate absolute and relative counts
    df_counts = pd.concat([abs_count, rel_count], axis=1)
    
    return df_counts


def show_duplicates(df, keys):
    return df[df[keys].duplicated(keep=False)].sort_values(keys)
