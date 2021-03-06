gcloud ai-platform jobs submit training randomforestclassifier \
       --module-name randomforestclassifier.task \
       --staging-bucket gs://api_local_test_bucket \
	--package-path randomforestclassifier \
	--stream-logs \
       --region us-central1 \
       --runtime-version 1.15 \
       --python-version 3.7 \
       -- \
       --trainFilePath gs://api_local_test_bucket/abhishek_r_testing/Datasets/Regression/train_reg_file1.csv \
       --trainOutputPath gs://api_local_test_bucket/abhishek_r_testing/Datasets/Regression/train_output_reg_file1.csv \
       --testFilePath gs://api_local_test_bucket/abhishek_r_testing/Datasets/Regression/test_reg_file1.csv \
       --testOutputPath gs://api_local_test_bucket/abhishek_r_testing/Datasets/Regression/test_output_reg_file1.csv \
       --outputFilePath gs://api_local_test_bucket/abhishek_r_testing/Outputs  
