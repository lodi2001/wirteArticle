import openai                                                                                                                                                      
import tiktoken                                                                                                                                                    
from bertopic.representation import OpenAI                                                                                                                         
from bertopic import BERTopic    
client = openai.OpenAI(api_key="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")

def perform_topic_modelling(data):                                                                                                                                     
      # Original code from functions.py                                                                                                                                  
                                                                                                                                       
                                                                                                                                                                         
      prompt = """<|system|>You are a helpful, respectful, and honest assistant for labeling topics..<|user|>                                                            
      I have a topic that contains the following documents:                                                                                                              
      [DOCUMENTS]                                                                                                                                                        
                                                                                                                                                                         
      The topic is described by the following keywords: '[KEYWORDS]'.                                                                                                    
                                                                                                                                                                         
      Based on the information about the topic above, please create a short label of this topic. Make sure you to only return the label and nothing                      
  more.<|assistant|>"""                                                                                                                                                  
      # Tokenizer                                                                                                                                                        
      tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")                                                                                                           
                                                                                                                                                                         
      # Create your representation model                                                                                                                                 
      representation_model = OpenAI(                                                                                                                                     
          client,                                                                                                                                                        
          model="gpt-3.5-turbo",                                                                                                                                         
          delay_in_seconds=2,                                                                                                                                            
          chat=True,                                                                                                                                                     
          nr_docs=15,                                                                                                                                                     
          prompt=prompt,                                                                                                                                                 
          doc_length=250,                                                                                                                                                
          tokenizer=tokenizer                                                                                                                                            
      )                                                                                                                                                                  
                                                                                                                                                                         
      topic_model = BERTopic(representation_model=representation_model)                                                                                                  
      return  topic_model  

def get_gpt_content(single_text,context_list):

  # Modify the 'content' of the 'user' role message to use f-strings for dynamic variables
  response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
    {
      "role": "system",
      "content": "You are a helpful, respectful, and honest assistant for writing a literature review section in an academic article."
    },
    {
      "role": "user",
      "content": f"I have a topics {single_text} that  contain the following context: {context_list}.\n"
    },
    {
      "role": "assistant",
      "content": "Based on the information about the topic above, please create a literature review section . \n"
    }
  ],
   temperature=0.7,
   max_tokens=500,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0
)
  
  return response.choices[0].message.content