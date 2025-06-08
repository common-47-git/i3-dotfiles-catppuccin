from gradio_client import Client

client = Client("rafaaa2105/flux-ghibsky-illustration")
result = client.predict(
		prompt="Night sea waves",
		seed=0,
		randomize_seed=True,
		width=1920,
		height=1080,
		guidance_scale=10,
		num_inference_steps=50,
		api_name="/infer"
)
print(result)