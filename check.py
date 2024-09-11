import pkg_resources

# Danh sách các thư viện và phiên bản yêu cầu
requirements = {
    "numpy": "1.26.4",
    "openai": "1.12.0",
    "tenacity": "8.2.3",
    "tiktoken": "0.6.0",
    "transformers": "4.34.1",
    "pandas": "2.2.0",
    "scikit-learn": "1.4.0",
    "torch": "2.2.0+cu118",
    "bitsandbytes": "0.42.0",
    "datasets": "2.14.7",
    "sentencepiece": "0.1.99",
    "peft": "0.6.2",
    "evaluate": "0.4.1",
    "trl": "0.7.1",
    "protobuf": "4.25.2"
}

# Kiểm tra phiên bản
for package, required_version in requirements.items():
    try:
        installed_version = pkg_resources.get_distribution(package).version
        if installed_version == required_version:
            print(f"{package}: OK")
        else:
            print(f"{package}: Not OK (Current version: {installed_version})")
    except pkg_resources.DistributionNotFound:
        print(f"{package}: Not installed")

