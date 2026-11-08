# import torch
# from transformers import pipeline, GenerationConfig

# device = torch.device(
# "cuda" if torch.cuda.is_available() else "cpu"
# )

# pipe = pipeline(
# "text-generation",
# model="openai-community/gpt2",
# dtype=torch.float32,
# device=device,
# clean_up_tokenization_spaces=False,
# )

# def generate_text(text: str) -> str:
#     generation_config = GenerationConfig(
#         max_new_tokens=50,
#         do_sample=True,
#         temperature=1.0,
#         top_k=1000,
#         top_p=0.1
#     )

#     prompt = text

#     resultado = pipe(
#         prompt,
#         generation_config=generation_config,
#         return_full_text=True,
#     )
#     return resultado[0]["generated_text"]