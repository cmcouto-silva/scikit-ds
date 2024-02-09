from sklearn import metrics

def clf_metrics(y_true, y_pred, y_proba=None):
    """
    Calculate various performance metrics for a classification model.

    Args:
    y_true (array-like): True labels.
    y_pred (array-like): Predicted labels.
    y_proba (array-like, optional): Predicted probabilities for the positive class.

    Returns:
    dict: A dictionary containing calculated metrics such as Accuracy, Balanced Accuracy, Recall, Precision, F1, and optionally ROC_AUC.
    """
    dict_metrics = {
        'Accuracy': metrics.accuracy_score(y_true, y_pred),
        'Balanced Accuracy': metrics.balanced_accuracy_score(y_true, y_pred),
        'Recall': metrics.recall_score(y_true, y_pred),
        'Precison': metrics.precision_score(y_true, y_pred),
        'F1': metrics.f1_score(y_true, y_pred),
    }

    if y_proba is not None:
        dict_metrics['ROC_AUC'] = metrics.roc_auc_score(y_true, y_proba)

    return dict_metrics
