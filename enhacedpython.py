import subprocess
import os
import logging

# Configure logging
logging.basicConfig(filename='build_docker_image.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def build_docker_image(image_name, dockerfile_path='.'):
    try:
        # Build Docker image
        subprocess.run(['docker', 'build', '-t', image_name, dockerfile_path], check=True)
        print(f'Docker image {image_name} built successfully.')
    except subprocess.CalledProcessError as e:
        # Log the error
        logging.error(f'Error building Docker image: {e}')
        # Raise the exception to propagate it further
        raise

if __name__ == '__main__':
    # Set your Docker image name and optional Dockerfile path
    docker_image_name = 'reactappautomated'
    dockerfile_path = '.'  # By default, it looks for the Dockerfile in the current directory

    # Optionally, you can specify a different Dockerfile path
    # dockerfile_path = '/path/to/your/dockerfile'

    try:
        # Build Docker image
        build_docker_image(docker_image_name, dockerfile_path)
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        # Log the unexpected error
        logging.error(f'An unexpected error occurred: {e}', exc_info=True)
