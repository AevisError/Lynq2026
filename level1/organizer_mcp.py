from google import genai

print("in omcp")


def sendmsg(message):

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=[message]
    )
    print(response.text)



