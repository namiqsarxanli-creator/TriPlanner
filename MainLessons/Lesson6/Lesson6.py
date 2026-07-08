#Ev tapsirigi

# def tercume_et(metn,dil="ingilis"):
#     gemini_sorus="Bu mÉ™tni " + dil + " dilinÉ™ tÉ™rcÃ¼mÉ™ et: " + metn
#     return gemini_sorus
#
# print(tercume_et("salam,necesen?"))
# print(tercume_et("salam,necesen?","alman"))


# from openai import OpenAI
#
# client = OpenAI(
#         api_key=os.getenv("GROQ_API_KEY", ""),
#         base_url="https://api.groq.com/openai/v1"
#     )
# def groq_sorus(sual, model_adi="openai/gpt-oss-120b"):
#     cavab = client.chat.completions.create(
#         model=model_adi,
#         messages=[{"role": "user", "content": sual}]
#     )
#     return cavab.choices[0].message.content
#
#
# def tercume_et(metn, dil="ingilis"):
#     sual = "Bu mÉ™tni " + dil + " dilinÉ™ tÉ™rcÃ¼mÉ™ et: " + metn
#     cavab = groq_sorus(sual)
#     return cavab
#
#
# netice1 = tercume_et("salam necesen")
# netice2 = tercume_et("salam necesen", "alman")
#
# print(netice1)
# print(netice2)
