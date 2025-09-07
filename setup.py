"""Setup script for FlappyBird AI package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="flappybird-ai",
    version="2.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Deep Q-Learning AI agent that masters Flappy Bird",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/flappy-bird-ai",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/flappy-bird-ai/issues",
        "Documentation": "https://github.com/yourusername/flappy-bird-ai#readme",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Games/Entertainment",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "isort>=5.12.0",
            "pre-commit>=3.0.0",
        ],
        "viz": [
            "tensorboard>=2.10.0",
            "matplotlib>=3.5.0",
            "seaborn>=0.12.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "flappy-play=src.flappy:main",
            "flappy-train=src.ai.train_dqn:main",
            "flappy-demo=src.ai.play_dqn:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["assets/**/*", "model/*.pt", "configs/*.yaml"],
    },
    zip_safe=False,
)
