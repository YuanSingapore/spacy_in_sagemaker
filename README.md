## Build an efficient training & hosting workflow in SageMaker using spacy project

This repository contains the CloudFormation template and prewritten source code powering the spacy project detailed in [spacy project](https://spacy.io/usage/projects). Feel free to customize it to fit your use case and share with us what you build!


|-code
|--train.py
|--project.yml
|--requirements.txt
|--


* `train.py` is the script run by the SageMaker training job that kickstart your spacy project. You can modify this script to reuse the pipeline with your own model training code. The detailed 
* `project.yaml` is the CloudFormation template you use to deploy the pipeline in your account. this cloudformation defines the data assets required by the project, as well as the available commands and workflows.

* `requirements.txt` is the file that define all the necessary packages together with their version to be installed

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.

