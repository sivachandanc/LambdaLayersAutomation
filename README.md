
# Lambda Layers Automation with Python

This repository contains a Python script that automates the creation and uploading of AWS Lambda Layers. The script uses Boto3 to interact with AWS services, argparse to parse command-line arguments, and pipreqs to generate a list of requirements from the project.

## Requirements
To run this script, you will need:

* Python 3.6 or higher
* AWS account with appropriate credentials
* pipreqs
* You can install pipreqs by running `pip install pipreqs` in your terminal.
## AWS CLI
Follow the medium article to install and configure AWS CLI
* [Medium Article](https://medium.com/@greg.farrow1/quick-start-guide-aws-cli-53254f84130)
## Usage

1. Cloning the repo

```
git clone https://github.com/sivachandanc/LambdaLayersAutomation.git

```
2. Navigate to the directory
```
cd LambdaLayersAutomation

```
3. Run the Script

```
python lambda_layers_automation.py -p <path_to_your_project> [-b <bucket_name> -pr <path_to_save_in_bucket>]

```
Replace `<path_to_your_project>` with the path to your project directory. If you want to upload the Lambda Layer to an S3 bucket, add the `-b` and `-pr` arguments with the name of the bucket and the path to save the file, respectively.

**Note:**
Make Sure the path doesn't end with **/**

4. The script will create a `python.zip` file in your project directory, which contains all the required packages for your Lambda function.

5. If you specified an S3 bucket to upload the Lambda Layer, the script will upload the `python.zip` file to the specified bucket and path.








## Functionality

The script performs the following functions:

1. `requirements()` - This function takes a path as an argument and creates a `requirements.txt` file in that path using pipreqs. If the `requirements.txt` file is created successfully, the function returns True. If not, it raises an exception. This function ensures that all the required packages and libraries for the Lambda function are listed in the `requirements.txt` file.

2. `layers_package()` - This function takes a path to a directory and creates a `python.zip` file in that directory. The zip file contains all the packages in the `requirements.txt` file in the directory. The function returns True if the zip file is created successfully and False if not. This function zips all the required packages in a single file so that we can upload it as a Lambda Layer.

3. `load_package()` - This function takes in the path of the zipped package, the name of the S3 bucket, and the path to save the file. It uses Boto3 to upload the zipped package to the specified S3 bucket. If the upload is successful, the function returns True, and if not, it raises an exception.
## Conclusion

AWS Lambda Layers are a powerful feature that can simplify the development and deployment of Lambda functions. By automating the creation and uploading of Lambda Layers with Python, you can save time and effort while ensuring that your Lambda function has all the required dependencies. With this script, you can easily manage your Lambda Layers and streamline your development process.

You can also read this on:[![Medium](https://img.shields.io/badge/medium-medium-black)](https://sivachandanc.medium.com/automating-the-creation-and-uploading-of-lambda-layers-in-aws-with-python-2bd70e0a03ba)
## 🚀 About Me

I am a highly motivated data engineer with 4 years of experience in designing, building and maintaining data pipelines. I have a passion for creating efficient and scalable solutions for managing and analyzing large amounts of data. My expertise includes working with various data storage systems, data integration techniques, and big data technologies such as Hadoop and Spark. I am also well-versed in programming languages such as Python and SQL. With my technical skills and attention to detail, I am confident in delivering high-quality data solutions to meet the needs of my clients.



## 🔗 Links
[![Medium](https://img.shields.io/badge/medium-medium-black)](https://sivachandanc.medium.com)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/siva-chandan-chakka/)

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Support

For support, email sivachandan1996@gmail.com
