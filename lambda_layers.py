import os
import boto3
import argparse


def requirements(path:str)->bool:
    """
    This function takes a path as an argument and creates a requirements.txt file in that path.
    It uses pipreqs to create the requirements.txt file.
    It returns True if the requirements.txt file is created successfully.
    It raises an exception if the requirements.txt file is not created successfully.

    """
    
    try:

        os.system('pip install pipreqs')
        os.system(f'pipreqs --force {path} --ignore=python')
        return True
    
    except Exception as e:

        print('couldn\'t create')
        raise e

def layers_package(path:str)->bool:
    """
    This function takes in a path to a directory and creates a python.zip file in that directory.
    The zip file contains all the packages in the requirements.txt file in the directory.
    The function returns True if the zip file is created successfully.
    The function returns False if the zip file is not created successfully.

    """

    try:

        print("Creating a folder named python")

        os.system(f'rm -rf {path}/python')
        os.system(f'mkdir {path}/python')

        print('forming the command')
        command = 'pip install '
        with open(f'{path}/requirements.txt','r') as file:
            for line in file:
                command += line.strip()+' '
        command += f'--target={path}/python/'
        print(f"The command to be run is: {command}")
        os.system(command)
        os.system(f'zip -r9 {path}/python.zip {path}/python')

    except Exception as e:
        print("Couldn't create a layers package")
        raise e
    

def load_package(path:str,bucket_name:str,path_to_save:str):
    
    try:
        s3 = boto3.client('s3')
        file_path = path+'/python.zip'
        key = path_to_save+'/python.zip'
        s3.upload_file(file_path,bucket_name,key)
    except Exception as e:
        print("Couldn't upload the zipped package")
        raise e

    
if __name__=="__main__":
    parser = argparse.ArgumentParser(
                    prog = 'Lambda Layer Package Generator',
                    description = 'Produces Zip package for usage in Lmabda Layers and optionally stores in a S3 bucket',
                    epilog = 'For further help go to\
                    https://github.com/sivachandanc/LambdaLayersAutomation.git')

    
    
    parser.add_argument('-p','--path',required=True,help='Path of your project')

    parser.add_argument('-b','--bucket',required=False,\
        help='Bucket name where you want to upload the package')
    parser.add_argument('-pr','--prefixes', required=False,\
                        help='Path inside the bucket to save the file')
    
    
    args = parser.parse_args()
    if os.path.exists(args.path):
        requirements(path = args.path)
        layers_package(path = args.path)

    elif not os.path.exists(args.path):
        print('The Path you provided is not valid')
    
    if args.bucket is not None and args.prefixes is not None:
        load_package(path = args.path,bucket_name=args.bucket,path_to_save=args.prefixes)
        