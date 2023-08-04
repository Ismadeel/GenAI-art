import os 
import replicate

os.environ["REPLICATE_API_TOKEN"]='<YOUR API KEY>'


output = replicate.run(
    "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
    input={"prompt": "an astronaut riding a rainbow unicorn"},
)
# Zip file containing input images, hosted somewhere on the internet
# zip_url = "https://drive.google.com/uc?export=download&id=1BPdPj5s5R9ejpXaWHXHVgxsTQsU4A-ZQ"

# # Train the model
# lora_url = replicate.run(
#     "replicate/lora-training:b2a308762e36ac48d16bfadc03a65493fe6e799f429f7941639a6acec5b276cc",
#     input={"instance_data": zip_url, "task": "style"}
# )


lora_url = "https://replicate.delivery/pbxt/fdtiMuQFF1yQAS22N4JWR3epRbW7ea5shRBsSmFqJBceBTZFB/tmpmzwgpo3puc.safetensors"

output_url = replicate.run(
    "replicate/lora:97ec1b97e5e6a6476e45ba7211d368509bbf39c30a927e39637f3cb98b36ac91",
    input={
        "prompt": "IT company logo",
        "lora_urls": lora_url,
    },
)

print(output_url)
