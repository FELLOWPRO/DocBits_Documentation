# Testing the model

## Steps to run classification tests to evaluate the accuracy and operational readiness of the model

To test the trained model and evaluate its accuracy and operational readiness, you can follow the steps below:

**Preparing the test data:**

* Collect a representative sample of test data covering different types of documents and scenarios that the model will handle in the field. Ensure that the test data is of high quality and correctly labeled.

**Running the classification tests:**

* Run the classification tests on the prepared test data.
* Feed the test data into the model and let the model make predictions for classifying the documents.

<figure><img src="../../../../../.gitbook/assets/docbits_model_prediction_test.png" alt="Docbits Model Prediction Test" width="375"><figcaption><p>Setting</p></figcaption></figure>

* Add a new one or edit an existing classification rule.

<figure><img src="../../../../../.gitbook/assets/docbits_classification_extraction_settings.png" alt="Docbits Classification Extraction Settings"><figcaption><p>Settings: Classification and Extraction</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/docbits_configure_classification_rule.png" alt="Docbits Configure Classification Rule" width="276"><figcaption><p>Configure classification Rule</p></figcaption></figure>

**Evaluating the model accuracy:**

* Compare the model's predictions with the actual classifications of the test data. Calculate metrics such as accuracy, precision, recall, and F1 score to evaluate the model's performance. These metrics provide insight into how well the model classified the documents and how reliable it is.

<figure><img src="../../../../../.gitbook/assets/docbits_model_training_metrics.png" alt="Docbits Model Training Metrics"><figcaption></figcaption></figure>

**Analyze errors:**

* Examine the errors the model made when classifying the test data and analyze their causes. Identify patterns or trends in the errors and, if necessary, make adjustments to the model to improve its performance.

**Optimize the model**:

* Based on the results of the classification tests and error analysis, you can optimize the model by adding training data, adjusting training parameters, or changing the model architecture. Repeat the testing process to check if the optimizations improved the model's performance.

**Document the results:**

* Document the results of the classification tests and any adjustments or optimizations made to the model. This will help you track the model's progress over time and ensure that it is constantly improving.

By regularly running classification tests and evaluating the performance of your model, you can ensure that it is suitable for use in production and delivers accurate results.
