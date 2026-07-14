**Decision Tree Baseline**
A Decision Tree classifier was trained using the scaled training data with default setting of
max_depth=None.
Results
Training Accuracy = 1.0000
Test Accuracy =0.8621
**Overfitting Analysis**
The decision tree shows clear sign of overfitting. The model achieved a training accuracy of
100%, meaning it perfectly classified every training example. However , its test accuracy
dropped to 86.21% on unseen data.
This large gap between training and test performance indicates that the model has
memorized patterns and noise specific to training database rather than learning
generalizable relationships. As a result, the model performs substantially worse when
evaluated on new data
Why decision trees are high -variance models
They build the tree greedily, selecting the best split at each node based on the current
training data
Because of greedy process, small changes in the training data can lead to very difficult tree
structures and predictions. This sensitivity to the training data makes decision trees prone to
overfitting.
Ensemble methods such as Random forests reduce this variance by averaging predictions
from any different trees, resulting in better generalization and more robust performance.
**Bootstrap Confidence Interval for AUC Difference**
To evaluate whether the Logistic Regression model with C = 1.0 consistently outperforms the model with C = 0.01, a bootstrap analysis was performed using 500 bootstrap samples drawn from the test set.
For each bootstrap sample:
1.	Test-set observations were sampled with replacement.
2.	The AUC for the C = 1.0 model was computed.
3.	The AUC for the C = 0.01 model was computed.
4.	The AUC difference was calculated as:
AUC Difference = AUC(C = 1.0) − AUC(C = 0.01)
The distribution of 500 AUC differences was then summarized using its mean and a 95% bootstrap confidence interval.
Interpretation
If the 95% confidence interval excludes zero (both bounds are positive or both are negative), this indicates that the difference in AUC between the two models is likely consistent across different samples of data. In that case, the model with the higher AUC can be considered to have a reliable performance advantage.
If the 95% confidence interval includes zero, the observed AUC difference may be due to random sampling variation. In this situation, there is insufficient evidence to conclude that one model consistently outperforms the other, and the performance difference should be interpreted with caution.
For this experiment:
•	If both confidence interval bounds are greater than 0, then the C = 1.0 model consistently outperforms the C = 0.01 model.
•	If both confidence interval bounds are less than 0, then the C = 0.01 model consistently outperforms the C = 1.0 model.
•	If the interval spans zero, neither model demonstrates a statistically reliable advantage.

