#this file uses latest version of langchain.

from langchain_community.document_loaders import YoutubeLoader
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
import os
from typing import Optional

# Load environment variables from a .env file
load_dotenv()

def summarize_youtube_video(video_id: str, language: str = "zh-Hans", translation: Optional[str] = None) -> str:
    """
    Summarizes the transcript of a YouTube video using Langchain's YoutubeLoader and OpenAI's GPT model.
    
    Args:
        video_id (str): The ID of the YouTube video to summarize.
        language (str, optional): The language code for the video's transcript. Defaults to "zh-Hans".
        translation (Optional[str], optional): The target language code for translation, if translation is required. Defaults to None.
    
    Returns:
        str: The summary of the YouTube video's transcript.
    """
    
    # Initialize the YoutubeLoader with the video ID and optional language and translation
    loader = YoutubeLoader(video_id, language=[language], translation=translation)

    # Load the transcript
    transcript = loader.load()
    print(transcript)
    
    # Initialize the ChatOpenAI model (make sure to set up your API key in the .env file)
    openai_api_key = os.getenv('OPENAI_API_KEY')
    chat_model = ChatOpenAI(api_key=openai_api_key)

    # Load the summarization chain
    summarize_chain = load_summarize_chain(chat_model)

    # Summarize the transcript
    summary = summarize_chain.invoke(transcript)

    return summary

# Example usage
summary = summarize_youtube_video("OhOc4n_LiFQ")
print(summary)
