import subprocess
import os

def build_docker_image(image_name, dockerfile_path='.'):
    # Build Docker image
    try:
        subprocess.run(['docker', 'build', '-t', image_name, dockerfile_path], check=True)
        print(f'Docker image {image_name} built successfully.')
    except subprocess.CalledProcessError as e:
        print(f'Error building Docker image: {e}')

if __name__ == '__main__':
    # Set your Docker image name and optional Dockerfile path
    docker_image_name = 'reactappautomated'
    dockerfile_path = '.'  # By default, it looks for the Dockerfile in the current directory

    # Optionally, you can specify a different Dockerfile path
    # dockerfile_path = '/path/to/your/dockerfile'

    # Build Docker image
    build_docker_image(docker_image_name, dockerfile_path)
