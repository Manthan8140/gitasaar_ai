import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ.get("OPENROUTER_API_KEY"),
)

# Streamlit UI
st.title("GitaSaar - The Essence of Bhagavad Gita")
st.subheader("Discover the wisdom of the Bhagavad Gita")

# User input
user_input = st.text_input("Ask, and let the eternal wisdom answer.", "")

if st.button("Show me the Way"):
  if user_input.strip():
    # Display a placeholder for streaming response
    response_placeholder = st.empty()

    # Make API call with streaming
    completion = client.chat.completions.create(
      extra_body={},
      model="deepseek/deepseek-chat-v3-0324:free",
      messages=[
        {
          "role": "system",
          "content": "You're an expert in 'Bhagavat Gita' Shloka and its explanation in hindi and sanskrit for Shloka. Your task is to search the exact related shloka based on the given context and provide the explanation in hindi and sanskrit. You are not allowed to provide any other information or explanation."
        },
        {
          "role": "user",
          "content": f"""
          {user_input}

          [OUTPUT FORMAT]
          <Number of Shlokas: Do not include this in the output. eg. भगवद्गीता – अध्याय 2, श्लोक 14>
          <Shloka in Sanskrit: Do not include this in the output>

          अर्थात

          <Explanation in Hindi: Do not include this in the output>

          <Explanation in Hindi: Do not include this in the output>

          [EXAMPLE OUTPUT]
          भगवद्गीता – अध्याय 2, श्लोक 14
          मात्रास्पर्शास्तु कौन्तेय शीतोष्णसुखदुःखदाः।
          आगमापायिनोऽनित्यास्तांस्तितिक्षस्व भारत॥

          अर्थात्
          हे अर्जुन! इन्द्रियों और विषयों के संपर्क से सर्दी-गर्मी और सुख-दुःख उत्पन्न होते हैं। ये क्षणिक और परिवर्तनशील हैं। इसलिए, तू उन्हें धैर्यपूर्वक सहन कर।

          हिन्दी व्याख्या:
          यह श्लोक बताता है कि जीवन के सुख-दुःख स्थायी नहीं होते, वे इन्द्रिय-संपर्क से उत्पन्न होते हैं और समय के साथ बदलते रहते हैं। इन्हें सहन करना ही ज्ञान और स्थिरता का मार्ग है।
          """
        }
      ],
      stream=True,
    )

    # Stream the response
    text = ""
    for i in completion:
      text += i.choices[0].delta.content
      response_placeholder.text(text)
  else:
    st.warning("Please enter a query.")