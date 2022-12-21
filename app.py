import gradio as gr
import openai

def factgenerator(text, num_facts, openaikey):

  if not text:
    return "Enter some text to check facts"

  facts = "one"

  if num_facts == 1:
    facts = "one"
  elif num_facts == 2:
    facts = "two"  
  elif num_facts == 3:
    facts = "three"
  elif num_facts == 4:
    facts = "four"  
  elif num_facts == 5:
    facts = "five"   

  openai.api_key = openaikey     

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="How long before the FBI raids @elonmusk's home?\nFBI\n• The FBI was founded in 1908 and is a federal investigative agency.\n\nElon Musk\n• Elon Musk is a South African-born American business magnate, investor, and inventor.\n\nSimilar to the above format, generate " + facts + " facts for each entity present in the text.\n" + text + "." + "\n\n",
  temperature=0.7,
  max_tokens=3900,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
  return response['choices'][0]['text']

with gr.Blocks() as demo:
    gr.Markdown(
    """
    <h1><center><b>FactGen</center></h1>

    """)
    gr.Markdown(
    """
    To get a better understanding of the text, this app gives facts about the entities present in the text. It uses OpenAI GPT3 in the backend, get your
    <a href = "https://beta.openai.com/account/api-keys">Openai key here</a> \n
    """)

    gr.Markdown(
        """
        **To use this space effectively**
        <br>- Enter your text in the input box or select one of the examples at the bottom. 
        <br>- Use dropdown to select the number of facts per entity.
        <br>- Enter your openai key </br>

        Please refer to the GitHub repo this Space is based on, here - <a href = "https://github.com/ravi03071991/FactGen">FactGen</a> .
        """
    )
    with gr.Row():
      with gr.Column():
        text = gr.Textbox(lines = 5, placeholder = "PM Modi to visit Tripura tomorrow; govt expects 72,000 to attend his public meeting", label = "Input")
        num_facts = gr.Dropdown([1, 2, 3, 4, 5],label="Click here to select Number of facts for each entity", value = 1)
        openaikey = gr.Textbox(lines = 1, label = "Enter Openai Key")
        text_button = gr.Button("Submit")
      with gr.Column():
        text_output = gr.Textbox(label = "Output")

    text_button.click(factgenerator, inputs=[text, num_facts, openaikey], outputs=text_output)
    # We can choose text from one of the following examples
    gr.Examples([["Elizabeth Warren Prods Tesla About Elon Musk and Twitter"], 
                                   ["Chelsea news and transfers LIVE: Christopher Nkunku confirmed, Bellingham move, Moukoko contract"],
                                   ["PM Modi to visit Tripura tomorrow; govt expects 72,000 to attend his public meeting"],
                                   ["Biden to deliver Patriot missiles to Ukraine as Zelenskyy visits Washington."],
                                   ["Meet the AI Pioneers Who Won The 2022 Princess of Asturias Award"]],
                inputs = [text])

demo.launch()
