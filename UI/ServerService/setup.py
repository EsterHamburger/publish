import setuptools

setuptools.setup(
    name="ServerService",
    version="1.0.0",
    packages=setuptools.find_packages("ServerService"),
    package_dir={"": "src"},
    install_requires=["python-dotenv", "pika", "fastapi", "uvicorn"],
    extras_require={"dev": ["pytest", "ruff"]},
)
