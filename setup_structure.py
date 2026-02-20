import os
print("FILE IS RUNNING")

structure = {
    "data": {
        "raw": {},
        "processed": {
            "train": {
                "HR": {},
                "LR": {}
            },
            "val": {
                "HR": {},
                "LR": {}
            },
            "test": {
                "HR": {},
                "LR": {}
            }
        }
    },
    "src": {
        "datasets": {},
        "models": {
            "srgan": {},
            "edsr": {},
            "transformer": {}
        },
        "losses": {},
        "trainers": {},
        "utils": {},
        "inference": {}
    },
    "configs": {
        "srgan.yaml": None,
        "edsr.yaml": None,
        "transformer.yaml": None
    },
    "experiments": {},
    "checkpoints": {},
    "outputs": {
        "images": {},
        "logs": {}
    },
    "notebooks": {},
    "scripts": {}
}


def create_structure(base_path, structure_dict):
    for name, sub in structure_dict.items():
        path = os.path.join(base_path, name)

        # If value is None → create empty file
        if sub is None:
            open(path, 'a').close()
        else:
            os.makedirs(path, exist_ok=True)
            create_structure(path, sub)


if __name__ == "__main__":
    base_dir = os.getcwd()
    create_structure(base_dir, structure)
    print("✅ SR Project structure (SRGAN, EDSR, Transformer) created successfully!")