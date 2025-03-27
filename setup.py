from setuptools import setup, find_packages

setup(
    name='aws_util',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'sphinx',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'ecs_connect = aws_util.ecs_utils:main',  # ecs_connect becomes the command
        ],
    },
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com', # Replace with your email
    description='A utility for interacting with AWS ECS.',
    url='https://github.com/yourusername/aws_util', # Replace with your repo URL
    classifiers=[
        'Development Status :: 3 - Alpha',  # Adjust as needed
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Replace with your license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='aws, ecs, boto3',
)
